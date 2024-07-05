#from https://huggingface.co/docs/transformers/en/training

from datasets import load_dataset
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
import numpy as np
import evaluate
from transformers import TrainingArguments, Trainer
import torch
import os
#print("NVLINK DISABLE ENV?", os.getenv("NCCL_P2P_DISABLE"))
tmpdir = os.getenv("TMPDIR")
dataset = load_dataset("yelp_review_full")#, cache_dir=tmpdir)

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")#, cache_dir=tmpdir)


def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)


tokenized_datasets = dataset.map(tokenize_function, batched=True)

train_dataset = tokenized_datasets["train"].select(range(20000))
eval_dataset = tokenized_datasets["test"].select(range(20000))

model = AutoModelForSequenceClassification.from_pretrained("bert-base-cased", num_labels=5)#, cache_dir=tmpdir)

def get_optimal_batch_size():
    if torch.cuda.is_available():
        total_memory = torch.cuda.get_device_properties(0).total_memory
        print("amout of GPU memory",total_memory)
        # Example logic to determine batch size, this may need to be adjusted
        # The base batch size and memory per batch can be tuned based on the model and sequence length
        base_batch_size = 8
        memory_per_batch = 0.70 * 1024 * 1024 * 1024  # Assume each batch takes 2GB of memory
        max_batch_size = int(total_memory // memory_per_batch)
        return min(max_batch_size, 60)
    else:
        print("cuda not found")
        # Default batch size if no GPU is available
        return 2

batch_size = get_optimal_batch_size()

print("BATCH SIZE", batch_size)

training_args = TrainingArguments(output_dir="output_dir", 
        dataloader_num_workers=2, 
        dataloader_pin_memory=True, 
        per_device_train_batch_size=batch_size, 
        per_device_eval_batch_size=batch_size*2, 
        eval_strategy="epoch", 
        save_strategy="epoch")

metric = evaluate.load("accuracy")

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    compute_metrics=compute_metrics,
)

trainer.train()

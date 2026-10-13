This guide is intended for IEETA HPC (pleiades) administrators and covers how to update and use spack to install modules using the softadm account.

# Environments

SPACK environments are used to segregate the main production environment from accidental changes and updates. In the following sections, we look at how to use them to install packages.

## Install a package

Installing a package is a 3-step job from adding it to installing it in production. It starts with using the pre-existing enviroment (ubuntu24-stack) to add the package:

```bash
spack -e /apps/local/spack/environments/ubuntu24-stack add ...
```

Then we need to concretize the package into the list using:

```bash
spack -e /apps/local/spack/environments/ubuntu24-stack concretize -f
```

Then once everything is done, we promote it to production and install it using:

```bash
spack -e /apps/local/spack/environments/ubuntu24-stack install -j16
spack module lmod refresh -y
```

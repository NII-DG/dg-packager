# DG-Packager

RO-Crate Generate tools

## Installation

 - Python : >= 3.8

1. install dg-packager

    ```bash
    # Install from PyPI [TODO: not available yet]
    $ pip install dg-packager

    OR

    # install from source [TODO: not available yet]
    $ mkdir {dir to clone dg-packager repository}
    $ cd {dir to clone dg-packager repository}
    $ git clone <this repo>
    $ cd dg-packager
    $ python3 -m pip install .
    ```

2. install nii-dg(SDK library)

    ```bash
    $ mkdir {dir to clone nii-dg repository}
    $ cd {dir to clone nii-dg repository}

    $ git clone https://github.com/NII-DG/nii-dg.git
    $ cd nii-dg
    $ python3 -m pip install .
    ```

## Usage

### Getting RO-Crate from Raw metadata derived from some Data Storage Platform

1. For Gin-Fork

   Step 1. Getting Raw Metadata from Gin-fork API

   1. Access ```[GET] https://ginfork.sample.domain/api/v1/repos/{repo_id}/{branch_name}/metadata```

        ※[GIN-fork API for getting metadta](https://github.com/NII-DG/gogs/blob/develop/4Q_20230329/docs/api/gin-fork_api.yaml)

   Step 2. Getting Ro-Crate from Raw Metadata derived from Gin-Fork

    ```python
    from from dg_packager.ro_generator.gin_ro_generator import GinRoGenerator
    from dg_packager.error.error import JsonValidationError, RoPkgError

    try:
        # Raw Metadata(Json; dict) acquired from Gin-fork API(by  1 step) give Generate Function.
        ro_crete = GinRoGenerator.Generate(raw_metadata)
        # you are able to obtain Ro-Crate(JSOn; dict).
    except JsonValidationError as e:
        # If given Raw Metadata to Function is invalid format, exception occurs.(derived dg-packager)

        # (Do something.....)

    except RoPkgError as e:
        # If each value of metadata is invalid on checking property, exception occurs.(derived SDK Library)

        # (Do something.....)
    ```

2. For AAAAA



## Branch and Release Info

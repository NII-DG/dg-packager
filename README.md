# DG-Packager

RO-Crate Generate tools

## Function

* Packaging of research metadata obtained from various services into RO-Crate in compliance with the nii-dg library schema.
  * Support Services
    1. [GIN-fork](https://dg.nii.ac.jp/)

## Installation

- Python : >= 3.9

1. Install dg-packager

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

2. Install [nii-dg library](https://github.com/NII-DG/nii-dg)

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
    import json

    try:
        # Raw Metadata(Json; dict) acquired from Gin-fork API(by  1 step) give Generate Function.
        ro_crete = GinRoGenerator.Generate(raw_metadata)
        # you are able to obtain Ro-Crate(Json; dict).
        print(json.dumps(ro_crete, indent=4))
    except JsonValidationError as e:
        # If given Raw Metadata to Function is invalid format, exception occurs.(derived dg-packager)
        print(e)
        # e.g.: {'required_key': ['invalid_key_name', /....................], 'invalid_value_type': ['error_msg', ......], 'invalid_value' :['error_msg', ......]}


        # (Do something.....)

    except RoPkgError as e:
        # If each value of metadata is invalid on checking property, exception occurs.(derived nii-dg Library)
        print(e)
        # {'results': [{'<ginfork.File Dockerfile>': {'name': 'This property is required, but not found.', 'sdDatePublished': 'The value is invalid format.'}}, {'<ginfork.File LICENSE>': {'name': 'This property is required, but not found.'}}]}

        # (Do something.....)
    ```

## Branch and Release Management

- `main`: Latest Release Branches
  - Direct push to main is prohibited.
- `develop/<name>`: branch for development
- `feature/<name>`: branch for each function/modification
  - Basically, create a `feature/<name>` branch from `develop/<name>` and merge it into the `develop/<name>` branch.

Release work is done by creating a PR from `develop/<name>` to `main`, which is then merged after receiving the RV.

## License

[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0).
See the [LICENSE](./LICENSE).
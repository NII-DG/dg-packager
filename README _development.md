# dg-packager development document

## Preparation

1. Install Python >= 3.9

2. Clone dg-packaget repository
   - [dg-packaget repository](https://github.com/NII-DG/dg-packager)

    ```bash
    git clone https://github.com/NII-DG/dg-packager.git
    ```

3. Create virtual environment

    ```bash
    {your working dir} > cd dg-packager
    {your working dir}/dg-packager> py -3.10 -m venv env-dg-pkg
    ```

4. Activate virtual environment

    ```bash
    {your working dir}/dg-packager> env-dg-pkg/Scripts/Activate.ps1
    ```

5. Install nii-dg SDK library

   - [nii-dg repository](https://github.com/NII-DG/nii-dg)

6. (Option) Deactivate virtual environment

    ```bash
    {your working dir}/dg-packager> deactivate
    ```
# Examples of PROTOplast

This repository has example notebooks which showcase how you can use PROTOplast for ML development on scRNA-seq data.

## How to set up environment for the notebooks

### Step 1: Clone the repo

```bash
git clone git@github.com:dataxight/protoplast-ml-example.git
```


### Step 2: Update submodules

We have submoduled TabNet and SIMS, as they require updates due to API changes.  Once these changes have been accepted into their respective repos, the submodules will no longer be necessary

```bash
cd protoplast-ml-example
git submodule init
git submodule update
```

### Step 3: Setup the environment

We use uv to install all dependencies, including the submodules themselves
```bash
uv sync
uv pip install -e submodules/tabnet
uv pip install -e submodules/SIMS
```bash


### Step 4: 

Start Jupyter Lab

```bash
uv run jupyter lab
```

## Resources

PROTOplast:

- [Website](https://wwww.dataxight.com/services/protoplast)
- [Github](https://github.com/dataxight/protoplast)
- [Documentation](https://protoplast.dataxight.com)

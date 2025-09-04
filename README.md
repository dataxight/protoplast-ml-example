# protoplast-ml-example

[![Release](https://img.shields.io/github/v/release/dataxight/protoplast-ml-example)](https://img.shields.io/github/v/release/dataxight/protoplast-ml-example)
[![Build status](https://img.shields.io/github/actions/workflow/status/dataxight/protoplast-ml-example/main.yml?branch=main)](https://github.com/dataxight/protoplast-ml-example/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/dataxight/protoplast-ml-example/branch/main/graph/badge.svg)](https://codecov.io/gh/dataxight/protoplast-ml-example)
[![Commit activity](https://img.shields.io/github/commit-activity/m/dataxight/protoplast-ml-example)](https://img.shields.io/github/commit-activity/m/dataxight/protoplast-ml-example)
[![License](https://img.shields.io/github/license/dataxight/protoplast-ml-example)](https://img.shields.io/github/license/dataxight/protoplast-ml-example)

protoplast ml examples

- **Github repository**: <https://github.com/dataxight/protoplast-ml-example/>
- **Documentation** <https://dataxight.github.io/protoplast-ml-example/>

## Getting started with your project

### 1. Clone the repository

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```
git clone git@github.com:dataxight/protoplast-ml-example.git
```

Get the submodules
```
git submodule init
git submodule update
```

Opening up the workspace
`uv run marimo edit notebooks/`
You can commit the marimo python files directly after you finished your development

### 2. Set Up Your Development Environment

Then, install the environment and the pre-commit hooks with

```bash
make install
```

This will also generate your `uv.lock` file


### 3. Development

Edit the code in scripts/example.py, then run it
```
uv run python scripts/example.py
```

### 4. Commit the changes

Lastly, commit the changes made by the two steps above to your repository.

```bash
git add .
git commit -m $MESSAGE
git push origin $BRANCH
```


You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPI, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/codecov/).

## Releasing a new version

- Create an API Token on [PyPI](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting [this page](https://github.com/dataxight/protoplast-ml-example/settings/secrets/actions/new).
- Create a [new release](https://github.com/dataxight/protoplast-ml-example/releases/new) on Github.
- Create a new tag in the form `*.*.*`.

For more details, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/cicd/#how-to-trigger-a-release).

---

Repository initiated with [fpgmaas/cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv).

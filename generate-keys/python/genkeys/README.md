# genkeys


## Setup

Pre-req: Install a version of python with pyenv

Set a Python version (aligned with pyproject.toml):
```SH
pyenv shell 3.12.4
```

Create virt env with active pyenv Python:
```SH
poetry env use python
```

Activate:
```SH
poetry shell
```

Install dependencies from poetry.lock:
```SH
poetry install
```

Show deps:
```SH
poetry show
```

Select your active virt env in VScode so it can resolve the deps

## Packages Added

poetry add bip-utils


```SH
py_ver=3.12.4; env_name=crypto-utils
pyenv virtualenv $py_ver $env_name; pyenv activate $env_name; pip install -r requirements.txt
pyenv deactivate; yes | pyenv virtualenv-delete $env_name
```


# genkeys

## Docs

https://bip-utils.readthedocs.io/en/latest/bip_utils/bip/bip39/bip39_mnemonic.html

The list of tokens supported by bip44:
https://bip-utils.readthedocs.io/en/latest/bip_utils/bip/conf/bip44/bip44_coins.html#bip_utils.bip.conf.bip44.bip44_coins.Bip44Coins.CARDANO_BYRON_ICARUS


## Poetry Env Setup

Pre-req: Install a version of python with pyenv (e.g. 3.12.4)

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


## Notes

- BIP-44 stands for Bitcoin Improvement Proposal 44, which defines a standard for hierarchical deterministic (HD) wallets.
- BIP-44 builds on BIP-32 (HD wallets) and BIP-39 (mnemonics).
- It uses a single master seed to deterministically generate a hierarchical tree of keys.


## Example Tokens Supported

CARDANO_BYRON_ICARUS
BITCOIN
ETHEREUM


## Not used

```SH
py_ver=3.12.4; env_name=crypto-utils
pyenv virtualenv $py_ver $env_name; pyenv activate $env_name; pip install -r requirements.txt
pyenv deactivate; yes | pyenv virtualenv-delete $env_name
```


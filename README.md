Limited Bank API (Wise)
=======================

The limited banking API allows accessing a bank account of the Wise bank.


It can display:

- only a selection of transactiopns
- transfers that match
- transfers added together by a certain rule

This is the backbone of transparent banking transactions.

## Development


Install the package for development.

```sh
pip install -e .[dev] --upgrade
```

Run the tests:

```sh
pytest
```

We also use `tox` to run tests.

```sh
tox
```

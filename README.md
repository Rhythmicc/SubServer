# SubServer

FastAPI with sub-clash, support update config, and get config url wrapped.

## Install

```shell
pip3 install git+https://github.com/Rhythmicc/sub-clash.git -U
pip3 install git+https://github.com/Rhythmicc/SubServer.git -U
```

## Usage

```shell
SubServer serv
```

## Developer

If you need use global config, just edit `__config__.py`:

1. make `enable_config = True`.
2. edit `questions` list.
3. using `config` at `main.py`.

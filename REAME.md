# ansible-test

## Bootstrap

```shell
uv init
uv add --dev molecule ansible-lint 'molecule-plugins[docker]' ruff
uv add ansible

ansible-galaxy role init roles/common
cd roles/common
molecule init scenario --driver-name docker
```

## Set up

```shell
uv sync
source .venv/bin/activate
```

## Molecule

```shell
# All
molecule test

# Or
molecule create
molecule converge
molecule idempotence
molecule verify
molecule destry
```

## Lint

```shell
ansible-lint
ruff format
ruff check
```

# Cloudnull filesystems Collection for Ansible

This collection includes helpful Ansible roles and content to help with automating the deployment of file systems at cloudnull.

See example playbooks within the collection for how the roles and modules may be used.

Roles included in this collection (click on the link to see the role's README and documentation):

  - `cloudnull.filesystems.btrfs`
  - `cloudnull.filesystems.format`
  - `cloudnull.filesystems.lvg`
  - `cloudnull.filesystems.mdadm`
  - `cloudnull.filesystems.zfs_pool`
  - `cloudnull.filesystems.zfs_replicate`
  - `cloudnull.filesystems.zfs_setup`

> All roles use input validation to ensure types are correct. Detailed documentation on defaults and other variables can always
  be found in `defaults/main.yml`.

## Installation

Install via Ansible Galaxy:

```
ansible-galaxy collection install cloudnull.filesystems
```

Or include this collection in your playbook's `requirements.yml` file:

``` yaml
---
collections:
  - name: cloudnull.filesystems
```

## Running Local Tests

All roles have testing which can be executed in CI or locally. This is an example of running molecule locally to
test one of the roles within this collection.

``` shell
apt install python3-pip

pip install ansible-core molecule

~/.local/bin/ansible-galaxy collection install git@github.com:cloudnull/ansible-collection-filesystems.git -U

pushd ~/.ansible/collections/ansible_collections/cloudnull/filesystems/molecule
  export MOLECULE_BASE_CONFIG="$(pwd)/molecule-base.yaml"
popd

pushd ~/.ansible/collections/ansible_collections/cloudnull/filesystems/roles/zfs_setup
  molecule --debug --base-config "${MOLECULE_BASE_CONFIG}" test --scenario-name "default"
popd
```

> While `molecule` can be used within containers, vagrant, and VMs, it can also consume the host which it is running
  on. The above example expects tests are run from a dedicated machine; additionally different roles implement
  different drivers which have varying levels of system isolation.

## License

MIT

## Author

This collection was created by [Cloudnull](https://cloudnull.io).

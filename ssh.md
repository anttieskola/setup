Should be pre-installed most likely on all distros.

- Debian package name openssh-server

Known hosts are found in ~/.ssh/known_hosts. (Can be manually remove single)

Copied keys are found in ~/.ssh/authorized_keys

Generated id's are found in ~/.ssh/id_xxx. These atleast can be reused on any nix host. But if you change hostname and copy your id to remote it keeps old name...

# Easylogin
Generate key (currently default is already 3072)
```bash
ssh-keygen -t rsa
```
Copy key to remote host
```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub antti@zeus
```


# Sources
- ```man ssh-keygen```
- ```man ssh-copy-id```
- [Debian wiki](https://wiki.debian.org/SSH#Using_shared_keys)

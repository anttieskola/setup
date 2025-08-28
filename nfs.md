# NFS file share between linux

## NFSv4 server setup

```bash
sudo ufw allow from 192.168.1.0/24 to any port 2049 proto tcp
sudo ufw allow from 192.168.1.0/24 to any port 2049 proto udp
sudo ufw reload

sudo apt install nfs-kernel-server
sudo nano /etc/exports
```

```ini
/mnt/fast       192.168.1.0/24(rw,sync,fsid=0,no_subtree_check)
/mnt/vault1     192.168.1.0/24(rw,sync,fsid=0,no_subtree_check)
```

```bash
sudo exportfs -a
sudo systemctl restart nfs-kernel-server
```

## NFSv4 client setup

```bash
sudo apt install nfs-common
sudo mount -t nfs4 storage:/mnt/storage0 /mnt/storage0
```

### fstab

```ini
storage:/mnt/storage0 /mnt/storage0 nfs4 defaults,_netdev,nofail 0 0
```

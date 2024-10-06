# Creating crypted filesystem
1. Install cryptsetup
```bash
sudo apt install cryptsetup
```
2. Use fdisk to create empty linux partition (lsblk / lsblk -f to list all block devices)
3. Encrypt the partition
```bash
sudo cryptsetup luksFormat /dev/sdX1
```
4.Open the encrypted partition
```bash
sudo cryptsetup luksOpen /dev/sdX1 my_encrypted_volume
```
5. Create a filesystem on the encrypted partition
```bash
sudo mkfs.ext4 /dev/mapper/my_encrypted_volume
```
6. Mount the encrypted partition
```bash
sudo mount /dev/mapper/my_encrypted_volume /mnt/my_encrypted_volume
```
7. Unmount the encrypted partition
```bash
sudo umount /mnt/my_encrypted_volume
sudo cryptsetup luksClose my_encrypted_volume
```

## Backup headers
```bash
sudo cryptsetup luksHeaderBackup /dev/sdX1 --header-backup-file /path/to/backup/luksheader.img
```

## Restoring backup headers
```bash
sudo cryptsetup luksHeaderRestore /dev/sdX1 --header-backup-file /path/to/backup/luksheader.img
```

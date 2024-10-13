
https://askubuntu.com/questions/1250199/move-bootloader-or-remove-efi-partition-in-second-drive

Facing the very same problem with Ubuntu 18.04, I followed PrakashS's answer while making sure the new EFI partition was mounted at /boot/efi before installing grub into it.

I first created a new fat32 partition with GParted on the Ubuntu disk, with the boot flag. (GParted automatically adds the esp flag when checking boot.)

The instructions below use sdb1 for the new EFI parition to match the device name in your question.

    Find the UUID of sdb1:
    sudo blkid | grep /dev/sdb1

    In /etc/fstab, replace the UUID of the /boot/efi entry with that of sdb1:
    sudo nano /etc/fstab

    Ctrl+O then Return to save. Ctrl+X to exit.

    To enact the change, unmount Windows EFI from and mount Ubuntu EFI to /boot/efi:
    sudo umount /boot/efi && sudo mount /boot/efi

    Confirm that it's sdb1 that is mounted at /boot/efi:
    lsblk | grep /boot/efi

    Install grub on sdb (without part number):
    sudo grub-install /dev/sdb

    Generate initramfs image:
    sudo update-initramfs -u -k all

    Generate grub2 config file:
    sudo update-grub

    Reboot.

    Confirm that it's still sdb1 that is mounted at /boot/efi:
    lsblk | grep /boot/efi


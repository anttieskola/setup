# Mounting crypted storage at bootup

Need cryptsetup and installing this creates template `/etc/crypttab`.
```bash
sudo apt-get install cryptsetup
```

In `/etc/fstab` we have to define the devices to mount, where to mount and options.
Using UUID is nice as they same the same even if you change disks in the machine
(on my own machines the disk dev changes). You can use gnome-disk-utility to create
these or do it manually.

`fstab`
```
# something is broke, might have worked better to just use UUID= instead device
# for some reason to by-uuid values seemed to change? (Thought UUID won't change if partition table is not modified...)
# storage drives (encrypted)
/dev/disk/by-uuid/dd75e247-023a-40ce-a5a0-e17908592e67 /mnt/files auto nosuid,nodev,nofail,x-gvfs-show,x-gvfs-name=files 0 0
/dev/disk/by-uuid/b0348931-ed28-42ad-ab16-f08fcc1ae64a /mnt/media auto nosuid,nodev,nofail,x-gvfs-show,x-gvfs-name=media 0 0
```

Then in the crypttab you can define the devices, their key and options. It is possible to add
password here but as most of my drives are unencrypted I want to specifically ask the password
when system is booted.

I think there will be an issue when I change drives as crypttab wants the device name and that can change depending on the HW :(

1. Is the device name (target)
2. Disks UUID (source)
3. Password, none means it will ask it in boot (keyfile)
4. luks is the encryption method (options)

/etc/crypttab
```
# something is broke here aswelll..
#[name] [source device]                        [key]  [options]
# storage drives (encrypted) - ask password on boot
media UUID=6837418d-ca9a-4cca-9dfe-59f963040242 none luks
files UUID=0951f644-aa6a-4754-8597-accc35d13388 none luks
```

# blkid dump
```
/dev/sdd1: LABEL="home" UUID="399455a9-e9bf-433a-a8b1-0d74a79af31a" BLOCK_SIZE="4096" TYPE="ext4" PARTLABEL="home" PARTUUID="60a3e4f1-90a6-4bff-8f0d-da96c36b70d0"
/dev/sda: UUID="0951f644-aa6a-4754-8597-accc35d13388" TYPE="crypto_LUKS"
/dev/sdc1: UUID="D356-0874" BLOCK_SIZE="512" TYPE="vfat" PARTLABEL="efi" PARTUUID="a4afc230-2f99-42d1-b75a-caabd5692057"
/dev/sdc2: LABEL="boot" UUID="a6dee682-1ead-46b3-9250-53b5c2256932" BLOCK_SIZE="1024" TYPE="ext2" PARTLABEL="boot" PARTUUID="be6a4724-9fe7-4ccd-8e71-b540d135aabf"
/dev/sdc3: UUID="b52099e3-36be-4a09-b0d6-7a6f4c326272" TYPE="swap" PARTLABEL="swap" PARTUUID="5398b61a-2e5d-49b5-b6e4-897c953892db"
/dev/sdc4: LABEL="root" UUID="151b6da8-3eb8-4fe4-8aa6-edab0a93fa69" BLOCK_SIZE="4096" TYPE="ext4" PARTLABEL="root" PARTUUID="a4d7e0ef-951a-44fe-9f67-fa5fdd9c1459"
/dev/sdc5: LABEL="var" UUID="bea0a1c3-9e01-4719-915b-acf54cf7ef9a" BLOCK_SIZE="4096" TYPE="ext4" PARTLABEL="var" PARTUUID="a8b388fa-d9f2-4c76-b66d-1ebc7a3503bf"
/dev/sdb: UUID="6837418d-ca9a-4cca-9dfe-59f963040242" TYPE="crypto_LUKS"
```

## Some try hard action goes to horror story
One time this setup (atleast close to it) above worked. After first boot it asked
passwords on bootup to opened drives and they got mounted correctly aswell.

Then I did second bootup and It did not work, was getting tired and also fustrated.
So I went thru some examples and notes I searched from the internet. Make new
configuration of fstab and crypttab.

After booting the new configuration there was bad error that caused the bootup to halt.
I had root account disable on the system, so had to use LiveCD (usb-stick) to load it
up to fix the erros.

Had not have live usb on hand so jumped on other machine, load image and started writing
into my usb stick in device /sdd, here I made a BIG TYPO insted /sdd I wrote /sda...

Seconds later I panic and kill everything. Thinking that well If it was in use/mounted
It would not write anything on device. Well unlucky device was old spinning harddisk
I was about to check if theres anything important (from 10 years ago). Ofcourse the
device was not mounted or in use anyway. Took harddisk to yeat another host and checked
whats left, well the new partition table from image was writen to it so its game over.

Lucky I atleast briefly looked the content week ago and saw some my old games and got
some fond memory flashbacks.

Kinda sad about it, will keep harddisk for a bit but don't think anything can be
done as the old parition table is lost.

# Future
Will at some point read & learn more about crypting with dm-crypt and luks so I know
how to make sure I will not lose data and know how to mount them in anyway I want.
For laptop I wil most likely make a setup where everyhing possible is crypted but
most likely don't care can I modify its installation afterwards, which I really need
on these workstations.

# Sources
- [Ubuntu fstab](https://help.ubuntu.com/community/Fstab)
- [Debian manual crypttab](https://manpages.debian.org/bullseye/cryptsetup/crypttab.5.en.html)
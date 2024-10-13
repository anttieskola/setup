# systemd

- Show messages from previous boot (reversed way)
```bash
journalctl -r -b -1
```

# system logs
- '/var/log/dpkg': here you find what was last installed
- '/var/log/apt/history': last install cmd
- '/var/log/alternatives': history changes made with update-alternatives
- '/var/log/nginx/access': nginx access
- '/var/log/nginx/error': ngingx errors
- '/var/log/phpx.x-fpm.log' php engine
- '/var/log/postgresql/postgresql-xx-main': postgresql logs
- '/var/log/wtmp': logged users (use last command to access)

# memory testing

## in os / running
install and run
```bash
sudo apt install memtester
sudo memtester 1024 5
```

## bootup
install memtest and configure bootup
```bash
sudo apt install memtest86+
sudo update-grub
```

# disk check
```bash
sudo smartctl -a /dev/sdX

# if not installed
sudo apt install smartmontools
```

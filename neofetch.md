# Install
```bash
sudo apt install neofetch
```

# configure to all users
```bash
sudo nano /etc/bash.bashrc
# Add to end (checks terminal interactive)

# neofetch
if [[ $- == *i* ]]; then
    echo
    neofetch
fi
# Save and exit
```

# configure single user
```bash
nano .bash_aliases
# add somewhere (checks terminal interactive)

# neofetch
if [[ $- == *i* ]]; then
    echo
    neofetch
fi
# save and exit
```

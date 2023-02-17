Is not installed on default but just run
```bash
sudo apt-get install git
```

# SSH Keys
Work same way as SSH login keys, we generate a key to be used like for example github. Then add the public key to github. Then add key into use on our local system and it just works.

## Creating

Remember **not to use real email** address with public services. Like github documentation suggest using following format.

```bash
ssh-keygen -t ed25519 -C "anttieskola@users.noreply.github.com"
```

Add your new keys public part to the service you use it for.

## Using
Check ssh agent is running
```bash
ssh-agent -s
```
Add key to agent
```bash
ssh-add ~/.ssh/id_github.pub
```
You can add the command to your ~/.bash_aliases for example to get it set automatically.

## Test
```bash
ssh -T git@github.com
```

If it says permission denied the key is not on the ssh-agent.

When working it responds with message
```
Hi anttieskola! You've successfully authenticated, but GitHub does not provide shell access.
```


# Sources
- [Wikipedia ed25519](https://en.wikipedia.org/wiki/EdDSA)
- [Github](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
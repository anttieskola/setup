# JAVA setup guide
I first used temurin (adoptium) for Java installation, it is open source and free to use.
But will now switch to debian provided openjdk packages for easier maintenance and updates,
as it is provided by the OS package manager.

## Debian OpenJDK
## Installation

```bash
# Note with version 25 sonarqube does not work
sudo apt install openjdk-21-jdk
```

This setups path and JAVA_HOME automatically.

## Adoptium / Temurin

## Purging OS Java
Purged APT packages
'''text
default-jdk/stable,now 2:1.17-74 amd64 [installed]
default-jdk-headless/stable,now 2:1.17-74 amd64 [installed,automatic]
default-jre/stable,now 2:1.17-74 amd64 [installed,automatic]
default-jre-headless/stable,now 2:1.17-74 amd64 [installed,automatic]
openjdk-17-jdk/stable-security,now 17.0.14+7-1~deb12u1 amd64 [installed,automatic]
openjdk-17-jdk-headless/stable-security,now 17.0.14+7-1~deb12u1 amd64 [installed,automatic]
openjdk-17-jre/stable-security,now 17.0.14+7-1~deb12u1 amd64 [installed,automatic]
openjdk-17-jre-headless/stable-security,now 17.0.14+7-1~deb12u1 amd64 [installed,automatic]

```

- Purge

```bash
sudo apt purge default-jdk default-jdk-headless default-jre default-jre-headless openjdk-17-jdk openjdk-17-jdk-headless openjdk-17-jre openjdk-17-jre-headless
# shame on pdftk
# default-jdk* default-jdk-headless* default-jre* default-jre-headless* openjdk-17-jdk*
# openjdk-17-jdk-headless* openjdk-17-jre* openjdk-17-jre-headless* pdftk* pdftk-java
sudo apt autoremove
# bye bye for many packages, not sure will this break something...
```

- Get latest version from [adoptium](https://adoptium.net/)
- Just first extract package to Downloads, this will create name like 'jdk-21.0.6+7'
- Then move the folder as sudo to /usr/local/
- Then create symlink to the folder named /usr/local/java

```bash
# Move and create/update symlink
sudo mv ~/Downloads/jdk-21.0.6+7 /usr/local/
sudo ln -s /usr/local/jdk-21.0.6+7 /usr/local/java
```

- Then modify .bash_aliases

```bash
# Add/modify JAVA_HOME and PATH
export JAVA_HOME=/usr/local/java
export PATH=$PATH:$JAVA_HOME/bin
```

## Java download

1. Get [adoptium](https://adoptium.net/), it is opensource, previously named OpenJDK.

Currently using version

```text
openjdk 21.0.6 2025-01-21 LTS
OpenJDK Runtime Environment Temurin-21.0.6+7 (build 21.0.6+7-LTS)
OpenJDK 64-Bit Server VM Temurin-21.0.6+7 (build 21.0.6+7-LTS, mixed mode, sharing)
```

### Setup

1. Set JAVA_HOME to the installation directory
2. Set PATH to include JAVA_HOME/bin

```bash
# add into .bash_aliases

# export java home
export JAVA_HOME=/usr/local/java
# export java path to bin
export PATH=$PATH:$JAVA_HOME/bin
```

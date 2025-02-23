# Java download

1. Get [adoptium](https://adoptium.net/), it is opensource, previously named OpenJDK.

Currently using version

```text
openjdk 21.0.6 2025-01-21 LTS
OpenJDK Runtime Environment Temurin-21.0.6+7 (build 21.0.6+7-LTS)
OpenJDK 64-Bit Server VM Temurin-21.0.6+7 (build 21.0.6+7-LTS, mixed mode, sharing)
```

## Setup

1. Set JAVA_HOME to the installation directory
2. Set PATH to include JAVA_HOME/bin

```bash
# add into .bash_aliases

# export java home
export JAVA_HOME=/usr/local/java
# export java path to bin
export PATH=$PATH:$JAVA_HOME/bin
```

# Win

## Software

- 7-Zip
- dotnet sdk
- Git
- Visual studio community
  - Desktop development with C++
  - Invidual packages what we need atm
- Node.js
- Rustup
- VS Code

## Environment variables

- `DOTNET_CLI_TELEMETRY_OPTOUT=1`
- `DOTNET_ROOT=Z:\dotnet\`
- `DOTNET_USE_POLLING_FILE_WATCHER=1`
- `SONAR_HOST=http://ares:9000`
- `SONAR_TOKEN=your-sonar-token`

Setup path to contain cli tools and onedrive bin.

## DevDrive

- z:\
- Min 50GB

### Moving caches to DevDrive using symbolic links

```cmd
mklink /D %USERPROFILE%\.cargo z:\caches\cargo
mklink /D %USERPROFILE%\.dotnet z:\caches\dotnet
mklink /D %USERPROFILE%\.nuget z:\caches\nuget
mklink /D %USERPROFILE%\.rustup z:\caches\rustup
mklink /D %USERPROFILE%\.sonarlint z:\caches\sonarlint
mklink /D %USERPROFILE%\.vscode z:\caches\vscode
```

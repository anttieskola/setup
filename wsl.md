# WSL Configuration

- **Systemd Enabled:** Ensures that systemd is used as the init system.
- **Interop Disabled:** Disables interoperability with Windows.
- **Append Windows Path:** Prevents Windows paths from being appended to the WSL environment.

```conf
[boot]
systemd=true

[interop]
enabled = false
appendWindowsPath = false
```

# Lab 9: Package Management in Unix Systems

## 1. What is Package Management?
Package management is a system for installing, updating, configuring, and removing software. A package is a compressed archive containing software binaries, libraries, configuration files, and metadata.

### Key Benefits:
- **Dependency Resolution**: Automatically installs required libraries and components.
- **Centralized Control**: Safe updates and removal through official repositories.
- **Version Control**: Ensures smooth management of software versions.

## 2. Package Management Systems
| Distribution | Package Manager | Format |
|--------------|-----------------|--------|
| Ubuntu/Debian| APT (Advanced Package Tool) | .deb |
| RedHat/CentOS| YUM/DNF | .rpm |
| Arch Linux   | Pacman | .tar.xz |
| macOS        | Homebrew / MacPorts | - |

## 3. Practical Task: Managing 'nginx' package
During this lab, I performed the following operations with the 'nginx' package as required:

### Steps taken:
1. **Update Database**: Synchronized package index with repositories.
   ```bash
   sudo apt update
   ```
2. **Search**: Located the package in the repository.
   ```bash
   apt search nginx
   ```
3. **Dependencies**: Checked what other packages nginx requires to function.
   ```bash
   apt-cache depends nginx
   ```
4. **Installation**: Downloaded and installed the package.
   ```bash
   sudo apt install nginx
   ```
5. **Removal**: Completely removed the package including configuration files using purge.
   ```bash
   sudo apt purge nginx
   ```

## 4. Common APT Commands Reference
| Command | Description |
|---------|-------------|
| `apt update` | Refresh package list from repositories |
| `apt upgrade` | Upgrade all installed packages |
| `apt install` | Install a specific software package |
| `apt remove` | Uninstall package (keep config files) |
| `apt purge` | Uninstall package and delete config files |

## 5. Important Locations
- **/etc/apt/sources.list**: Main repository sources file.

---
**Performed by:** Kaiyrkul

# Lab 9: Package Management in Unix Systems

## 1. What is Package Management?
[cite_start]Package management is a system for installing, updating, configuring, and removing software[cite: 77, 113]. [cite_start]A package is a compressed archive containing software binaries, libraries, configuration files, and metadata[cite: 76, 79, 83].

### Key Benefits:
- [cite_start]**Dependency Resolution**: Automatically installs required libraries and components[cite: 78, 91, 129].
- [cite_start]**Centralized Control**: Safe updates and removal through official repositories[cite: 90, 114].
- [cite_start]**Version Control**: Ensures smooth management of software versions[cite: 78].

## 2. Package Management Systems
| Distribution | Package Manager | Format |
|--------------|-----------------|--------|
| Ubuntu/Debian| APT (Advanced Package Tool) | [cite_start].deb [cite: 85, 89] |
| RedHat/CentOS| YUM/DNF | [cite_start].rpm [cite: 86] |
| Arch Linux   | Pacman | .tar.xz |
| macOS        | Homebrew / MacPorts | - |

## 3. Practical Task: Managing 'nginx' package
[cite_start]During this lab, I performed the following operations with the 'nginx' package as required[cite: 143]:

### Steps taken:
1. [cite_start]**Update Database**: Synchronized package index with repositories[cite: 94, 101, 116].
   ```bash
   sudo apt update
   ```
2. [cite_start]**Search**: Located the package in the repository[cite: 97, 138].
   ```bash
   apt search nginx
   ```
3. [cite_start]**Dependencies**: Checked what other packages nginx requires to function[cite: 141, 142].
   ```bash
   apt-cache depends nginx
   ```
4. [cite_start]**Installation**: Downloaded and installed the package[cite: 93, 103, 126].
   ```bash
   sudo apt install nginx
   ```
5. [cite_start]**Removal**: Completely removed the package including configuration files using purge[cite: 135, 136].
   ```bash
   sudo apt purge nginx
   ```

## 4. Common APT Commands Reference
| Command | Description |
|---------|-------------|
| `apt update` | [cite_start]Refresh package list from repositories [cite: 94, 116] |
| `apt upgrade` | [cite_start]Upgrade all installed packages [cite: 95, 121] |
| `apt install` | [cite_start]Install a specific software package [cite: 93, 126] |
| `apt remove` | [cite_start]Uninstall package (keep config files) [cite: 96, 131] |
| `apt purge` | [cite_start]Uninstall package and delete config files [cite: 135, 136] |

## 5. Important Locations
- [cite_start]**/etc/apt/sources.list**: Main repository sources file[cite: 117, 127].

---
**Performed by:** Kaiyrkul

# Lab 11: Installing Packages from Source

## 1. Why Install from Source?
There are several reasons to install software from source:
- **Access to the Latest Version**: Sometimes the latest features or fixes are only available in the source code.
- **Customization**: Allows changing default configuration options or enabling/disabling specific features.
- **Optimization**: Software can be optimized for specific hardware and needs.
- **No Available Packages**: When precompiled packages are not available for your distribution.

## 2. Practical Task: Installing Neofetch from Source
Neofetch is a command-line system information tool written in Bash. It displays a summary of system info like OS, Kernel, Uptime, and CPU with an ASCII logo.

### Steps performed:
1. **Installed Dependencies**: Installed 'git' and 'make' using APT.
2. **Cloned Repository**: Downloaded the source code from GitHub: `git clone https://github.com/dylanaraps/neofetch.git`.
3. **Build and Install**: Used the `make` utility to copy the script to `/usr/local/bin/` for global access.
   ```bash
   sudo make install
   ```
4. **Verification**: Successfully ran `neofetch` to display system information.

---
**Performed by:** Kaiyrkul

# Lab 11: Installing Packages from Source

## 1. Why Install from Source?
[cite_start]There are several reasons to install software from source[cite: 143, 144]:
- [cite_start]**Access to the Latest Version**: Sometimes the latest features or fixes are only available in the source code[cite: 146].
- [cite_start]**Customization**: Allows changing default configuration options or enabling/disabling specific features[cite: 148].
- [cite_start]**Optimization**: Software can be optimized for specific hardware and needs[cite: 149].
- [cite_start]**No Available Packages**: When precompiled packages are not available for your distribution[cite: 150].

## 2. Practical Task: Installing Neofetch from Source
[cite_start]Neofetch is a command-line system information tool written in Bash[cite: 229, 230]. [cite_start]It displays a summary of system info like OS, Kernel, Uptime, and CPU with an ASCII logo[cite: 231, 232, 240, 243].

### Steps performed:
1. [cite_start]**Installed Dependencies**: Installed 'git' and 'make' using APT[cite: 244, 246].
2. [cite_start]**Cloned Repository**: Downloaded the source code from GitHub: `git clone https://github.com/dylanaraps/neofetch.git`[cite: 251, 252].
3. [cite_start]**Build and Install**: Used the `make` utility to copy the script to `/usr/local/bin/` for global access[cite: 258, 259, 260].
   ```bash
   sudo make install
   ```
4. [cite_start]**Verification**: Successfully ran `neofetch` to display system information[cite: 261, 264, 265].

---
**Performed by:** Kaiyrkul

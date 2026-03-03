# Lab 11: Installing Packages from Source

## 1. Why Install from Source?
Installing from source provides several advantages:
- **Latest Version**: Access to features not yet available in precompiled packages.
- **Customization**: Ability to change configuration options during build.
- **Optimization**: Software can be optimized for specific hardware.

## 2. Practical Task: Installing Neofetch
Neofetch is a command-line tool that displays system information with ASCII art.

### Installation Steps:
1. **Dependencies**: Installed 'git' and 'make' using APT.
2. **Cloning**: Downloaded the source code from the official GitHub repository.
3. **Building**: Used the 'make' utility to prepare the script.
4. **Installation**: Executed 'sudo make install' to move the executable to system PATH.

## 3. Verification
Running the command `neofetch` confirms successful installation by displaying OS, Kernel, and CPU information.

---
**Performed by:** Kaiyrkul

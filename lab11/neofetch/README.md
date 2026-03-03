# Lab 11: Installing Packages from Source

## 1. Why Install from Source?
Installing from source provides several advantages[cite: 144, 145]:
- **Latest Version**: Access to features not yet available in precompiled packages[cite: 146].
- **Customization**: Ability to change configuration options during build[cite: 148].
- **Optimization**: Software can be optimized for specific hardware[cite: 149].

## 2. Practical Task: Installing Neofetch
Neofetch is a command-line tool that displays system information with ASCII art.

### Installation Steps:
1. **Dependencies**: Installed 'git' and 'make' using APT[cite: 244, 246].
2. **Cloning**: Downloaded the source code from the official GitHub repository[cite: 251, 252].
3. **Building**: Used the 'make' utility to prepare the script[cite: 255, 257].
4. **Installation**: Executed 'sudo make install' to move the executable to system PATH.

## 3. Verification
Running the command `neofetch` confirms successful installation by displaying OS, Kernel, and CPU information[cite: 261, 265].

---
**Performed by:** Kaiyrkul

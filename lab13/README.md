# Lab 13: Keylogger Implementation

## Objective
The goal is to understand how **Keyloggers** capture user input and how data exfiltration works in a cyberattack lifecycle[cite: 93, 105].

## Components
1. **Keylogger (main.py)**: Uses the `pynput` library to monitor and record keystrokes[cite: 112, 116].
2. **Local Storage (log.txt)**: Stores captured keys locally on the victim's machine[cite: 151, 176].
3. **Data Exfiltration (server.py)**: A simulated API server that receives logged data from the victim's machine[cite: 177].

## Security Task
Modified the base script to include a function that transmits the `log.txt` data to a remote storage server, simulating a real-world data breach[cite: 177].

---
**Status:** Completed

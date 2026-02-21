import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "kanatbekova_ka@auca.kg" # Твоя почта
sender_password = "" # Пароль приложения
receiver_email = "kanatbekovakaiyrkul@gmail.com" # Почта "жертвы"

subject = "Bank Account Update Required"
# Ссылка на локальный файл, как в примере
link = "file:///" + os.path.abspath("index.html")
body = f"Please update your card details: {link}"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()

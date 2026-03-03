import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# 1. Загружаем секреты из файла .env
load_dotenv()

sender_email = os.getenv("EMAIL_USER")
sender_password = os.getenv("EMAIL_PASS")
receiver_email = sender_email  # Отправляем себе для теста

# 2. Создаем структуру письма
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Important: Security Update for Your Bank Account"

# Генерируем путь к index.html
file_path = os.path.abspath("index.html")

body = f"""
<html>
<body>
    <h2 style="color: #0056b3;">Action Required: Verify Your Card</h2>
    <p>Dear Customer, we've detected unusual activity on your account.</p>
    <p>To avoid service interruption, please verify your payment details here:</p>
    <p><a href="file:///{file_path}">Update Payment Information</a></p>
    <br>
    <p>Thank you,<br>Secure Banking Team</p>
</body>
</html>
"""
msg.attach(MIMEText(body, "html"))

# 3. Отправка письма с правильной последовательностью команд
try:
    print("Connecting to Gmail...")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    
    server.ehlo()         # Приветствуем сервер
    server.starttls()     # ВКЛЮЧАЕМ ШИФРОВАНИЕ 
    server.ehlo()         # Повторно приветствуем уже в защищенном режиме
    
    print("Logging in...")
    server.login(sender_email, sender_password)
    
    print("Sending email...")
    server.sendmail(sender_email, receiver_email, msg.as_string())
    
    print("--- SUCCESS: Email sent! ---")

except Exception as e:
    print(f"\n!!! ERROR: {e}")

finally:
    try:
        server.quit()
    except:
        pass
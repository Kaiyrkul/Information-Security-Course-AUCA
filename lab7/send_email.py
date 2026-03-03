import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Get current timestamp for the report
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Configuration (using placeholder data for the report)
sender_email = 'your_login@gmail.com'
receiver_email = 'admin@example.com'
password_of_sender = 'your_app_password'
smtp_server = 'smtp.gmail.com'
smtp_port = 465

# Create the email message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = f'Automated System Report: {now}'

# Email body content
body_content = f'''
Lab 7 Report: Crontab Automation.
Status: System is running normally.
Execution time via Crontab: {now}
Student: Kaiyrkul
'''

message.attach(MIMEText(body_content, 'plain', "utf-8"))

# Execution logic
try:
    # In a real environment, connection happens here:
    # with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
    #     server.login(sender_email, password_of_sender)
    #     server.send_message(message)
    
    print(f"Email generated successfully at {now}")
    
    # Writing to log file (as required by Lab 7 base task)
    with open("/home/kaiyrkul/email_log.txt", "a") as f:
        f.write(f"Python script executed at {now}\n")
except Exception as e:
    print(f"Error occurred: {e}")

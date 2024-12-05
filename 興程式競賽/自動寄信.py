import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Gmail 設置
sender_email = "noron12334@gmail.com"  # 您的 Gmail 地址
app_password = "ubyz ucjp jdas unjz"      # 您的應用程式專用密碼

def send_email(receiver_email, subject, message):
    # 建立郵件內容
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # 加入郵件內容
    msg.attach(MIMEText(message, 'plain'))

    try:
        # 連線到 Gmail 的 SMTP 伺服器
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, app_password)

        # 發送郵件
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("郵件已成功發送到", receiver_email)

    except Exception as e:
        print("發送失敗：", e)

    finally:
        # 關閉伺服器
        server.quit()

# 測試發送
receiver_email = "noron23@yahoo.com.tw"   # 接收者的電子郵件地址
subject = "包裹通知"
message = "這你的包裹已經收到。"

send_email(receiver_email, subject, message)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox

# Gmail 設置
sender_email = "noron12334@gmail.com"  # 您的 Gmail 地址
app_password = "ubyz ucjp jdas unjz"     # 您的應用程式專用密碼

def send_email():
    # 從介面中取得收件者、主題和內容
    receiver_email = receiver_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)

    # 建立郵件內容
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        # 連接到 Gmail 的 SMTP 伺服器並發送郵件
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        
        # 顯示成功訊息
        messagebox.showinfo("成功", "郵件已成功發送到 " + receiver_email)

    except Exception as e:
        # 顯示錯誤訊息
        messagebox.showerror("發送失敗", f"郵件發送失敗：{e}")

# 建立 Tkinter 視窗
root = tk.Tk()
root.title("自動寄信系統")

# 收件人 Email 輸入框
tk.Label(root, text="收件人 Email:").grid(row=0, column=0, padx=10, pady=10)
receiver_entry = tk.Entry(root, width=30)
receiver_entry.grid(row=0, column=1, padx=10, pady=10)

# 主題輸入框
tk.Label(root, text="主題:").grid(row=1, column=0, padx=10, pady=10)
subject_entry = tk.Entry(root, width=30)
subject_entry.grid(row=1, column=1, padx=10, pady=10)

# 信件內容輸入框
tk.Label(root, text="信件內容:").grid(row=2, column=0, padx=10, pady=10)
message_text = tk.Text(root, height=10, width=30)
message_text.grid(row=2, column=1, padx=10, pady=10)

# 發送按鈕
send_button = tk.Button(root, text="發送", command=send_email)
send_button.grid(row=3, column=1, pady=20)

# 啟動 Tkinter 介面
root.mainloop()

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox, Toplevel, Label, Button, Entry
import sqlite3
from tkinter import ttk

# Gmail 設置
sender_email = "noron12334@gmail.com"  # 您的 Gmail 地址
app_password = "dcnt amqh xmsm lybg"        # 您的應用程式專用密碼

# 資料庫操作函數
def get_all_residents(search_name=""):
    conn = sqlite3.connect('residents.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, room_number, email FROM residents ORDER BY (name = ?) DESC, name', (search_name,))
    result = cursor.fetchall()
    conn.close()
    return result

def add_resident(name, room_number, email):
    conn = sqlite3.connect('residents.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO residents (name, room_number, email) VALUES (?, ?, ?)', (name, room_number, email))
    conn.commit()
    conn.close()
    messagebox.showinfo("成功", "成功新增住戶資料")

def update_resident(name, room_number, email):
    conn = sqlite3.connect('residents.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE residents SET room_number = ?, email = ? WHERE name = ?', (room_number, email, name))
    conn.commit()
    conn.close()
    messagebox.showinfo("成功", "成功更新住戶資料")

# 寄送郵件函數
def send_email(receiver_email):
    subject = "包裹到達通知"
    message = "您的包裹已經到達"
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        messagebox.showinfo("成功", "郵件已成功發送到 " + receiver_email)
    except Exception as e:
        messagebox.showerror("發送失敗", f"郵件發送失敗：{e}")

# 查詢並顯示住戶資料
def handle_check():
    name = name_entry.get()
    residents = get_all_residents(name)

    if residents:
        show_confirmation(residents)
    else:
        messagebox.showerror("錯誤", "找不到該住戶的資料")

# 顯示住戶確認視窗
def show_confirmation(residents):
    confirm_window = Toplevel(root)
    confirm_window.title("確認住戶資料")

    columns = ('name', 'room_number', 'email')
    tree = ttk.Treeview(confirm_window, columns=columns, show='headings')
    tree.heading('name', text='姓名')
    tree.heading('room_number', text='房號')
    tree.heading('email', text='電子郵件')
    tree.grid(row=0, column=0, columnspan=3)

    for resident in residents:
        tree.insert('', tk.END, values=resident)

    selected_resident = residents[0]

    send_button = Button(confirm_window, text="發送", command=lambda: confirm_and_send(confirm_window, selected_resident[2]))
    send_button.grid(row=1, column=0, pady=10)
    update_button = Button(confirm_window, text="更新", command=lambda: show_update_window(selected_resident))
    update_button.grid(row=1, column=1, pady=10)
    cancel_button = Button(confirm_window, text="取消", command=confirm_window.destroy)
    cancel_button.grid(row=1, column=2, pady=10)

# 更新住戶資料視窗
def show_update_window(resident):
    update_window = Toplevel(root)
    update_window.title("更新住戶資料")

    Label(update_window, text="姓名:").grid(row=0, column=0)
    Label(update_window, text="房號:").grid(row=1, column=0)
    Label(update_window, text="電子郵件:").grid(row=2, column=0)

    name_entry = Entry(update_window, width=30)
    name_entry.grid(row=0, column=1)
    name_entry.insert(0, resident[0])

    room_entry = Entry(update_window, width=30)
    room_entry.grid(row=1, column=1)
    room_entry.insert(0, resident[1])

    email_entry = Entry(update_window, width=30)
    email_entry.grid(row=2, column=1)
    email_entry.insert(0, resident[2])

    update_button = Button(update_window, text="儲存", command=lambda: save_update(update_window, name_entry.get(), room_entry.get(), email_entry.get()))
    update_button.grid(row=3, column=0, columnspan=2, pady=10)

def save_update(window, name, room_number, email):
    update_resident(name, room_number, email)
    window.destroy()

# 新增住戶資料視窗
def show_add_window():
    add_window = Toplevel(root)
    add_window.title("新增住戶資料")

    Label(add_window, text="姓名:").grid(row=0, column=0)
    Label(add_window, text="房號:").grid(row=1, column=0)
    Label(add_window, text="電子郵件:").grid(row=2, column=0)

    name_entry = Entry(add_window, width=30)
    name_entry.grid(row=0, column=1)

    room_entry = Entry(add_window, width=30)
    room_entry.grid(row=1, column=1)

    email_entry = Entry(add_window, width=30)
    email_entry.grid(row=2, column=1)

    add_button = Button(add_window, text="新增", command=lambda: save_add(add_window, name_entry.get(), room_entry.get(), email_entry.get()))
    add_button.grid(row=3, column=0, columnspan=2, pady=10)

def save_add(window, name, room_number, email):
    add_resident(name, room_number, email)
    window.destroy()

# 寄送郵件並關閉視窗
def confirm_and_send(window, email):
    send_email(email)
    window.destroy()

# 建立 Tkinter 主視窗
root = tk.Tk()
root.title("包裹通知系統")

Label(root, text="住戶姓名:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=10)

check_button = tk.Button(root, text="查詢", command=handle_check)
check_button.grid(row=1, column=0, pady=20)

add_button = tk.Button(root, text="新增住戶", command=show_add_window)
add_button.grid(row=1, column=1, pady=20)

root.mainloop()

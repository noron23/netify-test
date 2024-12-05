import sqlite3

# 連接到資料庫（如果不存在，則創建它）
conn = sqlite3.connect('residents.db')
cursor = conn.cursor()

# 創建住戶資料表
cursor.execute('''
CREATE TABLE IF NOT EXISTS residents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    room_number TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# 插入範例住戶資料
residents_data = [
    ('林均融', '202', 'noron23@yahoo.com.tw'),
    ('右膝', '101', 'noron23@yahoo.com.tw'),
    ('溫子威', '303', 'maweidaweedkiller@gmail.com')
]

cursor.executemany('INSERT INTO residents (name, room_number, email) VALUES (?, ?, ?)', residents_data)
conn.commit()
conn.close()
print("資料庫建立完成並插入了範例數據")

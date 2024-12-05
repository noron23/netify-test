import requests

# 1. 設定 API URL
url = "https://zenquotes.io/api/random"

# 2. 發送 GET 請求
response = requests.get(url)

# 3. 確認請求成功 (狀態碼 200 表示成功)
if response.status_code == 200:
    data = response.json()  # 將回應數據轉換成 JSON 格式
    quote = data[0]["q"]    # 名言內容
    author = data[0]["a"]   # 作者
    print(f"{quote} - {author}")
else:
    print("無法獲取名言，請求失敗！")

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# 目標網站 URL
url = 'https://www.chinatimes.com/'

# 設置請求頭部，模擬瀏覽器請求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 重試次數
retry_count = 0
max_retries = 3

while retry_count < max_retries:
    # 發送請求並獲取網頁內容
    response = requests.get(url, headers=headers)

    # 如果遇到 403，提示並進行重試
    if response.status_code == 403:
        print(f"遇到 403 錯誤，正在重試... (重試次數：{retry_count + 1})")
        
        # 檢查用戶是否輸入 q 停止
        user_input = input("如果要停止爬蟲，請輸入 'q' 並按 Enter：")
        if user_input.lower() == 'q':
            print("爬蟲已停止。")
            break
        
        # 等待一些時間再重試
        time.sleep(5)
        retry_count += 1
    else:
        # 請求成功後解析 HTML 內容
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 找到所有包含新聞標題的 <a> 標籤，並且 class 屬性為 'title'
            titles = soup.find_all('a', class_='title')
            
            # 提取標題文字並存儲到列表中
            titles_list = [title.get_text(strip=True) for title in titles]
            
            # 將標題儲存為 CSV 文件
            df = pd.DataFrame(titles_list, columns=['News Title'])
            df.to_csv('chinatimes_news_titles.csv', index=False)
            print("新聞標題已成功儲存到 'chinatimes_news_titles.csv' 文件中。")
        break

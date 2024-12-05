import pandas as pd
import os
os.chdir("c:/Users/user/Desktop/林均融/程式/程式設計 week11 機器學習")

# 讀取 test.csv 檔案
test_data = pd.read_csv('test.csv')

# 查看 Name 這一列
print("Age 欄位的內容：")
print(test_data['Age'])

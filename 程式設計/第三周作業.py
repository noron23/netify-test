dic = {"科學書籍":{"愛因斯坦傳","馬斯克傳"}, "個人成長":{"原子習慣", "執行長日記", "拆掉思維裡的牆"}}
book_status = [("愛因斯坦傳", True), ("馬斯克傳", False), ("原子習慣", True), ("執行長日記", False), ("拆掉思維裡的牆", True)]


#把book_status轉成dic才能查詢
status_dic = {book : status for book, status in book_status}
for category, books in dic.items():
    print(f"分類：{category}")
    print('-'*30)
    
    for book in books:
        status_str = "可借閱" if status_dic[book] else "不可借閱"
        print(f"書名:{book:<20} 狀態:{status_str:<10}")
    
    print('-'*30)
    print("hello")
    
    
            
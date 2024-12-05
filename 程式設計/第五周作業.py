class Book:
    #定義類別的初始資訊 
    def __init__(self, book_id, name, author, price, available):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.price = price
        self.available = available

    #這邊就展示書籍的資訊
    def display_info(self):
        print(f"書籍編號：{self.book_id}")
        print(f"書名：{self.name}")
        print(f"作者：{self.author}")
        print(f"價格：{self.price}")
        print(f"狀態：{'可借' if self.available == 'True' else '不可借'}")


def load_books(filename):
    books = {}
    #利用try except偵測
    #為了要尋找書籍必須能偵測，所以把書籍資訊存到串列裡面，之後尋找再回復
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            next(f)  # 跳過標題行
            for line in f:
                data = line.strip().split(',')
                if len(data) == 5:
                    book_id, name, author, price, available = data
                    books[book_id] = Book(book_id, name, author, price, available)
    except FileNotFoundError:
        print(f"錯誤：檔案 {filename} 不存在")
    return books


def find_book(books):
    book_id = input("請輸入書籍編號：")
    if book_id in books:
        books[book_id].display_info()
    else:
        print(f"錯誤：書籍編號 {book_id} 不存在")


def main():
    #books是紀錄書籍的陣列，會經過運算後回傳，為了能尋找
    books = load_books("books.txt")
    while True:
        print("1. 查找書籍")
        print("2. 離開")
        choice = input("選擇操作：")
        if choice == '1':
            find_book(books)
        elif choice == '2':
            print("再見！")
            break
        else:
            print("無效的選擇，請重新選擇")


if __name__ == "__main__":
    main()

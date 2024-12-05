import datetime
import random
#引入模組
#以下就是不同類別的初始化以及封裝，還有格式化輸出
class Book():
    def __init__(self, title, author, year, genre):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__genre = genre
    
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_year(self):
        return self.__year
    
    def get_genre(self):
        return self.__genre
    
    def get_info(self):        
        print(f"書名:{self.get_title()}, 作者:{self.get_author()}, 出版年份：{self.get_year()}, 類型:{self.get_genre()}")
       
class Novel(Book):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year, genre)
    
    def get_info(self):
        print(f"小說 - 書名:{self.get_title()}, 作者:{self.get_author()}, 出版年份：{self.get_year()}, 類型:{self.get_genre()}")

class ScienceBook(Book):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year, genre)
    
    def get_info(self):
        print(f"科學書籍 - 書名:{self.get_title()}, 作者:{self.get_author()}, 出版年份：{self.get_year()}, 類型:{self.get_genre()}")
  
class Borrower():
    #記得用列表船入類別的話，不用再()裡面有東西
    def __init__(self, name):
        self.__name = name
        self.borrowed_books = []
        
    def get_name(self):
        return self.__name
    
    def add_books(self, book):
        self.borrowed_books.append(book)
    
    #時間的用法記起來
    def get_borrowed_books_reports(self):
        print(f"借閱者: {self.get_name()} 的借書列表:")
        print(f"當前時間:{datetime.date.today()}")
        for i in self.borrowed_books:
            i.get_info()
    #選擇隨機一本書 記得回船的東西因為是類別所以是地址 後面要接上方法
    def get_random_book(self):
        print("隨機選擇的一本書是:")
        random.choice(self.borrowed_books).get_info()

#以下是主要程式 先把物件指定類別 之後就把第一位讀者命名出來測試各種功能
    
book1 = Novel("追風的孩子", "你爸爸", 2005, "小說")
book2 = ScienceBook("大自然好好玩", "地理大世界是我", 2005, "科學書籍")

p1 = Borrower("小明")
p1.add_books(book1)
p1.add_books(book2)
p1.get_borrowed_books_reports()
p1.get_random_book()
    
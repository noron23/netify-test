def check_inventory():
    try:
        f = open("inventory.txt", mode='r', encoding = 'utf-8')
        content = f.read()
        if content == '':
            print("目前庫存沒有東西")
        else:
            print(content)
    
    except FileNotFoundError:
        print("檔案不存在，將自動建立新檔案")
        f = open("inventory.txt", mode='w', encoding = 'utf-8')
    
def add_inventory():
    f = open("inventory.txt", mode='a', encoding = 'utf-8')
    item = input("請選擇要輸入的商品\n")
    try:
        num = int(input("請輸入商品的數量\n"))
        f.write(f"{item}, {num} \n")
    except ValueError:
        print("請輸入有效的數字")
    

def update_inventory():
    #偵測找出物品 輸入
    f = open("inventory.txt", mode='r', encoding = 'utf-8')
    item_array = []
    
    for line in f:
        item, num = line.strip().split(",")
        item_array.append([item, num])
    
    new_item = input("請輸入你要修改的商品\n")
    new_num = input("請輸入修改的數量\n")
    
    updated = False
    
    for i in range(len(item_array)):
        if new_item == item_array[i][0]:
            item_array[i][1] = new_num
            updated = True
            print("修改成功")
            
    if not updated:
        print("未找到商品，請重新執行整個功能")
    
    #找到東西改好陣列 要寫回
    f = open("inventory.txt", mode='w', encoding = 'utf-8')     
    for item, num in item_array:
        f.write(f"{item}, {num}\n")
    

while True:
    print("操作選單如下：")
    choice = input('''1. 查看庫存
2. 新增商品
3. 更新商品數量
4. 離開
''')

    if choice == '1':
        check_inventory()
    elif choice == '2':
        add_inventory()
    elif choice == '3':
        update_inventory()
    elif choice == '4':
        print("掰掰")
        raise SystemExit
    else:
        print("無效的選擇，請重新輸入")
else:
    pass
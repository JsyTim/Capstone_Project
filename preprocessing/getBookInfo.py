import requests, json, random, csv
path = "C:/Users/TIM58/Documents/GitHub/Capstone_Project/isbn.csv"


def getBookInfo(barcode):
    url = 'https://douban.uieee.com/v2/book/isbn/' + str(barcode)
    r = requests.get(url)
    res = json.loads(r.text)
    if res is None:
        return "无法获取图书详情信息"
    return res


def getbooklist():
    with open(path, 'r', encoding='UTF-8') as reader:
        csv_reader = csv.reader(reader)
        bookList = []
        for row in csv_reader:
            bookList.append(row[0].replace(' ', ''))
        print(bookList)


getbooklist()
bookList = ['9788781074519', '9787536021440', '9787530208694', '9787530209981', '9787530208656', '9787530209042', '9787530208632', '9787563397648', '9787563397631', '9787563397655', '9787549509140', '9787020066919', '9787500652045', '9787561334386', '9787561335017', '9787561334409', '9787561334409', '9787561337561', '9787020024759', '9787205047702', '9787101007473', '9787020028115', '9787530209226', '9787020036509', '9787539924564', '9787536692930', '9787536693968', '9787229030933', '9787536455382', '9787535458667', '9787542729040', '9789573305545', '9787806399071', '9787806399057', '9787530208960', '9787530208915', '9787530208960', '9787806399095', '9787806399682', '9787805676258', '9787506261579', '9787020027606', '9787020040179', '9787501600069', '9787020032044', '9787020017164', '9787532741793', '9787532712243', '9787532739981', '9787532718214', '9787532710942', '9787806574317', '9787500609049', '9787806574676', '9787540213152', '9787530467558', '9787530474396', '9787530455234', '9787530459928', '9787532378784', '9787532378746', '9787108011114', '9787030107596', '9787309044546', '9787532361724']
# booklist=[9787500438847, 9787563332854, 9787807600558, 9787111188469, 9787121019333, 9787111165170, 9787530467558, 9787530474396, 9787540471309]

def getSql():
    for i in range(len(bookList)):
        res = getBookInfo(bookList[i])
        insert = "INSERT INTO `book` (`cat_id`, `book_isbn13`, `book_title`, `book_author`, `book_price`, `book_oprice`, `book_main_image`, `book_grade`, `book_press`, `book_binding`, `book_desc`, `book_degrees`, `book_stock`, `tags`, `book_status`) VALUES"
        cat_id = str(1)
        book_isbn13 = res['isbn13']
        book_title = res['title']
        book_author = str(res['author'][0])
        book_price = (res['price'].replace('元', ''))
        book_oprice = res['price'].replace('元', '')
        book_main_image = res['image']
        book_grade = res['rating']['average']
        book_press = res['publisher']
        book_binding = res['binding']
        book_desc = res['summary'].replace("\n", ' ')
        book_degrees = str(random.randint(1, 10))
        book_stock = str(random.randint(3, 50))
        tags = res['tags'][0]['name']
        book_status = str(1)
        sql = insert + '( "'+str(cat_id)+'","'+book_isbn13+'","'+book_title+'","'+book_author+'", "'+book_price+'" , "'+book_oprice+'" ,"'+book_main_image+'", "'+book_grade+'","'+book_press+'","'+book_binding+'","'+book_desc+'","'+book_degrees+'","'+book_stock+'", "'+tags+'","'+book_status+'")'
        print(sql)
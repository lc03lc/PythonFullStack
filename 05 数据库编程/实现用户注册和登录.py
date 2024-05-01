import pymysql


def register():
    print("用户注册")
    name = input("请输入用户名: ")
    psd = input("请输入密码: ")

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', charset='utf8', db='test')
    cursor = conn.cursor()

    sql = 'insert into tb(name, psd) values ("{}", "{}")'.format(name, psd)
    cursor.execute(sql)
    conn.commit()

    cursor.close()
    conn.close()

    print("注册成功")


def login():
    print("用户登录")
    name = input("请输入用户名: ")
    psd = input("请输入密码: ")

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', charset='utf8', db='test')
    cursor = conn.cursor()

    # sql = 'select name,psd from tb where name="{}" and psd="{}"'.format(name, psd)
    # cursor.execute(sql)
    # 避免SQL注入
    cursor.execute("select * from tb where name=%s and psd=%s", [name, psd])
    result = cursor.fetchone()

    if result:
        print("登录成功")
    else:
        print("用户名或密码错误")

    cursor.close()
    conn.close()


while True:
    msg = input("R, L, Q ?\n")
    if msg.upper() == 'Q':
        break
    if msg.upper() == 'R':
        register()
        continue
    if msg.upper() == 'L':
        login()
        continue
    print('again')

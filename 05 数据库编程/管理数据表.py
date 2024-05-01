import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', charset='utf8')
cursor = conn.cursor()

# 1. 查看数据表
cursor.execute('use test')
cursor.execute('show tables')
result = cursor.fetchall()
print(result)

# 2. 创建表
sql = '''
create table tb2(
    id int not null primary key auto_increment,
    title varchar(128),
    content text,
    ctime datetime
)default charset=utf8;
'''
cursor.execute(sql)
conn.commit()

# 关闭连接
cursor.close()
conn.close()
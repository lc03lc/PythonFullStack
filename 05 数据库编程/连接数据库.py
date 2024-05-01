import pymysql

# 连接MySQL
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', charset='utf8')
cursor = conn.cursor()

# 1.查看数据库
# 发送指令
cursor.execute('show databases')
result = cursor.fetchall()
print(result)  # (('information_schema',), ('mysql',), ('performance_schema',), ('sys',), ('test',))

# 2.创建数据库
cursor.execute('create database db3 default charset utf8 collate utf8_general_ci')
conn.commit()

# 3.删除数据库
cursor.execute('drop database db3')
conn.commit()

# 4.进入数据库，查看表
cursor.execute('use test')
cursor.execute('show tables')
result = cursor.fetchall()
print(result)

# 关闭连接
cursor.close()
conn.close()
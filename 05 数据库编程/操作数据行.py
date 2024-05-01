import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', charset='utf8', db='test')
cursor = conn.cursor()

# 1. 新增
cursor.execute("insert into tb(name, age) values ('qq', 21)")
conn.commit()

# 2. 删除
cursor.execute("delete from tb where name='qq'")
conn.commit()

# 3. 修改
cursor.execute("update tb set age='22' where name='zl'")
conn.commit()

# 查看数据表
cursor.execute("select * from tb")
result = cursor.fetchall()
print(result)

cursor.close()
conn.close()

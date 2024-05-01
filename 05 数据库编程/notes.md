# MySQL操作

#### 库操作

```sql
# 创建数据库
create database db3 default charset utf8 collate utf8_general_ci;
# 删除数据库
drop database db3;
```



#### 创建表

```sql
create table tb(
	id int primary key,				-- 主键（不允许为空、元素不能重复）
    name varchar(16) not null, 		-- 不允许为空
    email varchar(32) null,			-- 允许为空（默认）
    age int default 18				-- 默认值为3
)default charset=utf8;
```

主键一般用于表示当前这条数据的编号（类似于身份证），比较繁琐，需要自己来维护。所以，数据库一般会将主键和自增结合

```sql
create table tb(
	id int auto_increment primary key,	-- 主键（不允许为空、元素不能重复）& 自增
    name varchar(16) not null, 			-- 不允许为空
    email varchar(32) null,				-- 允许为空（默认）
    age int default 18					-- 默认值为3
)default charset=utf8;
```

**注意**：一个表中只能有一个自增列

#### 修改表

- 删除表  `drop table 表名;`

- 清空表 `delete from 表名` `truncate table 表名` (速度快但是无法恢复)

- 修改表

  - 添加列

    ```sql
    alter table 表名 add 列名 类型;
    alter table 表名 add 列名 类型 DEFAULT 默认值;
    alter table 表名 add 列名 类型 not null default 默认值;
    alter table 表名 add 列名 类型 not null primary key auto_increment
    ```

  - 删除列

    ```sql
    alter table 表名 drop column 列名;
    ```

  - 修改列 类型+名称

    ```sql
    alter table 表名 change 原列名 新列名 新类型; -- 新列名可以与原列名相同
    alter table tb change id id int not null;
    ```

  - 修改列 仅类型

    ```sql
    alter table 表名 modify 列名 类型;
    ```

  - 修改列 仅默认值

    ```sql
    alter table 表名 alter 列名 set default 1000;
    ```

  - 删除列 默认值

    ```sql
    alter table 表名 alter 列名 drop default;
    ```

  - 添加主键

    ```sql
    alter table 表名 add primary key(列名);
    ```

  - 删除主键

    ```sql
    alter table 表名 drop primary key;
    ```

#### 内置客户端操作

- 新增数据

  ```sql
  insert into 表名 (列名,) values (对应值,);
  
  insert into tb1 (name, psd) values ('zs', 18), ('ls', 19);
  insert into tb1 values ('zs', 18), ('ls', 19);					-- 如果只有两列
  ```

- 删除数据

  ```sql
  delete from 表名;									-- 清空表
  delete from 表名 where 条件;
  
  delete from tb1;
  delete from tb1 where name='zs';
  delete from tb1 where name='zs' and age<18;
  ```

- 修改数据

  ```sql
  update 表名 set 列名=值
  update 表名 set 列名=值 where 条件;
  
  update tb1 set name='zs';					-- 将表中所有name改为zs
  update tb1 set name='zs' where id=10;		-- 将表中id为10的name改为zs
  update tb1 set age=age+1;					-- 所有年龄+1
  ```

- 查询数据

  ```sql
  select * from 表名;
  select 列名,列名,列名 from 表名;
  select 列名 as 别名,列名 as 别名 from 表名;
  select * from 表名 where 条件;
  
  select * from tb1;
  select id,name,age from tb1;
  select id,name as N,age from tb1;
  select * from tb1 where age>18
  ```


#### 必备SQL语句

- 条件搜索

  ```sql
  select * from info where not exists (select * from depart where id=5);
  select * from info where id not in (1,4,6);
  select * from info where depart_id in (select id from depart;
  ```

- 通配符

  %：任意字符

  _：一个字符

  ```sql
  select * from info where name like "_a%";
  ```

  注意：一般用于数量小，数据量大的搜索

- 映射

  ```sql
  select id,
  	name,
  	(select title from depart where depart.id=info.depart_id) as depart 
  from info;
  
  +----+-------+--------+
  | id | name  | depart |
  +----+-------+--------+
  |  1 | zs    | 开发   |
  |  2 | ls    | 开发   |
  |  3 | ww    | 运营   |
  |  4 | zl    | 开发   |
  |  5 | kelly | 开发   |
  |  6 | james | 开发   |
  |  7 | 李杰  | 销售   |
  +----+-------+--------+	
  # 注意：效率很低
  
  select id,
  	name,
  	case depart_id when 1 then "第一部门" when 2 then "第二部门" else "第三部门" end v1,
  	case when age<18 then "少年" when age<30 then "青年" else "油腻男" end v2
  from info;
  ```

- 排序

  ```sql
  select * from info order by age desc;					-- 倒序
  select * from info order by age asc;					-- 顺序
  select * from info order by age by age asc,id desc;		-- 优先age，其次desc
  ```

- 取部分

  ```sql
  select * from info limit 4;								-- 获取前4条
  select * from info limit 3 offset 2;						-- 从第2个位置开始取3条数据
  select * from info where id > 3 order by age desc limit 4;
  ```

- 分组

  ```sql
  select age from info group by age;
  select age,max(id) from info group by age;
  select age,count(id) from info group by age;
  
  # 对已经得到的聚合函数进行再次筛选，需要使用having，不能用where
  select depart_id,count(name) from info group by depart_id having count(name)>2;
  ```

  ```sql
  # 到目前为止SQL执行顺序
  	where; group by; having; order by; limit
  
  select age,count(id) from info where id>2 group by age havinh count(id)>1 order by age limit 2;
  ```

- 左右连表

  ```sql
  主表 left outer join 从表 on 主表.x = 从表.y;
  从表 right outer join 主表 on 主表.x = 从表.y;
  表 inner join 表 on 条件;		-- 内连接
  
  select * from info left outer join depart on info.depart_id=depart.id;
  select info.id,info.name,depart.title from info left outer join depart on info.depart_id=depart.id;
  ```

- 联合(上下连表)

  ```sql
  select id,title from depart
  union
  select id,name from info;
  ```

  注意：不同类型也可以连接，自动去重（如果保存所有则`union -> union all`）

#### 表关系

用外键约束：

```sql
create table info(
	id int not null auto_increment primary key,
    name varchar(16) not null,
    email varchar(32) null,
    age int,
    depart_id int not null,
    constraint fk_info_depart foreign key (depart_id) reference depart(id)
)default charset=utf8;
```

如果表结构已经创建好了，额外增加外键：

```sql
alter table info add constraint fk_info_depart foreign key info(depart_id) reference depart(id);
```

删除外键：

```sql
alter table info drop foreign key fk_info_depart;
```
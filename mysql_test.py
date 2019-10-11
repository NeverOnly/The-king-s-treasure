# 1).连接到数据库（host:localhost username:root password:root database:books）
# 2).查询图书表的数据（包括：图书id、图书名称、阅读量、评论量）
# 3).获取查询结果的总记录数
# 4).获取查询结果的第一条数据
# 5).获取全部的查询结果


# 导包
import pymysql
# 建立数据库连接
conn = pymysql.connect(host = "localhost", user = "root", password = "root", database = "books", port = 3306, autocommit = False)
# 创建游标对象
cursor = conn.cursor()
# 执行操作：查询图书表的数据
inquire_book = "select id,title,`read`,comment from t_book"
cursor.execute(inquire_book)

# 获取查询结果的总记录数
tol = cursor.rowcount
print("记录总数为：{}".format(tol))

# 获取查询结果的第一条数据
one = cursor.fetchone()
print("第一条数据为：",one)

# 获取全部的查询结果
for_all = cursor.fetchall()
for i in for_all:
    print(i)


# 关闭数据库和游标
cursor.close()
conn.close()
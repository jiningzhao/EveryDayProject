"""
开发人员：赵吉宁
脚本功能：连接MYSQL数据库
时间：2019年8月12日
"""
import pymysql

db = pymysql.Connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "newbanker",
    db = "go",
    # charset = "utf8"
)

# op = "select * from component"
# cursor.execute(op)
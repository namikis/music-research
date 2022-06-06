from email import charset
import pymysql.cursors

conn = pymysql.connect(host='localhost',
                        user='root',
                        password='',
                        database='music-research',
                        charset='utf8mb4',
                        )

with conn.cursor() as cursor:
    sql = "INSERT INTO musics VALLUE('')"
    cursor.excute(sql)

conn.close()

from email import charset
import pymysql.cursors
import os
from dotenv import load_dotenv

# .envファイルの内容を読み込見込む
load_dotenv()

# os.environを用いて環境変数を表示させます
print(os.environ['API_KEY'])

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

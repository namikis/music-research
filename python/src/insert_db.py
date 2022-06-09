import pymysql.cursors
import os

port = os.environ['DB_PORT']
host = os.environ['DB_HOST']
user = os.environ['DB_USERNAME']
password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']

conn = pymysql.connect(host=host,
                        user=user,
                        password=password,
                        database=db_name,
                        charset='utf8mb4',
                        )

with conn.cursor() as cursor:
    sql = "INSERT INTO musics (music_name, valence, energy, music_id) VALUE('test_name2', 1, 2, '123445')"
    cursor.execute(sql)

conn.commit()

conn.close()

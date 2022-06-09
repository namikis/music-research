import pymysql.cursors
import os

class DB_CONN:
    def __init__(self):
        port = os.environ['DB_PORT']
        host = os.environ['DB_HOST']
        user = os.environ['DB_USERNAME']
        password = os.environ['DB_PASSWORD']
        db_name = os.environ['DB_NAME']

        self.conn = pymysql.connect(host=host,
                                user=user,
                                password=password,
                                database=db_name,
                                charset='utf8mb4',
                                )

    def insertMusic(self, data_list):
        with self.conn.cursor() as cursor:
            #sql = "INSERT INTO musics (music_name, valence, energy, music_id) VALUE('test_name2', 1, 2, '123445')"
            sql = "INSERT INTO musics (music_name, valence, energy, music_id, artist_name) VALUE "
            for data in data_list.values():
                if "valence" in data and "energy" in data:
                    print(data)
                    sql += "('" + data['music_name'] + "','" + str(data['valence']) + "','" + str(data['energy']) + "','" + data['music_id'] + "','" + data["artist_name"] + "'),"
            sql = sql.rstrip(',')
            sql += ";"
            cursor.execute(sql)
            self.conn.commit()

    def closeDB(self):
        self.conn.close()

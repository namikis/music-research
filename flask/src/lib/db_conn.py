import pymysql.cursors
import os
from dotenv import load_dotenv

load_dotenv()

class DB_CONN:
    def __init__(self, local=False):
        port = os.environ['DB_PORT']
        if local == False:
            host = os.environ['DB_HOST']
        else:
            host = "localhost"
        user = os.environ['DB_USERNAME']
        password = os.environ['DB_PASSWORD']
        db_name = os.environ['DB_NAME']

        self.conn = pymysql.connect(host=host,
                                user=user,
                                password=password,
                                database=db_name,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor
                                )

    def insertMusic(self, data_list):
        with self.conn.cursor() as cursor:
            #sql = "INSERT INTO musics (music_name, valence, energy, music_id) VALUE('test_name2', 1, 2, '123445')"
            sql = "INSERT INTO musics (music_name, valence, energy, music_id, artist_name) VALUE "
            count = 0
            #50個ずつISNERT
            for data in data_list.values():
                count += 1
                if "valence" in data and "energy" in data:
                    #print(data)
                    sql += "('" + data['music_name'] + "','" + str(data['valence']) + "','" + str(data['energy']) + "','" + data['music_id'] + "','" + data["artist_name"] + "'),"
                if count == 50:
                    sql = sql.rstrip(',') + ";"
                    print("\n" + sql)
                    cursor.execute(sql)
                    sql = "INSERT INTO musics (music_name, valence, energy, music_id, artist_name) VALUE "
                    count = 0
        self.conn.commit()

    def selectSQL(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
        return result

    def getArtists(self):
        sql = "SELECT DISTINCT(artist_name) FROM musics"
        artists = self.selectSQL(sql)
        self.closeDB()
        return artists

    def getMusicsByArtistName(self, artist_name):
        sql = "SELECT music_name, valence, energy, artist_name, music_id FROM musics WHERE artist_name= " + artist_name
        musics = self.selectSQL(sql)
        self.closeDB()
        return musics

    def getMusicsByFeature(self, music_feature):
        param = 0.005
        valence_range = "valence <= " + str(music_feature["valence"] + param) + "&& valence >= " +str(music_feature["valence"] - param)
        energy_range = "energy <= " + str(music_feature["energy"] + param) + "&& energy >= " +str(music_feature["energy"] - param)
        sql = "SELECT music_name, valence, energy, artist_name, music_id FROM musics WHERE " + valence_range + " && " + energy_range
        musics = self.selectSQL(sql)
        self.closeDB()
        return musics

    def getMusicsByFormalName(self, music_name_list):
        in_text = self.getInText(music_name_list)
        sql = "SELECT music_name, valence, energy, artist_name, music_id FROM musics WHERE music_name IN" + in_text
        musics = self.selectSQL(sql)
        self.closeDB()
        return musics

    def getInText(self, music_list):
        in_text = "("
        for music_name in music_list:
            music_name = music_name.replace("'", " ")
            music_name = music_name.replace('"', " ")
            in_text += '"' + music_name + '",'
        in_text = in_text[:-1] + ")"
        print(in_text)
        return in_text

    def getMusicDist(self):
        sql = "SELECT artist_name AS artist, COUNT(*) AS music_count from musics GROUP BY artist_name ORDER BY music_count;"
        res = self.selectSQL(sql)
        self.closeDB()
        return res

    def getAllMusicFeatures(self):
        sql = "SELECT valence, energy from musics;"
        res = self.selectSQL(sql)
        self.closeDB()
        return res

    def closeDB(self):
        self.conn.close()

from lib.db_conn import DB_CONN
import lib.logic as logic

class mainController():

    @staticmethod
    def getArtist():
        db_conn = DB_CONN()
        return db_conn.getArtists()

    @staticmethod
    def getMusicsByArtistName(artist_name):
        db_conn = DB_CONN()
        return db_conn.getMusicsByArtistName(artist_name)

    @staticmethod
    def fusionMusic(target_music_features):
        fusioned_feature = logic.getFusionedFeature(target_music_features)
        db_conn = DB_CONN()
        return db_conn.getMusicsByFeature(fusioned_feature)


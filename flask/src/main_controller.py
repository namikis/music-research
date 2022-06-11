from lib.db_conn import DB_CONN
from lib.music_feature import SpotifyMusic
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

    @staticmethod
    def getFormalName(search_name):
        spotify_music = SpotifyMusic()
        return spotify_music.searchFormalName(search_name)


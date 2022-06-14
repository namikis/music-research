from lib.db_conn import DB_CONN
from lib.music_feature import SpotifyMusic
import pprint

spotify_music = SpotifyMusic()
#musics = spotify_music.getMusics()
#musics = spotify_music.getMusicsSmall()
musics = spotify_music.getMusicsLarge()

# musics = {
#     "1eGY6roK1W2vFIhDXu2lXq" :{
#         "music_name" : "m Ready",
#         "valence" : 0.752,
#         "energy" : 0.687,
#         "artist_name" : "Tevin Campbell",
#         "music_id": "1eGY6roK1W2vFIhDXu2lXq" 
#     },
# }

db_conn = DB_CONN()
db_conn.insertMusic(musics)
db_conn.closeDB()
print("completed.")

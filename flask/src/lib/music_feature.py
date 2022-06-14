import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

class SpotifyMusic():
    def __init__(self):
        ccm = SpotifyClientCredentials(client_id = os.environ['SPOTIFY_CLIENT_ID'], client_secret = os.environ['SPOTIFY_SECRET_ID'])
        self.spotify = spotipy.Spotify(client_credentials_manager = ccm)

    def preProcess(self, music_data):
        music_name = music_data['name'].replace("'", " ")
        artist_name = music_data['artists'][0]['name'].replace("'", " ")
        return {"music_name": music_name, "artist_name": artist_name}

    def getMusics(self):
        all_track_ids = []
        audio_data_list = {}

        for num in range(0, 22, 2):
            year = "year:" + str(2000 + num) + "-" + str(2000 + num + 1)
            search_str = "genre:j-pop " + year
            for i in range(20):
                offset = 50 * i
                results = self.spotify.search(q=search_str, limit=50, offset=offset, type='track', market=None)
                for result in results['tracks']['items']:
                    processed_music = self.preProcess(result)
                    print(processed_music['music_name'], "-", processed_music['artist_name'])
                    all_track_ids.append(result['id'])
                    audio_data_list[result['id']] = {"music_name":processed_music['music_name'], "artist_name":processed_music['artist_name']}
        


        track_ids = list(set(all_track_ids))

        for idx in range(0, 10000, 100):
            audio_feature_list = self.spotify.audio_features(track_ids[idx:idx+99])
            for audio_feature in audio_feature_list:
                audio_data_list[audio_feature['id']]["valence"] = audio_feature['valence']
                audio_data_list[audio_feature['id']]["energy"] = audio_feature['energy']
                audio_data_list[audio_feature['id']]["music_id"] = audio_feature['id']

        return audio_data_list

    def getMusicsLarge(self):
        all_track_ids = []
        audio_data_list = {}

        for year_count in range(1980, 2023):
            year = "year:" + str(year_count)
            search_str = "genre:j-pop " + year
            for i in range(20):
                offset = 50 * i
                results = self.spotify.search(q=search_str, limit=50, offset=offset, type='track', market=None)
                for result in results['tracks']['items']:
                    processed_music = self.preProcess(result)
                    print(processed_music['music_name'], "-", processed_music['artist_name'])
                    all_track_ids.append(result['id'])
                    audio_data_list[result['id']] = {"music_name":processed_music['music_name'], "artist_name":processed_music['artist_name']}
        


        track_ids = list(set(all_track_ids))

        for idx in range(0, len(track_ids), 100):
            audio_feature_list = self.spotify.audio_features(track_ids[idx:idx+99])
            for audio_feature in audio_feature_list:
                audio_data_list[audio_feature['id']]["valence"] = audio_feature['valence']
                audio_data_list[audio_feature['id']]["energy"] = audio_feature['energy']
                audio_data_list[audio_feature['id']]["music_id"] = audio_feature['id']

        return audio_data_list

    def getMusicsSmall(self):
        all_track_ids = []
        audio_data_list = {}

        
        year = "year:2020"
        search_str = "genre:j-pop " + year
            
        results = self.spotify.search(q=search_str, limit=50, type='track', market=None)

        for result in results['tracks']['items']:
            processed_music = self.preProcess(result)
            print(processed_music['music_name'], "-", processed_music['artist_name'])
            all_track_ids.append(result['id'])
            audio_data_list[result['id']] = {"music_name":processed_music['music_name'], "artist_name":processed_music['artist_name']}
        


        track_ids = list(set(all_track_ids))
    
        audio_feature_list = self.spotify.audio_features(track_ids)
        for audio_feature in audio_feature_list:
            audio_data_list[audio_feature['id']]["valence"] = audio_feature['valence']
            audio_data_list[audio_feature['id']]["energy"] = audio_feature['energy']
            audio_data_list[audio_feature['id']]["music_id"] = audio_feature['id']

        return audio_data_list

    def searchFormalName(self, search_name):
        result = self.spotify.search(q=search_name, type='artist', market=None)
        return result["artists"]["items"][0]["name"]

    def searchFormalMusics(self, search_name):
        results = self.spotify.search(q=search_name, type='track', market=None)
        music_list = []
        for result in results["tracks"]["items"]:
            music_list.append(result["name"])
        return music_list


# コンテナ外から実行

import matplotlib.pyplot as plt
 
artist_info = [
               {
                   "artist" : "yonezu",
                    "music_count": 20
               },
               {
                   "artist" : "higedan",
                    "music_count": 30
               },
               {
                   "artist" : "yorushika",
                    "music_count": 25
               },
               {
                   "artist" : "zutomayo",
                    "music_count": 50
               },
               {
                   "artist" : "ringo",
                    "music_count": 40
               },
]

artist_name_list = [artist["artist"] for artist in artist_info]
music_count_list = [artist["music_count"] for artist in artist_info]

print(artist_name_list)
print(music_count_list)

left = []
for i in range(len(artist_name_list)):
  left.append(i + 1)

print(left)

plt.bar(left, music_count_list, tick_label=artist_name_list)
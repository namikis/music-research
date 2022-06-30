import sys
sys.path.append("../")
from lib.db_conn import DB_CONN
import matplotlib as mpl
import matplotlib.pyplot as plt
import pprint
import numpy as np

db_conn = DB_CONN()
artist_info = db_conn.getMusicDist()
 
# artist_info = [
#                {
#                    "artist" : "yonezu",
#                     "music_count": 20
#                },
#                {
#                    "artist" : "higedan",
#                     "music_count": 30
#                },
#                {
#                    "artist" : "yorushika",
#                     "music_count": 25
#                },
#                {
#                    "artist" : "zutomayo",
#                     "music_count": 50
#                },
#                {
#                    "artist" : "ringo",
#                     "music_count": 40
#                },
# ]

artist_name_list = [artist["artist"] for artist in artist_info]
music_count_list = [artist["music_count"] for artist in artist_info]

# print(music_count_list)

# 余白を調整
mpl.rcParams['axes.xmargin'] = 0
plt.subplots_adjust(bottom=0.15)

xticks = []
yticks = np.arange(0, 1600, 100)

x_ticklabel = []
for i in range(0, max(music_count_list), 50):
  x_ticklabel.append(str(i) + "~" + str(i+50))
  xticks.append((i + i + 50) / 2)

fig, ax = plt.subplots()
ax.set_xlabel("Number of songs by artist")
ax.set_ylabel("Number of artists")
ax.set_xticks(xticks)
ax.set_yticks(yticks)
ax.set_xticklabels(x_ticklabel, rotation=90)

ax.hist(music_count_list, bins=32, alpha=0.5, ec='navy', range=(0, 1600))
plt.show()
fig.savefig("./images/hist.png")
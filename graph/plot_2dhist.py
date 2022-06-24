
# コンテナ外から実行
import sys
sys.path.append("../")
from flask.src.lib.db_conn import DB_CONN
import matplotlib as mpl
import matplotlib.pyplot as plt
import pprint
import numpy as np

import matplotlib.cm as cm

db_conn = DB_CONN(local=True)
music_info_list = db_conn.getAllMusicFeatures()
 

valence_list = [float(music["valence"]) for music in music_info_list]
energy_list = [float(music["energy"] )for music in music_info_list]

# print(valence_list)
# print(energy_list)

# 余白を調整
mpl.rcParams['axes.xmargin'] = 0
plt.subplots_adjust(bottom=0.15)

fig = plt.figure()
ax = fig.add_subplot(111)

g = ax.hist2d(valence_list, energy_list, bins = 60, cmap = cm.jet)
ax.set_xlabel("valence")
ax.set_ylabel("energy")
fig.colorbar(g[3], ax = ax)
plt.show()

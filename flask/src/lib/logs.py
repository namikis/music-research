import logging

# artist検索　アーティスト名
# 楽曲検索　楽曲名
# フュージョン　曲名✖️２
# プレイヤーを開く　曲名

class LogWriter():
    def __init__(self):
        logging.basicConfig(filename='./logs/actions.log', format='%(asctime)s %(message)s', datefmt='%m/%d %I:%M:%S %p', level=logging.WARNING)

    def writeLog(self, text):
        logging.warning(text)

    def writeFusionLog(self, artist_name_list):
        text = "FUSION: " + artist_name_list[0] + " ✖️ " + artist_name_list[1]
        self.writeLog(text)

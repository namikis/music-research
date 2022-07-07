import logging

# artist検索　アーティスト名
# 楽曲検索　楽曲名
# フュージョン　曲名✖️２
# プレイヤーを開く　曲名

class LogWriter():
    def __init__(self, log_type):
        self.logger = logging.getLogger(log_type)
        self.logger.setLevel(logging.DEBUG)
        ch = logging.FileHandler("./logs/" + log_type + ".log")
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def writeLog(self, text):
        self.logger.debug(text)

    def writeFusionLog(self, artist_name_list):
        text = "FUSION: " + artist_name_list[0] + " ✖️ " + artist_name_list[1]
        self.writeLog(text)

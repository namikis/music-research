from flask import Flask, request, jsonify
from main_controller import mainController
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    test = "testaaaa"
    return test

@app.route("/artists")
def getArtists():
    return jsonify(mainController.getArtist())

@app.route("/musics", methods=['GET', 'POST'])
def getMusicsByArtistName():
    artist_name = request.form['artist_name']
    return jsonify(mainController.getMusicsByArtistName(artist_name))

@app.route("/musics/fusion", methods=['POST'])
def fusionMusic():
    # target_music_features = [
    #     {
    #         "valence": 0.45,
    #         "energy": 0.87
    #     },
    #     {
    #         "valence": 0.54,
    #         "energy": 0.67
    #     }
    # ]
    target_music_features = request.form
    return jsonify(mainController.fusionMusic(target_music_features))

@app.route("/artists/formal_name", methods=['POST'])
def getFormalName():
    search_name = request.form["search_name"]
    return jsonify(mainController.getFormalName(search_name))

@app.route("/musics/formal_name", methods=['POST'])
def getFormalMusic():
    search_name = request.form["search_name"]
    return jsonify(mainController.getFormalMusics(search_name))

@app.route("/logs/search", methods=['POST'])
def writeSearchLog():
    search_data = request.form
    return mainController.writeSearchLog(search_data)

@app.route("/logs/player", methods=['POST'])
def writePlayerLog():
    set_player_data = request.form
    return mainController.writePlayerLog(set_player_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

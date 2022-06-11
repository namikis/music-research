from flask import Flask, request, jsonify
from main_controller import mainController
app = Flask(__name__)

@app.route("/")
def index():
    test = "testaaaa"
    return test

@app.route("/artists")
def getArtists():
    return jsonify(mainController.getArtist())

@app.route("/musics")
def getMusicsByArtistName():
    artist_name = request.args.get('artist_name', '')
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
    target_music_features = request.form.get("target_musics")
    return jsonify(mainController.fusionMusic(target_music_features))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

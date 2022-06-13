def getFusionedFeature(target_features):
    valence = (float(target_features["valence1"]) + float(target_features["valence2"])) / 2
    energy = (float(target_features["energy1"]) + float(target_features["energy2"])) / 2
    fusioned_feature = {
        "valence": valence,
        "energy": energy
    }
    return fusioned_feature

def preprocessData(musics):
    for music in musics:
        music["music_name"] = music["music_name"] + " - " + music["artist_name"]
    return musics

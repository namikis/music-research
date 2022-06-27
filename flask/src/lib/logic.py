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

def getFilteredMusics(musics, fusioned_feature):
    for music in musics:
        valence_delta = float(music["valence"]) - float(fusioned_feature["valence"])
        energy_delta = float(music["energy"]) - float(fusioned_feature["energy"])
        music["distance"] = valence_delta * valence_delta + energy_delta * energy_delta

    sorted_musics = sorted(musics, key=lambda x:x["distance"])
    if len(sorted_musics) < 3:
        response = sorted_musics[:len(sorted_musics)]
    else:
        response = sorted_musics[:3]

    return preprocessData(response)
    
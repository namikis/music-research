def getFusionedFeature(target_features):
    valence = (float(target_features[0]["valence"]) + float(target_features[1]["valence"])) / 2
    energy = (float(target_features[0]["energy"]) + float(target_features[1]["energy"])) / 2
    fusioned_feature = {
        "valence": valence,
        "energy": energy
    }
    return fusioned_feature

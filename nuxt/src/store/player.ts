const state = {
    musicIdInPlayer: '' as String
}

const mutations = {
    setMusicIdToPlayer(state: any, music_id: String){
        state.musicIdInPlayer = music_id
    }
}

const player = {
    state,
    mutations,
}

export default player

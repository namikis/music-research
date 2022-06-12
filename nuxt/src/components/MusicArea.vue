<template>
    <div class="music_area_wrapper">
        <div id="music_player_field" class="music_player"></div>
        <div class="music_field">
            <h3 class="selected_artist_name">{{ selected_artist_name }}</h3>
            <div class="music_items">
                <div class="music_item" v-for="music in music_list" :key="music.music_id" @click="setPlayer(music.music_id)">
                    <span @click="setTarget(music)"> ▲</span>
                    <span> {{ music.music_name }}</span>
                </div>
            </div>
        </div>
        
    </div>
</template>
<script lang="ts">
import Vue from 'vue'
import axios from 'axios'
export type Music = {
    music_name: string,
    valence: Number,
    energy: Number,
    music_id: string,
    artist_name: string
}
export default Vue.extend({
    props: {
        selected_artist_name:{
            type: String,
            default: ""
        },
        target_musics: {
            type: Array,
            default: ["tes"]
        },
    },  
    data(){
        return {
            music_list: [] as Array<Music>
        }
    },
    mounted(){
        this.music_list = [
            {
                "music_name": 'ミラーチューン',
                "valence": 0.895,
                "energy": 0.933,
                "music_id": "0R8JLNP107Hr7V7lL9oh13",
                "artist_name": "artist1"
            },
            {
                "music_name": 'あいつら全員同窓会',
                "valence": 0.913,
                "energy": 0.913,
                "music_id": "2VIK6jaaKghS4QPHr6sAkv",
                "artist_name": "artist2"
            },
            {
                "music_name": "秒針を噛む",
                "valence": 0.775,
                "energy": 0.962,
                "music_id": "4HgsPAX3MmMgIT60hJ4W4U",
                "artist_name": "artist3"
            }
        ]
    },
    methods: {
        setTarget(music: Music){
            this.$emit("setTarget", music)
        },
        getMusicsByArtistName(){
            const url = "http://localhost:5000/musics"
            const params = new URLSearchParams()
            params.append('artist_name', "'" + this.selected_artist_name + "'")
            console.log(url)
            axios.post(url, params).then((response) => {
                this.music_list = response.data
            })
        },
        setPlayer(music_id: String){
            //this.$store.commit('player/setMusicIdToPlayer', music_id)
            //console.log(this.$store.state.player.musicIdInPlayer)
            // 確認： encrypted-media; を消さないと再生されない
            let player_tag = '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/'+music_id+'?utm_source=generator" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture"></iframe>'

            document.getElementById('music_player_field')!.innerHTML = player_tag
        },
        getFusionMusic(){
            const url = "http://localhost:5000/musics/fusion"
            const params = new URLSearchParams()
            params.append("valence1", this.target_musics[0]["valence"])
            params.append("energy1", this.target_musics[0]["energy"])
            params.append("valence2", this.target_musics[1]["valence"])
            params.append("energy2", this.target_musics[1]["energy"])
            axios.post(url, params).then((response) => {
                this.music_list = response.data
            })
        }
    },
    watch: {
        selected_artist_name: function(){
            console.log(this.selected_artist_name)
            if(this.selected_artist_name.match("FUSION:")){
                this.getFusionMusic()
            }else if(this.selected_artist_name !== ""){
                this.getMusicsByArtistName()
            }
        }
    }
})
</script>
<style>
    .music_area_wrapper{
        background: black;
        width: 70%;
        overflow-y: scroll;
        height: 91vh;
    }
    .music_field{
        width: 85%;
        margin: 20px auto;
    }
    .music_player{
        width: 50%;
        position: fixed;
        bottom: 0;
        right: 0;
        margin:0 10% 30px 0;
        z-index: 999;
    }
    .music_items{
        display: flex;
        flex-wrap: wrap;
        padding-bottom:100px;
    }
    .music_item{
        color: white;
        border: 1px solid white;
        border-radius: 20px;
        padding: 5px 10px;
        margin:10px;
        opacity: 0.9;
    }
    .music_item:hover{
        background: white;
        color: black;
    }
    .music_item{
        cursor: pointer;
    }
    .selected_artist_name{
        color: white;
        font-weight: bold;
    }
</style>

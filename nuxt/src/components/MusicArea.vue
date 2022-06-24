<template>
    <div class="music_area_wrapper">
        <div id="music_player_field" class="music_player"></div>
        <div class="music_field">
            <h3 class="selected_artist_name">{{ selected_artist_name }}</h3>
            <div>
                <div v-if="music_list.length > 0" class="music_items">
                    <div class="music_item" v-for="music in music_list" :key="music.music_id">
                        <span @click="setTarget(music)" class="toFusionButton"> ▲</span>
                        <span @click="setTargetMusicId(music.music_id)" class="music"> {{ music.music_name }}</span>
                    </div>
                </div>
                <div v-else-if="search_error">
                    <h1 class="intro_message">Not Found.</h1>
                </div>
                <div v-else class="intro_wrapper">
                    <h1 class="intro_message">Search,  Listen, and Fusion Musics.</h1>
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
    props:["target_musics", "selected_artist_name", "target_music_id"],
    data(){
        return {
            music_list: [] as Array<Music>,
            search_error: false as boolean,
        }
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
        setTargetMusicId(music_id: String){
            this.$emit("update:target_music_id", music_id)
        },
        setPlayer(){
            //this.$store.commit('player/setMusicIdToPlayer', music_id)
            //console.log(this.$store.state.player.musicIdInPlayer)
            // 確認： encrypted-media; を消さないと再生されない
            let player_tag = '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/'+this.target_music_id+'?utm_source=generator" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture"></iframe>'

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
        },
        getSearchMusic(search_name: string){
            const url = "http://localhost:5000/musics/formal_name"
            const params = new URLSearchParams()
            params.append("search_name", search_name)
          
                axios.post(url, params).then((response) => {
                    this.music_list = response.data
                    console.log(response.data)
                    if(this.music_list.length == 0){
                        this.search_error = true;
                    }
                }).catch(error => {
                    console.log("Not Found")
                    this.search_error = true;
                })
        }
    },
    watch: {
        selected_artist_name: function(){
            console.log(this.selected_artist_name)
            if(this.selected_artist_name.match("FUSION:")){
                this.getFusionMusic()
            }else if(this.selected_artist_name.match("SONGS:")){
                this.getSearchMusic(this.selected_artist_name.substring(7))
            }else if(this.selected_artist_name !== ""){
                this.getMusicsByArtistName()
            }
            this.search_error = false;
        },
        target_music_id: function(){
            this.setPlayer()
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
        position:relative;
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
    /* .music_item:hover{
        background: white;
        color: black;
    } */
    .music_item{
        cursor: pointer;
    }
    .music:hover{
        color: #00DC82;
    }
    .selected_artist_name{
        color: white;
        font-weight: bold;
    }
    .intro_message{
        color: #00DC82;
    }
    .intro_wrapper{
        position:absolute;
        top:40%;
        left:15%;
    }
    .toFusionButton{
        background: white;
        color: black;
        border-radius: 50%;
        padding: 2px;
    }
    .toFusionButton:hover{
        color: #00DC82;
        opacity: 0.8;
    }
</style>

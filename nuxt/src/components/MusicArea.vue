<template>
    <div class="music_area_wrapper">
        <div class="music_field">
            <h1>{{ selected_artist_name }}</h1>
            <div class="music_items">
                <div class="music_item" v-for="music in music_list" :key="music.music_id">
                    <p>{{ music.music_name }} <span @click="setTarget(music)">▲</span> </p>
                    <iframe style="border-radius:12px" :src="'https://open.spotify.com/embed/track/' + music.music_id +'?utm_source=generator'" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>
                </div>
            </div>
        </div>
        
    </div>
</template>
<script lang="ts">
import Vue from 'vue'
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
        }
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
        }
    },
    watch: {
        selected_artist_name: function(){
            // get musics of artist_name
        }
    }
})
</script>
<style>
    .music_area_wrapper{
        background: gray;
        width: 70%;
    }
    .music_field{
        width: 85%;
        margin: 20px auto;
    }
</style>

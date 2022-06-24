<template>
    <div class="fusion_wrapper">

        <div class="target_item" v-for="target_music in target_musics" :key="target_music.music_id">
            <span @click="deleteTarget(target_music.music_id)" class="deleteButton">▼</span>
            <span @click="setTargetMusicId(target_music.music_id)">
                {{ target_music.music_name  }}
                -
                {{ target_music.artist_name }}
            </span>
        </div>
       
        <div>
            <div class="fusion_button_wrapper" v-if="target_musics.length==2" @click="getFusion">
                <span>Fusion!</span>    
            </div>
        </div>
    </div>    
</template>
<script lang="ts">
import Vue from 'vue'
import { Music } from './MusicArea.vue'
export default Vue.extend({
    props:["target_musics", "selected_artist_name", "target_music_id"],
    methods: {
        deleteTarget(music_id: String){
            const processed_musics = this.target_musics.filter((music : Music) => music.music_id != music_id)
            this.$emit("update:target_musics", processed_musics)
        },
        getFusion(){
            const fusion_name = "FUSION: " + this.target_musics[0]['music_name'] + " × " + this.target_musics[1]['music_name']
            this.$emit("update:selected_artist_name", fusion_name)
        },
        setTargetMusicId(target_music_id: string){
            this.$emit("update:target_music_id", target_music_id)
        }
    },
    mounted(){
        console.log(typeof(this.target_musics))
    }

})
</script>

<style>
    .fusion_wrapper{
        display: flex;
        padding: 10px;
        background: black;
        opacity: 0.9;
        justify-content: space-evenly;
    }
    .target_item, .fusion_button_wrapper{
        align-items: center;
        color: white;
        border: 1px solid white;
        border-radius: 20px;
        padding:5px 10px;
    }
    .target_item span, .fusion_button_wrapper{
        cursor: pointer;
        font-weight: bold;
    }
    .fusion_button_wrapper:hover{
        background: #00DC82;
        color: black;
    }
    .fusion_button_wrapper{
        color:#00DC82;
    }
    .deleteButton{
        background: white;
        color: black;
        border-radius: 50%;
        padding: 2px;
    }
    .deleteButton:hover{
        color: #00DC82;
        opacity: 0.8;
    }
</style>

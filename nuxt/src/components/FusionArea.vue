<template>
    <div class="fusion_wrapper">

        <div class="target_item" v-for="target_music in target_musics" :key="target_music.music_id">
            <span @click="deleteTarget(target_music.music_id)">▼</span>
            {{ target_music.music_name  }}
            -
            {{ target_music.artist_name }}
        </div>
       
        <div class="fusion_button_wrapper">
            <span v-if="target_musics.length==2">Fusion!</span>    
        </div>
    </div>    
</template>
<script lang="ts">
import Vue from 'vue'
import { Music } from './MusicArea.vue'
export default Vue.extend({
    props: {
        target_musics: {
            type: Array,
            default: ["tes"]
        }
    },
    methods: {
        deleteTarget(music_id: String){
            const processed_musics = this.target_musics.filter(music => music.music_id != music_id)
            this.$emit("update:target_musics", processed_musics)
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
        background: lightgray;
        justify-content: space-evenly;
    }
    .target_item, .fusion_button_wrapper{
        align-items: center;
    }
</style>

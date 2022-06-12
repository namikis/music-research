<template>
  <div class="wrapper">
    <Header />
    <FusionArea v-if="target_musics.length >= 1" 
      :target_musics.sync="target_musics"
      :selected_artist_name.sync="selected_artist_name"
    />
    <div class="container">
      <ArtistArea :selected_artist_name.sync="selected_artist_name" />
      <MusicArea 
        :selected_artist_name.sync="selected_artist_name"
        :target_musics.sync="target_musics"
        @setTarget="setTarget"  
      />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { Music } from '../components/MusicArea.vue'

export default Vue.extend({
  name: 'IndexPage',
  data(){
    return {
      target_musics: [] as Array<Music>,
      selected_artist_name: ""
    }
  },
  methods: {
    setTarget(music: Music){
      if(this.target_musics.length == 2){
        alert('すでに二つ選択されています。どちらかを取り消してください。')
      }else{
        this.target_musics.push(music)
      }
    }
  }

})
</script>
<style>
  .container{
    display: flex;
  }
</style>

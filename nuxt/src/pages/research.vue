<template>
  <div class="wrapper">
    <Header />
    <div class="research_container">
        <div class="research_wrapper">
            <h1 style="color: white;">実験用資料</h1>
            <div class="research_items">
                <div class="research_item">
                  <h1>リンク</h1>
                  <a href="https://docs.google.com/forms/d/e/1FAIpQLScDfsFRKLGLBAMaokk8dte9ai36PEZqzJ-2UxHkP_Wgkno2ug/viewform?usp=sf_link" target="_blank">アンケート</a>
                  <a href="https://open.spotify.com/" target="_blank">Spotify</a>
                </div>
                <div class="research_item">
                  <h1>
                    手順
                    <span
                     v-if="open_state == 1" 
                     @click="changeState"
                     class="state_icon"
                    >🔻</span>
                    <span
                     v-else
                     @click="changeState"
                     class="state_icon"
                     >🔺</span>
                  </h1>
                  <Introduction 
                    v-if="open_state !== 1"
                  />                  
                </div>
                <div class="research_item">
                  <h1>動画１（Spotify）</h1>
                  <video controls width="60%">
                      <source src="/research/Spotify.mp4" type="video/mp4">
                      Sorry, your browser doesn't support embedded videos.
                  </video>
                </div>
                <div class="research_item">
                  <h1>動画２（FUSION MUSIC）</h1>
                  <video controls width="60%">
                      <source src="/research/FUSIONMUSIC.mp4" type="video/mp4">
                      Sorry, your browser doesn't support embedded videos.
                  </video>
                </div>
               
            </div>
            
        </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'IndexPage',
  data(){
    return {
      open_state: 1
    }
  },
  methods:{
    changeState(){
      this.open_state *= -1
    }
  }

})
</script>
<style>
  .research_container{
    display: flex;
    background: black;
    height: 300vh;
  }
  .research_wrapper{
    width: 60%;
    margin: 20px auto;
  }
  .research_items{
    padding: 20px;
    margin: 10px;
  }
  .research_item{
      margin: 60px 0;
  }
  .research_item a{
      padding: 5px;
      font-weight: bold;
      color: white;
      font-size: 26px;
      text-decoration: none;
      border: 2px solid white;
  }
  .research_item h1{
    background: white;
    padding: 5px 15px;
    margin: 30px 0;
  }
  video {
    width: 100%;
  }
  .state_icon{
    color: black;
    cursor: pointer;
  }
</style>

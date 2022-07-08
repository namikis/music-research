<template>
  <div class="wrapper">
    <Header />
    <div class="research_container">
        <div class="research_wrapper">
            <h1 style="color: white;">実験用リンク</h1>
            <div class="research_items">
                <div class="research_item">
                  <a href="/research/introduction.pdf" target="_blank">手順書</a>
                  <a href="https://docs.google.com/forms/d/e/1FAIpQLScDfsFRKLGLBAMaokk8dte9ai36PEZqzJ-2UxHkP_Wgkno2ug/viewform?usp=sf_link" target="_blank">アンケート</a>
                  <a href="https://open.spotify.com/" target="_blank">Spotify</a>
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
  name: 'IndexPage'

})
</script>
<style>
  .research_container{
    display: flex;
    background: black;
    height: 150vh;
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
      margin: 30px 0;
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
    color: white;
    margin: 60px 0;
  }
</style>

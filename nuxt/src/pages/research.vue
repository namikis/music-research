<template>
  <div class="wrapper">
    <Header />
    <div class="research_container">
        <div class="research_wrapper">
            <h1 style="color: white;">実験用リンク</h1>
            <div class="research_items">
                <div class="research_item">
                    <a href="">動画１</a>
                </div>
                <div class="research_item">
                    <a href="">動画２</a>
                </div>
                <div class="research_item">
                    <a href="https://docs.google.com/forms/d/e/1FAIpQLScDfsFRKLGLBAMaokk8dte9ai36PEZqzJ-2UxHkP_Wgkno2ug/viewform?usp=sf_link" target="_blank">アンケート</a>
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
    height: 100vh;
  }
  .research_wrapper{
    width: 60%;
    margin: 20px auto;
  }
  .research_items{
    padding: 20px;
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
</style>

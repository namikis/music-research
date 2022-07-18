<template>
  <div class="wrapper">
    <Header />
    <CommonModal 
      v-if="$store.state.modal.isShowModal"
      :mode="'pass'"
      @updateState="updateSysState"
    />
    <div class="research_container">
        <div class="research_wrapper">
            <h1 style="color: white;">実験用資料</h1>
            <p style="color: white">使用システム：　
              <span v-if="sys_state == 'f'">FUSION MUSIC</span>
              <span v-else-if="sys_state == 's'">Spotify</span>
              <span v-else-if="sys_state == 'a'">管理用</span>
              <span v-else>権限なし</span>
              <button v-if="sys_state == 's' || sys_state == 'f'" class="sys_update_button" @click="openPassModal">変更</button>
            </p>
            <div class="research_items">
                <div class="research_item">
                  <h1>リンク</h1>
                  <div class="research_links">
                    <a href="https://docs.google.com/forms/d/e/1FAIpQLScDfsFRKLGLBAMaokk8dte9ai36PEZqzJ-2UxHkP_Wgkno2ug/viewform?usp=sf_link" target="_blank">アンケート</a>
                    <a href="https://open.spotify.com/" target="_blank">Spotify</a>
                  </div>
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
                <div class="research_item" v-if="sys_state == 's' || sys_state == 'a'">
                  <h1>動画１（Spotify）</h1>
                  <div class="research_video">
                    <video controls width="100%">
                      <source src="/research/Spotify.mp4" type="video/mp4">
                      Sorry, your browser doesn't support embedded videos.
                    </video>
                  </div>
                </div>
                <div class="research_item" v-if="sys_state == 'f' || sys_state == 'a'">
                  <h1>動画２（FUSION MUSIC）</h1>
                  <div class="research_video">
                    <video controls width="100%">
                      <source src="/research/FUSIONMUSIC.mp4" type="video/mp4">
                      Sorry, your browser doesn't support embedded videos.
                    </video>
                  </div>
                </div>
               <div class="research_item">
                  <h1>注意事項</h1>
                  <div class="attention_item" v-if="sys_state == 's' || sys_state == 'a'">
                    <p>・時間は無制限です。</p>
                    <p>・使い方動画は後から自由に見直して大丈夫です。</p>
                    <p>・お気に入り曲は知っている曲・知らない曲どちらでも問題ありません。</p> 
                    <p>・お気に入り曲はソングラジオ内の曲から選択してください。</p>
                    <p>・Spotify使用時は画面録画をします。</p>
                    <p></p>
                  </div>
                  <div class="attention_item" v-else-if="sys_state == 'f' || sys_state == 'a'">
                    <p>・時間は無制限です。</p>
                    <p>・使い方動画は後から自由に見直して大丈夫です。</p>
                    <p>・お気に入り曲は知っている曲・知らない曲どちらでも問題ありません。</p>
                    <p>・お気に入り曲は検索結果からではなく、フュージョンで提示された曲から選択してください。</p>
                  </div>
                </div>
            </div>
            
        </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import $cookies from "cookie-universal-nuxt"
import CommonModal from '~/components/CommonModal.vue'

export default Vue.extend({
    name: "ResearchPage",
    data() {
        return {
            open_state: 1,
            sys_state: ""
        };
    },
    mounted() {
        this.sys_state = this.$cookies.get("state");
        console.log(this.sys_state);
    },
    methods: {
        changeState() {
            this.open_state *= -1;
        },
        updateSysState() {
            let next_state = "none";
            if (this.sys_state == "f") {
                next_state = "s";
            }
            else if (this.sys_state == "s") {
                next_state = "f";
            }
            this.$cookies.set("state", next_state);
            this.sys_state = next_state;
        },
        openPassModal() {
            this.$store.commit("modal/openModal")
        }
    },
    components: { CommonModal }
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
  .research_video {
    width: 90%;
    margin: 0 auto;
    text-align: center;
  }
  .state_icon{
    color: black;
    cursor: pointer;
  }
  .research_links{
    padding: 10px;
  }
  .sys_update_button{
    margin: 0 5px; 
    font-size:12px;
  }
  .attention_item{
    background: white;
    padding: 10px 20px;
    margin: 10px auto;
    width: 95%;
    border-radius: 10px;
    font-weight: bold;
    font-size: 22px;
  }
</style>

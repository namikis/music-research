<template>
  <div class="research_intro_wrapper"> 
      <div class="message_wrapper">
          <div class="message_item">
              <h2 class="intro_title">実験概要</h2>
              <div class="message_field">
                  <p>・「Spotify」「FUSION MUSIC」の二つのシステムを使用し、気に入った曲をそれぞれ三曲ずつ見つける（メモしておく）</p>
                  <p>・時間は無制限</p>
                  <p>・知っている曲・知らない曲どちらでも良い</p>
                  <p class="message_accent">・Spotify使用時は画面録画をする</p>
                  <p class="message_accent">・検索結果からではなく提案内容から曲を選択する</p>
              </div>
          </div>
          <div class="message_item">
              <h2 class="intro_title">実験の流れ</h2>
              <div class="message_field">
                  <p>
                    １．使い方説明用動画①<br>
                    ２．システム①を自由に使用してお気に入り曲三つを決定する<br>
                    ３．アンケート①<br>
                  </p>
                  <p>
                    ４．使い方説明用動画②<br>
                    ５．システム②を自由に使用してお気に入り曲三つを決定する<br>
                    ６．アンケート②
                  </p>
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
    .message_accent{
        color: red;
    }
    .research_intro_wrapper{
        background: white;
        padding: 40px;
        border-radius: 10px;
    }
    .message_wrapper{
        width: 80%;
        margin: 0 auto;
    }
    .message_field{
        font-size:18px;
    }
    .intro_title{
        color: black !important;
    }
</style>
<!-- 実験概要
「Spotify」「FUSION MUSIC」の二つのシステムを使用し、気に入った曲をそれぞれ三曲見つける
時間は無制限
知っている曲・知らない曲どちらでも良い
Spotify使用時は画面録画をする
検索結果からではなく提案内容から曲を選択する

実験の流れ

使い方説明用動画①
システムの概要と使い方
システム①
システムを自由に使用してお気に入り曲を三つ決定する（メモしておく）
アンケート①

使い方説明用動画②
システムの概要と使い方
システム②
システムを自由に使用してお気に入り曲を三つ決定する（メモしておく）
アンケート② -->


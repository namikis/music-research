<template>
    <div class="search_wrapper">
        <div class="search_type_wrapper">
            <span><input type="radio" name="search_type" v-model="search_type" value="artist" checked>アーティスト</span>
            <span><input type="radio" name="search_type" v-model="search_type" value="song">楽曲</span>
        </div>
        <input class="search_window" type="text" @keypress.enter="onSubmit" v-model="search_name" placeholder="アーティスト名" v-if="search_type=='artist'">
        <input class="search_window" type="text" @keypress.enter="onSubmit" v-model="search_name" placeholder="楽曲名" v-else-if="search_type=='song'">
        <button @click="onSubmit">search</button>
        <button @click="clearSearch">clear</button>
    </div>
</template>
<script lang="ts">
import Vue from 'vue'
import axios from 'axios'
import $cookies from "cookie-universal-nuxt"

export default Vue.extend({
    data(){
        return {
            search_name: "" as string,
            search_type: "artist" as string
        }
    },  
    methods: {
        onSubmit(){
            if(this.search_type == "artist"){
                this.$emit("searchArtist", this.search_name)
            }else if(this.search_type == "song"){
                this.$emit("searchSong", this.search_name)
            }
            const url = "http://localhost:5000/logs/search"
            let params = new URLSearchParams()
            params.append("search_word", this.search_name)
            params.append("search_type", this.search_type)
            params.append("user_name", this.$cookies.get("user_name"))
            axios.post(url, params).then((response) => {
                console.log(response.data)
            })
        },
        clearSearch(){
            this.search_name = ""
            this.search_type = "artist"
            this.onSubmit()
        }
    }
})
</script>
<style>
    .search_window{
        width: 60%;
    }
    .search_type_wrapper{
        color: white;
    }
    .search_wrapper{
        margin-left: 15px;
    }
    
</style>

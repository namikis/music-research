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
export default Vue.extend({
    data(){
        return {
            search_name: "" as String,
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

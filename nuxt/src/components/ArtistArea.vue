<template>
    <div class="artist_area_wrapper">
        <div class="artist_field">
            <SearchArea 
                @searchArtist="searchArtist"
            />
            <div class="artist_items">
                <div class="artist_item" v-for="artist_name in artist_name_list" :key="artist_name.artist_name">
                    <span @click="selectedArtist(artist_name.artist_name)">{{ artist_name.artist_name }}</span>
                </div>
            </div>
        </div>
        
    </div>
</template>
<script lang="ts">
import Vue from 'vue'
import axios from 'axios'
type Artists = {
    artist_name: String
}
export default Vue.extend({
    props: {
        selected_artist_name:{
            type: String,
            default: ""
        }
    },
    data(){
        return{
            artist_name_list: [] as Array<Artists>,
            clone_artist_name_list: [] as Array<Artists>,
        }
    },
    mounted(){
        this.getAllAtristsName()
    },
    methods: {
        selectedArtist(artist_name: String){
            this.$emit("update:selected_artist_name", artist_name)
        },
        searchArtist(search_name: String){
            console.log(this.clone_artist_name_list)
            this.artist_name_list = this.clone_artist_name_list.slice()
            // TODO:SpotifyAPIにsearchして日本語のアーティスト名を取得する
            if(search_name !== ""){
                this.artist_name_list = this.artist_name_list.filter(artist_name => artist_name.artist_name == search_name)
            }
        },
        getAllAtristsName(){
            const url = "http://localhost:5000/artists"
            axios.get(url).then((response) => {
                this.artist_name_list = response.data
                this.clone_artist_name_list = this.artist_name_list.slice()
            })
        }
    }
})
</script>
<style>
    .artist_area_wrapper{
        padding:10px;
        background: lightblue;
        height:100vh;
        width: 30%;
        overflow: scroll;
    }
    .artist_field{
        width: 85%;
        margin: 20px auto;
    }
    .artist_items{
        width: 90%;
        margin: 40px auto;
        background: white;
        padding: 20px;
    }
    .artist_item{
        border: 1px solid black;
        padding: 5px;
        margin:10px 0;
    }
</style>

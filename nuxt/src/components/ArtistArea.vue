<template>
    <div class="artist_area_wrapper">
        <div class="artist_field">
            <SearchArea 
                @searchArtist="searchArtist"
                @searchSong="searchSong"
            />
            <div class="artist_items">
                <div class="artist_item" v-for="artist_name in artist_name_list" :key="artist_name.artist_name" @click="selectedArtist(artist_name.artist_name)">
                    <span>{{ artist_name.artist_name }}</span>
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
        searchArtist(search_name: string){
            this.artist_name_list = this.clone_artist_name_list.slice()
            
            if(search_name !== ""){
                const url = "http://localhost:5000/artists/formal_name"
                const params = new URLSearchParams()
                params.append('search_name', search_name)
                let formal_name_list: String[] = []
                axios.post(url, params).then((response) => {
                    formal_name_list = response.data
                    console.log(formal_name_list)
                    this.artist_name_list = this.artist_name_list.filter(artist_name => formal_name_list.includes(artist_name.artist_name))
                }).catch(error => {
                    console.log("Not Found")
                    formal_name_list = [search_name]
                    this.artist_name_list = this.artist_name_list.filter(artist_name => formal_name_list.includes(artist_name.artist_name))
                })
            }
        },
        searchSong(search_name: string){
            this.$emit("update:selected_artist_name", "SONGS: " + search_name)
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
        background: black;
        opacity: 0.9;
        width: 30%;
        border-right: 0.8px solid gray;
        height: 92vh;
    }
    .artist_field{
        width: 85%;
        margin: 20px auto;
    }
    .artist_items{
        width: 90%;
        margin: 20px auto;
        background: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        opacity: 0.9;
        height: 76vh;
        overflow-y: scroll;
    }
    .artist_item{
        border: 1px solid black;
        padding: 5px;
        margin:5px 0;
        background: black;
        color: white;
        cursor: pointer;
        border-radius: 10px;
        opacity: 0.9;
    }
    .artist_item:hover{
        opacity: 0.8;
    }
</style>

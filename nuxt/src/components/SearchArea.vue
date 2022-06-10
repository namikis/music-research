<template>
    <div class="search_wrapper">
        <input type="text" @keypress.enter="onSubmit" v-model="search_artist_name">
        <button @click="onSubmit">search</button>
        <button @click="clearSearch">clear</button>
    </div>
</template>
<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
    data(){
        return {
            search_artist_name: "" as String
        }
    },  
    methods: {
        onSubmit(){
            this.$emit("searchArtist", this.search_artist_name)
        },
        clearSearch(){
            this.search_artist_name = ""
            this.onSubmit()
        }
    }
})
</script>
<style>
    .search_wrapper input{
        width: 60%;
    }
</style>

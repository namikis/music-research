<template>
    <div class="header_wrapper">
        <div class="header_logo">
            <h2>FUSION MUSIC</h2>
        </div>
        <div class="header_right_wrapper">
             <div class="question_wrapper">
                <a href="https://docs.google.com/forms/d/e/1FAIpQLScDfsFRKLGLBAMaokk8dte9ai36PEZqzJ-2UxHkP_Wgkno2ug/viewform?usp=sf_link" target="_blank">アンケート</a>
            </div>
            <div class="name_input_wrapper">
                <div v-if="user_name == ''">
                    <input type="text" v-model="target_user_name">
                    <span @click="setUserName">set</span>
                </div>
                <div v-else>
                    {{ user_name }}
                    <span @click="deleteUserName">edit</span>                
                </div>
            </div>
        </div>
       
    </div>
</template>

<script lang="ts">
import Vue from 'vue'
import $cookies from "cookie-universal-nuxt"

export default Vue.extend({
    data(){
        return {
            user_name: "",
            target_user_name: "",
        }
    },
    mounted(){
        if(!this.$cookies.get("user_name")){
            this.$cookies.set("user_name", "")
        }else{
            this.user_name = this.$cookies.get("user_name")
        }
    },
    methods: {
        setUserName(){
            this.user_name = this.target_user_name
            this.$cookies.set("user_name", this.user_name)
            console.log(this.user_name)
        },
        deleteUserName(){
            this.user_name = ""
            this.$cookies.set("user_name", "")
        }
    }
})

</script>

<style>
    body, h1, h2{
        margin:0;
        padding:0;
    }
    .header_logo h2{
        padding:5px 20px;
        font-size:30px;
        background: black;
        color: #00DC82;
    }
    .header_wrapper{
        border-bottom: 1px solid rgba(0, 0, 0, 0.7);
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: black;
    }
    .name_input_wrapper{
        margin-right: 30px;
        color: white;
        font-size: 18px;
        font-weight: bold;
    }
    .name_input_wrapper span{
        background: white;
        padding: 5px;
        color: black;
        font-size: 14px;
        margin-left: 8px;
        cursor: pointer;
    }
    .name_input_wrapper span:hover{
        opacity: 0.9;
    }
    .header_right_wrapper{
        display: flex;
        align-items: center;
    }
    .question_wrapper{
        margin-right: 20px;
    }
    .question_wrapper:hover{
        opacity: 0.9;
    }
    .question_wrapper a{
        padding: 5px;
        background: white;
        text-decoration: none;
        font-weight: bold;
        color: black;
    }
</style>

<template>
    <div class="modal_wrapper">
        <div id="modal_content">
            <div class="pass_modal_wrapper" v-if="mode == 'pass'">
                <div class="pass_item">パスワード：</div>
                <div class="pass_item">
                    <input type="password" @keypress.enter="submitPass($event)" ref="focusInput">
                </div>
            </div>
        </div>
        <div id="modal_overlay"></div>
    </div>
</template>
<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
    props: ["mode"],
    mounted(){
        this.refs().focus()
    },  
    methods: {
        submitPass(event: any){
            const value = event.target.value
            if(value == process.env.AUTH_PASS){
                this.$emit("updateState")
            }else{
                alert('認証に失敗しました')
            }
            this.closeModal();
        },
        closeModal(){
            this.$store.commit("modal/closeModal")
        },
        refs(): any{
            return this.$refs.focusInput
        }
    }
})
</script>
<style>
    #modal_content{
        width:50%;
        margin:1.5em auto;
        padding:10px 20px;
        border:2px solid #aaa;
        background:#fff;
        z-index:3;
        position:fixed;
        right: 0;
        left: 0;
        top: 10%;
        min-height: 300px;
        border-radius: 10px;
    }

    #modal_overlay{
        z-index:2;
        position:fixed;
        top:0;
        left:0;
        width:100%;
        height:120%;
        background-color:rgba(0,0,0,0.75);
    }

    .pass_modal_wrapper{
        width: 100%;
        height: 300px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .pass_item, .pass_item input{
        font-size: 25px;
        font-weight: bold;
    }
</style>

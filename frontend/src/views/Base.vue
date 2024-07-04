<script setup lang="ts">
import {NButton,NFlex,NInput,NCard} from 'naive-ui'
import axiosInstance from '@/axios/axiosInstance'
import {ref} from 'vue'

const value = ref('')

function send(){
    axiosInstance.post('/api/submit',{
        message:value.value
    }).then(function (response){
        console.log(response)
    }).catch(function(error){
        console.log(error)
    })
    value.value = ''
}


 const message_from_test = ref('')
function test(){
     const source = new EventSource('/api/test')
     source.onopen = (e) => console('connection opened')
     source.onerror = (e) => console('conection failed')
     // source.message = (e) =>
 }


 // function test(){
 //      axiosInstance.post('/api/test',{
 //          message:'hello world'
 //      }).then(function (response){
 //          console.log(response)
 //      }).catch(function(error){
 //          console.log(error)
 //      })
 //      message_from_test.value = ''
 //  }



</script>

<template>
<div>
<n-flex class="base">
    <n-flex class="left" vertical>
        <n-button type="primary">连接大模型</n-button>
        <n-button type="primary">连接UE5</n-button>
        <n-card class="left_messageFrame" title="信息框"></n-card>
    </n-flex>
    <n-flex class="right" vertical>
        <n-card class="right_chatFrame" title="聊天框"></n-card>
        <n-flex class="right_down">
            <n-input class="right_down_input" type="text" v-model:value="value"/>
            <n-button type="primary" @click="send">发送</n-button>
        </n-flex>
    </n-flex>
</n-flex>

<n-button type="primary" @click='test'>test</n-button>
<p>{{message_from_test}}</p>

</div>
</template>

<style scoped>
.base{
    width: 100%;
    margin-top: 10em;
    margin-bottom: 10em;
}
.left{
    width: 20em;
}

.left_messageFrame{
    height: 62em;
}

.right{
    width: 60em;
}
.right_chatFrame{
    width:60em;
    height: 65em;
}
.right_down_input{
    width:55.2em
}
</style>

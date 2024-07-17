<script setup lang="ts">
import {NButton,NFlex,NInput,NCard} from 'naive-ui'
import axiosInstance from '@/axios/axiosInstance'
import {ref,computed} from 'vue'
import ChatFrame from '@/components/ChatFrame.vue'
import Configuration from '@/components/Configuration.vue'

const value = ref('')
const c_llm = ref('连接大模型')


const disabled = computed(()=>{
     return c_llm.value=='已连接' ? true : false
 })

function send(){
    axiosInstance.post('/api/submit',{
        message:value.value
    }).then(function(response){
        console.log(response)
    }).catch(function(error){
        console.log(error)
    })
    value.value = ''
}

function connect_llm(){
     axiosInstance.get('/api/connect')
     .then(function(response){
         console.log(response)
         c_llm.value = '已连接'
     }).catch(function(error){
         console.log(error)
     })
 }


</script>

<template>
    <div>
        <n-flex class="base">
            <n-flex class="left" vertical>
                <n-button type="primary" @click='connect_llm' :disabled=disabled>{{c_llm}}</n-button>
                <n-button type="primary">连接UE5</n-button>
                <Configuration/>
            </n-flex>
            <ChatFrame />
        </n-flex>
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

</style>

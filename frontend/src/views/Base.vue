<script setup lang="ts">
import {NButton,NFlex,NInput,NCard} from 'naive-ui'
import axiosInstance from '@/axios/axiosInstance'
import {ref} from 'vue'
import ChatFrame from '@/components/ChatFrame.vue'
import Configuration from '@/components/Configuration.vue'

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




</script>

<template>
    <div>
        <n-flex class="base">
            <n-flex class="left" vertical>
                <n-button type="primary">连接大模型</n-button>
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

<script setup lang='ts'>
import { ref, watchEffect, onMounted, nextTick,computed } from 'vue'
import { NLog, LogInst, NButton,NCard,NFlex,NInput,NDivider } from 'naive-ui'
import axiosInstance from '@/axios/axiosInstance.ts'

const log = ref('')
const logInst = ref<LogInst | null>(null)
const fontSize = ref(15)
const input_value = ref(null)

const jug =  defineProps(['jug_connect'])

const disabled = computed(()=>{
     return jug.jug_connect =='已连接'? false : true
 })


function sendMessage() {
    axiosInstance.post('/api/chat', {
        frontendMessage: input_value.value
    }).then((val) => {
        console.log(val)
    }).catch((err) => {
        console.log(err)
    })
    //input_value.value = null
}

onMounted(() => {
    console.log("mounted")
    const source = new EventSource('/api/chat/listen')
    source.onopen = (e) => console.log('Connection opened')
    source.onmessage = (e) => {
        log.value += e.data
    }
    watchEffect(() => {
        if (log.value) {
            nextTick(() => {
                logInst.value?.scrollTo({ position: 'bottom', silent: true })
            })
        }
    })
})
</script>



<template>
    <n-flex class="main" vertical>
        <n-card class="chatFrame">
            <n-divider title-placement="right" class='chatFrame_title'>
                <n-card class='chatFrame_title_card'><span class="chatFrame_title_txt">虚拟数字人对话框</span></n-card>
            </n-divider>
            <n-log ref="logInst" :log="log" :font-size="fontSize" :rows="25" />
        </n-card>
        <n-flex>
            <n-input class="input" type="text" placeholder="请输入" v-model:value="input_value" />
            <n-button type='primary' @click="sendMessage" :disabled="disabled">发送</n-button>
        </n-flex>
    </n-flex>
</template>



<style scoped>
.chatFrame {
    width: 60em;
    height: 65em;
   }

.chatFrame_title {
    margin-top: 0;
    margin-bottom: 0;
}

.chatFrame_title_txt {
    font-size: 1.5em;
    color: green;
    font-weight: 700;
}

 .main {
    width: 60em;
}

.input {
    width: 55.2em
}
</style>

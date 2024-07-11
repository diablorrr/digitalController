<script setup lang='ts'>
import { ref, watchEffect, onMounted, nextTick } from 'vue'
import { NLog, LogInst, NButton,NCard,NFlex,NInput,NDivider } from 'naive-ui'
import axiosInstance from '@/axios/axiosInstance.ts'

const log = ref('')
const logInst = ref<LogInst | null>(null)
const fontSize = ref(25)

function sendMessage() {
    axiosInstance.post('/api/chat', {
    }).then((val) => {
        console.log(val)
    }).catch((err) => {
        console.log(err)
    })
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
            <n-log ref="logInst" :log="log" :font-size="fontSize" :rows="5" />
        </n-card>
        <n-flex>
            <n-input class="input" type="text" placeholder="请输入" />
            <n-button type='primary' @click="sendMessage">发送</n-button>
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

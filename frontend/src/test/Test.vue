<script setup lang='ts'>
import {ref,watchEffect,onMounted,nextTick} from 'vue'
import {NLog,LogInst,NButton} from 'naive-ui'
import axiosInstance from '../axios/axiosInstance.ts'

const log = ref('sfsldfj')
const logInst = ref<LogInst|null>(null)

function getlog_do(){
     console.log(123)
     log.value = ''
     const source = new EventSource('/api/test/listen')
     console.log(source)
     source.onopen = (e) => console.log('Connection opened')
     source.onerror = (e) => console.log('Error:',e)
     source.onmessage = (e) => {
         console.log(e)
         if(e.data === '[DONE]') source.close()
         else log.value += e.data + '\n'
     }
 }

function getLog(){
     axiosInstance.post('/api/test',{
     }).then((val)=>{
         console.log(val)
     }).catch((err)=>{
         console.log(err)
     })
    // setTimeout(function(){
    //     getlog_do()
    // },1000)
 }



onMounted(()=>{
     watchEffect(()=>{
         if(log.value){
             nextTick(()=>{
               logInst.value?.scrollTo({position:'bottom',silent:true})
             })
         }
     })
 })

</script>

<template>
    <n-log ref="logInst" :log="log" />
    <n-button type='primary' @click="getlog_do">listen</n-button>
    <n-button type='primary' @click="getLog">create data</n-button>
</template>

<style scoped>

</style>

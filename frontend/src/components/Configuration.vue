<script setup lang='ts'>
import {NCard,NFlex,NButton,NSlider,NInputNumber,NDivider} from 'naive-ui'
import {ref} from 'vue'

const temperature = ref(0.5)
const top_p = ref(0.5)
const maximum_length = ref(2048)
</script>

<template>
    <n-card class="configuration" title='模型配置'>
        <n-flex>
            <n-button type='warning' class="clear">清除历史记录</n-button>
            <n-divider />
            <n-card title='Temperature'>
                <n-slider v-model:value="temperature" :step="0.1" :max="1" :min="0"></n-slider>
                <br />
                <n-input-number v-model:value="temperature" size="small"></n-input-number>
            </n-card>
            <br />
            <n-card title='Top P'>
                <n-slider v-model:value="top_p" :step="0.1" :max="1" :min="0"></n-slider>
                <br />
                <n-input-number v-model:value="top_p" size="small"></n-input-number>
            </n-card>
            <br />
            <n-card title='Maximum length'>
                <n-slider v-model:value="maximum_length" :step="128" :max="4096" :min="0"></n-slider>
                <br />
                <n-input-number v-model:value="maximum_length" size="small"></n-input-number>
            </n-card>
            <br />
            <n-button type='primary' class="confirm">确定配置</n-button>
        </n-flex>
    </n-card>
</template>

<style scoped>
 .clear{
    width: 18em;
    height: 4em;

 }
 .configuration{
     width:21.5em;
    height: 62em;
 }
 .confirm{
     width:18em;
 }
</style>

<template>
  <div>
    <ParentChild
      @update-name="updateName"
      @some-event="someCallback"
      @emit-args="getNumbers"
      my-msg="message"
      :dynamic-props="name"
    />
  </div>
</template>

<script setup>
import ParentChild from '@/components/ParentChild.vue'
import { ref } from 'vue'

const name = ref('Alice')
const someCallback = function () {
  console.log('ParentChild가 발신한 이벤트를 수신했어요.')
}
const getNumbers = function (...args) {
  console.log(args)
  console.log(`ParentChild가 전달한 추가인자 ${args}를 수신했어요.`)
}
const updateName = function () {
  name.value = 'Bella'
}
</script>

<style scoped>

</style>
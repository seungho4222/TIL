<template>
  <div>
    <p @click="goBack">← 뒤로가기</p>
    <h1>내가 좋아하는 채널</h1>
    <div v-if="channelList">
      <div v-for="channel in channelList" :key="channel.id">
        <ul class="d-flex">
          <li>
            <h2><strong>{{ channel.snippet.channelTitle }}</strong></h2>
          </li>
          <button class="btn btn-danger btn-sm ms-3" @click="removeChannel(channel)">채널 삭제</button>
        </ul>
      </div>
    </div>
    <div v-else>
      <strong>채널 없음</strong>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const channelList = ref(null)

channelList.value = JSON.parse(localStorage.getItem('channel'))

const removeChannel = (video) => {
  const itemIdx = channelList.value.findIndex((item) => item.id === video.id)
  channelList.value.splice(itemIdx, 1)
  localStorage.setItem('channel', JSON.stringify(channelList.value))
}

const goBack = () => {
  router.go(-1)
}

</script>

<style scoped>

</style>
<template>
  <div>
    <p @click="goBack">← 뒤로가기</p>
    <h2>비디오 검색</h2>
    <form @submit.prevent="searchData" class="d-flex mb-3">
      <input type="text" class="form-control me-3" placeholder="검색어를 입력하세요." v-model="inputData">
      <button class="btn btn-success nowrap">찾기</button>
    </form>
    <div class="video-list d-flex flex-wrap">
      <div v-for="video in videoList" :key="video.id" class="video rounded">
        <img :src="video.snippet.thumbnails.medium.url" alt="" @click.prevent="goDetail(video)">
        <div class="m-2">{{ video.snippet.title }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()

const myURL = 'https://www.googleapis.com/youtube/v3/search'
const myKey = import.meta.env.VITE_APP_KEY
const inputData = ref('')

const videoList = ref([])

const searchData = () => {
  axios.get(myURL, {
    params: {
      key: myKey,
      part: 'snippet',
      type: 'video',
      q: inputData.value,
    }
  }).then(res => {
    videoList.value = res.data.items
    console.log(videoList.value)
    inputData.value = ''
  }).catch(err => {
    console.log('No Search')
  })
}

const goBack = () => {
  router.go(-1)
}

const goDetail = (video) => {
  router.push(`/${video.id.videoId}`)
}

</script>

<style scoped>
.nowrap {
  white-space: nowrap;
}

.video-list {
  margin: 10px auto;
  gap: 30px;
}

.video {
  border: 1px solid rgba(128, 128, 128, 0.5);
  width: 30%;
}
img {
  width: 100%;
}
</style>
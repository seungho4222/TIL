<template>
  <div v-if="video">
    <p @click="goBack">← 뒤로가기</p>
    <h1>{{ video.snippet.title }}</h1>
    <p>업로드 날짜 : {{ video.snippet.publishedAt.slice(0, 10) }}</p>
    <iframe width="640" height="360" :src="`https://www.youtube.com/embed/${videoId}`"
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    <p>{{ video.snippet.description }}</p>
    <button class="btn btn-primary me-3" @click.prevent="saveVideo(video)">동영상 저장</button>
    <button class="btn btn-warning" @click.prevent="addChannel(video)">채널 저장</button>
    <!-- <button v-if="isDuplicate" 
    class="btn btn-primary me-3" 
    @click.prevent="saveVideo(video)">
    동영상 저장 취소</button>
    <button v-else 
    class="btn btn-danger me-3"  
    @click.prevent="removeVideo(video)"
    >동영상 저장
    </button> -->
  </div>
  <div v-else>
    <strong>Loading...</strong>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()

const myURL = 'https://www.googleapis.com/youtube/v3/videos'
const myKey = import.meta.env.VITE_APP_KEY

const video = ref('')
const videoId = route.params.videoId

axios.get(myURL, {
  params: {
    key: myKey,
    part: 'snippet',
    id: videoId,
  }
}).then(res => {
  video.value = res.data.items[0]
  console.log(video.value)
}).catch(err => {
  console.log('No Search')
})

const goBack = () => {
  router.go(-1)
}

const savevideoContent = ref(false)

// 나중에 볼 영상
const saveVideo = (video) => {
  const box = JSON.parse(localStorage.getItem('later')) || []
  
  // 중복된 제품이 있는지 확인
  const isDuplicate = box.length > 0 && box.find((item) => item.id === video.id)

  // 중복이 아니라면 추가
  if(!isDuplicate) {
    alert('나중에 볼 영상에 추가합니다')
    box.push(video)
    savevideoContent.value = true
  } else {
    alert('이미 있는 영상입니다.')
    box.value.splice(itemIdx, 1)
    savevideoContent.value = false
  }

  // 수정된 카트 데이터를 localStorage 에 저장
  localStorage.setItem('later', JSON.stringify(box))

  router.push('/later')
}


// 좋아하는 채널 저장
const addChannel = (video) => {
  const channelList = JSON.parse(localStorage.getItem('channel')) || []

  // 중복된 제품이 있는지 확인
  const isDuplicate = channelList.length > 0 && channelList.find((item) => item.id === video.id)

  // 중복이 아니라면 추가
  if(!isDuplicate) {
    alert('채널을 등록합니다.')
    channelList.push(video)
  } else {
    alert('이미 있는 채널입니다.')
  }

  // 수정된 카트 데이터를 localStorage 에 저장
  localStorage.setItem('channel', JSON.stringify(channelList))

  router.push('/channel')
}

// const removeVideo = (video) => {
//   const itemIdx = box.value.findIndex((item) => item.id === video.id)
//   box.value.splice(itemIdx, 1)
//   localStorage.setItem('later', JSON.stringify(box.value))
// }

</script>

<style scoped>
p {
  color: gray
}
</style>
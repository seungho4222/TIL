<template>
  <div>
    <p @click="goBack">← 뒤로가기</p>
    <h1>나중에 볼 동영상</h1>
    <div v-if="videoList" class="video-list d-flex flex-wrap">
      <div v-for="video in videoList" :key="video.id" class="video rounded">
        <img :src="video.snippet.thumbnails.medium.url" alt="">
        <div class="m-2">{{ video.snippet.title }}</div>
        <div>
          <button @click="goDetail(video)" class="btn btn-primary mx-3">Detail</button>
          <button @click="removeVideo(video)" class="btn btn-danger">동영상 삭제</button>
        </div>
      </div>
    </div>
    <div v-else>
      <strong>비디오 없음</strong>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const videoList = ref(null)

videoList.value = JSON.parse(localStorage.getItem('later'))

const goDetail = (video) => {
  router.push(`/${video.id}`)
}

const removeVideo = (video) => {
  const itemIdx = videoList.value.findIndex((item) => item.id === video.id)
  videoList.value.splice(itemIdx, 1)
  localStorage.setItem('later', JSON.stringify(videoList.value))
}

const goBack = () => {
  router.go(-1)
}

</script>

<style scoped>
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
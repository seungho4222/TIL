<template>
  <div>
    <h1>상세 페이지</h1>
    <div v-if="product" class="product-card">
      <img :src="product.image" alt="">
      <strong>{{ product.title }}</strong>
      <p>가격 : ${{ product.price }}</p>
      <button @click="addCart(product)">장바구니에 추가</button>
    </div>
    <div v-else>
      <strong>로딩중...</strong>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const product = ref('')
const productId = route.params.productId
const storeURL = `https://fakestoreapi.com/products/${productId}`

axios.get(storeURL)
  .then((response) => {
    // console.log(response.data)
    product.value = response.data
  }).catch((error) => {
    confirm.log(error)
  })

  const addCart = (product) => {

  const existingCart = JSON.parse(localStorage.getItem('cart')) || []

  const isDuplicate = existingCart.length > 0 && existingCart.find((item) => item.id === product.id)

  if(!isDuplicate){
    alert('장바구니에 추가합니다')
    existingCart.push(product)
  } else {
    alert('이미 있는 상품입니다. 장바구니로 이동합니다.')
  }

  localStorage.setItem('cart', JSON.stringify(existingCart))

  router.push('/cart')
}
</script>

<style scoped>

</style>
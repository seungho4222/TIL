<template>
  <div>
    <h1>장바구니</h1>
    <div v-if="cartItems">
      <div v-for="product in cartItems" :key="product.id" class="product-card">
        <img :src="product.image" alt="">
        <strong>{{ product.title }}</strong>
        <p>가격 : ${{ product.price }}</p>
        <button @click="goDetail(product)">상세페이지로 이동</button>
        <button @click="removeCart(product)">장바구니에서 제거</button>
      </div>
    </div>
    <div v-else>
      <strong>장바구니에 담긴 상품이 없습니다.</strong>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const cartItems = ref(null)

cartItems.value = JSON.parse(localStorage.getItem('cart'))

const goDetail = (product) => {
  router.push(`/${product.id}`)
}

const removeCart = (product) => {
  // localStorage 에서 삭제
  // 현재 cartItems.value 에서 삭제
  // 1. 현재 localStorage 에 저장된 데이터 가져오기
  // const existingCart = JSON.parse(localStorage.getItem('cart'))

  // 2. 삭제할 아이템 index 검색
  const itemIdx = cartItems.value.findIndex((item) => item.id === product.id)

  // 3. 데이터 삭제
  cartItems.value.splice(itemIdx, 1)

  // 4. 삭제된 데이터 기준으로 데이터 반영
  localStorage.setItem('cart', JSON.stringify(cartItems.value))
}

</script>

<style scoped>

</style>
<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <nav class="navbar navbar-expand-lg bg-dark">
    <a class="navbar-brand disabled ms-3 text-light" href="">
      Mytube
    </a>
    <button class="navbar-toggler bg-secondary" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item active text-dark">
          <RouterLink :to="{ name: 'home' }">Home</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink :to="{ name: 'search' }">Search</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink :to="{ name: 'later' }">Later</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink :to="{ name: 'channel' }">Channel</RouterLink>
        </li>
      </ul>
    </div>
  </nav>
  
  <div class="container mt-3">
    <RouterView />
  </div>
</template>

<style scoped>
a {
  text-decoration: none;
  color: gray;
}
.navbar-nav {
  gap: 10px;
}
</style>

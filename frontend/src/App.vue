<template>
  <div class="container">
    <header
      class="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3 mb-4 border-bottom"
    >
      <a
        href="/"
        class="fw-bold text d-flex align-items-center col-md-3 mb-2 mb-md-0 text-dark text-decoration-none"
      >
        Address Book
      </a>

      <ul class="nav col-12 col-md-auto mb-2 text-center text-md-end mb-md-0">
        <li>
          <RouterLink to="/" class="nav-link px-2 link-dark"
            >Contacts</RouterLink
          >
        </li>
        <li>
          <RouterLink to="/create" class="nav-link px-2 link-dark"
            >New Contact</RouterLink
          >
        </li>
      </ul>
    </header>

    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
import HelloWorld from "@/components/HelloWorld.vue";
</script>

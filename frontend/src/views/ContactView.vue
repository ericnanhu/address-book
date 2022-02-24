<template>
  <div class="p-5 mb-4 bg-light rounded-3">
    <div class="container-fluid py-5 d-grid gap-3">
      <img src="/dbguJcWc_400x400.jpeg" width="100" height="100" />
      <ul class="list-group">
        <li class="list-group-item">First Name: <span>Eric</span></li>
        <li class="list-group-item">Last Name: <span>Hu</span></li>
        <li class="list-group-item">Email: <span>example@example.com</span></li>
        <li class="list-group-item">Phone: <span>123456789</span></li>
      </ul>
      <RouterLink to="/update">
        <button type="button" class="btn btn-outline-primary">Update</button>
      </RouterLink>
      <RouterLink to="/delete">
        <button type="button" class="btn btn-outline-danger">Delete</button>
      </RouterLink>
    </div>
  </div>
</template>

<script></script>

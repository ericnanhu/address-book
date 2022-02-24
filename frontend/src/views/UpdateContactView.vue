<template>
  <h2>Update the Contact</h2>
  <form>
    <div class="mb-3">
      <label for="firstNameInput" class="form-label">First Name</label>
      <input type="text" class="form-control" id="firstNameInput" />
    </div>
    <div class="mb-3">
      <label for="lastNameInput" class="form-label">Last Name</label>
      <input type="text" class="form-control" id="lastNameInput" />
    </div>
    <div class="mb-3">
      <label for="emailInput" class="form-label">Email address</label>
      <input
        type="email"
        class="form-control"
        id="emailInput"
        aria-describedby="emailHelp"
      />
      <div id="emailHelp" class="form-text">
        We'll never share your email with anyone else.
      </div>
    </div>
    <div class="mb-3">
      <label for="phoneInput" class="form-label">Phone Number</label>
      <input type="tel" class="form-control" id="phoneInput" />
    </div>
    <div class="mb-3">
      <label for="imageInput" class="form-label">Image</label>
      <input class="form-control" type="file" id="imageInput" />
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
</template>

<script></script>

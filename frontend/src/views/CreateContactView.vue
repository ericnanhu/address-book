<template>
  <h2>Create a New Contact</h2>
  <form
    action="POST"
    enctype="multipart/form-data"
    @submit.prevent="createContact"
  >
    <div class="mb-3">
      <label for="firstNameInput" class="form-label">First Name</label>
      <input
        type="text"
        class="form-control"
        id="firstNameInput"
        v-model="this.contactDetails.firstName"
      />
    </div>
    <div class="mb-3">
      <label for="lastNameInput" class="form-label">Last Name</label>
      <input
        type="text"
        class="form-control"
        id="lastNameInput"
        v-model="this.contactDetails.lastName"
      />
    </div>
    <div class="mb-3">
      <label for="emailInput" class="form-label">Email address</label>
      <input
        type="email"
        class="form-control"
        id="emailInput"
        aria-describedby="emailHelp"
        v-model="this.contactDetails.email"
      />
      <div id="emailHelp" class="form-text">
        We'll never share your email with anyone else.
      </div>
    </div>
    <div class="mb-3">
      <label for="phoneInput" class="form-label">Phone Number</label>
      <input
        type="tel"
        class="form-control"
        id="phoneInput"
        v-model="this.contactDetails.phone"
      />
    </div>
    <div class="mb-3">
      <label for="imageInput" class="form-label">Image</label>
      <input
        class="form-control"
        type="file"
        id="imageInput"
        @change="selectImage($event)"
      />
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
</template>

<script>
import { CREATE_CONTACT } from "@/mutations";

export default {
  data() {
    return {
      contactDetails: {
        firstName: "",
        lastName: "",
        email: "",
        phone: "",
        avatar: null,
      },
    };
  },

  methods: {
    selectImage(event) {
      this.contactDetails.image = event.target.files[0];
    },

    async createContact() {
      await this.$apollo
        .mutate({
          mutation: CREATE_CONTACT,
          variables: {
            firstName: this.contactDetails.firstName,
            lastName: this.contactDetails.lastName,
            email: this.contactDetails.email,
            phone: this.contactDetails.phone,
            image: this.contactDetails.image,
          },
        })
        .then(() => {
          this.$router.push("/");
        })
        .then(() => {
          this.$router.go();
        });
    },
  },
};
</script>

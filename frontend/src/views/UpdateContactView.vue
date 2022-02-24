<template>
  <h2>Update the Contact</h2>
  <form
    action="POST"
    enctype="multipart/form-data"
    @submit.prevent="updateContact"
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
import { CONTACT_BY_ID } from "@/queries";
import { UPDATE_CONTACT } from "@/mutations";

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

  async created() {
    const contact = await this.$apollo.query({
      query: CONTACT_BY_ID,
      variables: {
        id: this.$route.params.id,
      },
    });
    this.contactDetails.firstName = contact.data.contactById.firstName;
    this.contactDetails.lastName = contact.data.contactById.lastName;
    this.contactDetails.email = contact.data.contactById.email;
    this.contactDetails.phone = contact.data.contactById.phone;
    this.contactDetails.image = contact.data.contactById.image;
  },

  methods: {
    selectImage(event) {
      this.contactDetails.image = event.target.files[0];
    },

    async updateContact() {
      await this.$apollo
        .mutate({
          mutation: UPDATE_CONTACT,
          variables: {
            contactId: this.$route.params.id,
            firstName: this.contactDetails.firstName,
            lastName: this.contactDetails.lastName,
            email: this.contactDetails.email,
            phone: this.contactDetails.phone,
            image: this.contactDetails.image,
          },
        })
        .then(() => {
          this.$router.push(`/contact/${this.$route.params.id}`);
        });
    },
  },
};
</script>

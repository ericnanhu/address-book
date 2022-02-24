<template>
  <div class="p-5 mb-4 bg-light rounded-3">
    <div class="container-fluid py-5 d-grid gap-3">
      <img
        :src="`http://127.0.0.1:8000/media/${this.contact.image}`"
        width="100"
        height="100"
      />
      <ul class="list-group">
        <li class="list-group-item">
          First Name: <span>{{ this.contact.firstName }}</span>
        </li>
        <li class="list-group-item">
          Last Name: <span>{{ this.contact.lastName }}</span>
        </li>
        <li class="list-group-item">
          Email: <span>{{ this.contact.email }}</span>
        </li>
        <li class="list-group-item">
          Phone: <span>{{ this.contact.phone }}</span>
        </li>
      </ul>
      <RouterLink :to="`/update/${this.contact.id}`">
        <button type="button" class="btn btn-outline-primary">Update</button>
      </RouterLink>
      <RouterLink to="/delete">
        <button
          type="button"
          class="btn btn-outline-danger"
          @click="this.deleteContact()"
        >
          Delete
        </button>
      </RouterLink>
    </div>
  </div>
</template>

<script>
import { CONTACT_BY_ID } from "@/queries";
import { DELETE_CONTACT } from "@/mutations";

export default {
  data() {
    return {
      contact: {},
    };
  },

  async created() {
    const contact = await this.$apollo.query({
      query: CONTACT_BY_ID,
      variables: {
        id: this.$route.params.id,
      },
    });
    this.contact = contact.data.contactById;
  },

  methods: {
    async deleteContact() {
      await this.$apollo
        .mutate({
          mutation: DELETE_CONTACT,
          variables: {
            contactId: this.$route.params.id,
          },
        })
        .then(() => {
          this.$router.push("/delete");
        })
        .then(() => {
          this.$router.go();
        });
    },
  },
};
</script>

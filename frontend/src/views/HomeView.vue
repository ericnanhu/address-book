<template>
  <main>
    <ul class="list-group">
      <li
        class="list-group-item d-flex justify-content-between align-items-center"
        v-for="contact in this.contacts"
        :key="contact.id"
      >
        <span
          ><img
            :src="`http://127.0.0.1:8000/media/${contact.image}`"
            class="img-thumbnail"
            width="70"
            height="70"
        /></span>
        <span>{{ contact.firstName }} {{ contact.lastName }}</span>
        <span>
          <RouterLink :to="`/contact/${contact.id}`"
            ><button type="button" class="btn btn-outline-primary">
              View Details
            </button></RouterLink
          >
        </span>
      </li>
    </ul>
  </main>
</template>

<script>
import { ALL_CONTACTS } from "@/queries";

export default {
  data() {
    return {
      contacts: {},
    };
  },

  async created() {
    const contacts = await this.$apollo.query({
      query: ALL_CONTACTS,
    });
    this.contacts = contacts.data.allContacts;
  },

  methods: {},
};
</script>

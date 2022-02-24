<template>
  <main>
    <!-- search -->
    <form @submit.prevent="this.search()" class="d-flex mb-3">
      <input
        class="form-control me-2"
        type="search"
        placeholder="Search"
        aria-label="Search"
        v-model="this.searchText"
      />
      <button class="btn btn-outline-success" type="submit">Search</button>
    </form>

    <!-- Sort -->
    <form @change="this.sort()" class="mb-3">
      <div class="h3">Sort By:</div>
      <div class="form-check">
        <input
          class="form-check-input"
          type="radio"
          name="flexRadioDefault"
          id="sortByID"
          value="ID"
          v-model="this.sortMethod"
        />
        <label class="form-check-label" for="sortByID"> ID </label>
      </div>
      <div class="form-check">
        <input
          class="form-check-input"
          type="radio"
          name="flexRadioDefault"
          id="sortByFirstName"
          value="FirstName"
          v-model="this.sortMethod"
        />
        <label class="form-check-label" for="sortByFirstName">
          First Name
        </label>
      </div>
      <div class="form-check">
        <input
          class="form-check-input"
          type="radio"
          name="flexRadioDefault"
          id="sortByLastName"
          value="LastName"
          v-model="this.sortMethod"
        />
        <label class="form-check-label" for="sortByLastName"> Last Name </label>
      </div>
    </form>

    <ul class="list-group">
      <li
        class="list-group-item d-flex justify-content-between align-items-center"
        v-for="contact in this.updatedContacts"
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
      updatedContacts: {},
      sortMethod: "ID",
      searchText: "",
    };
  },

  async created() {
    const contacts = await this.$apollo.query({
      query: ALL_CONTACTS,
    });
    this.contacts = contacts.data.allContacts;
    this.updatedContacts = this.contacts;
  },

  methods: {
    sort() {
      const unsorted = this.contacts;
      let sorted = [];

      if (this.sortMethod == "ID") {
        Object.keys(unsorted)
          .sort(function (a, b) {
            if (unsorted[a].id < unsorted[b].id) {
              return -1;
            }
            if (unsorted[a].id > unsorted[b].id) {
              return 1;
            }
            return 0;
          })
          .forEach(function (key) {
            console.log(key);
            sorted.push(unsorted[key]);
          });
        this.updatedContacts = sorted;
      } else if (this.sortMethod == "FirstName") {
        Object.keys(unsorted)
          .sort(function (a, b) {
            if (unsorted[a].firstName < unsorted[b].firstName) {
              return -1;
            }
            if (unsorted[a].firstName > unsorted[b].firstName) {
              return 1;
            }
            return 0;
          })
          .forEach(function (key) {
            console.log(key);
            sorted.push(unsorted[key]);
          });
        this.updatedContacts = sorted;
      } else if (this.sortMethod == "LastName") {
        Object.keys(unsorted)
          .sort(function (a, b) {
            if (unsorted[a].lastName < unsorted[b].lastName) {
              return -1;
            }
            if (unsorted[a].lastName > unsorted[b].lastName) {
              return 1;
            }
            return 0;
          })
          .forEach(function (key) {
            console.log(key);
            sorted.push(unsorted[key]);
          });
        this.updatedContacts = sorted;
      }
    },

    search() {
      const unfiltered = this.contacts;
      let filtered = [];
      console.log(unfiltered);
      for (const contact of unfiltered) {
        if (
          contact.firstName.includes(this.searchText) ||
          contact.lastName.includes(this.searchText)
        ) {
          filtered.push(contact);
        }
      }
      this.updatedContacts = filtered;
    },
  },
};
</script>

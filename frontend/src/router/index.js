import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ContactView from "../views/ContactView.vue";
import CreateContactView from "../views/CreateContactView.vue";
import UpdateContactView from "../views/UpdateContactView.vue";
import DeleteSuccessView from "../views/DeleteSuccessView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/contact",
      name: "contact",
      component: ContactView,
    },
    {
      path: "/create",
      name: "create",
      component: CreateContactView,
    },
    {
      path: "/update",
      name: "update",
      component: UpdateContactView,
    },
    {
      path: "/delete",
      name: "delete",
      component: DeleteSuccessView,
    },
  ],
});

export default router;

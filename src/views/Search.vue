<template>
  <v-container class="py-0 fill-height">
    <v-card>
      <v-card-title>
        還沒做完
      </v-card-title>
    </v-card>
<!--    {{ this.$route.params}} {{this.$route.params.round}}-->
    <v-responsive max-width="260">
      <v-text-field
          dense
          flat
          hide-details
          rounded
          solo-inverted
          v-model=search_text
          append-icon="mdi-eye"
          @keydown.enter.prevent="send_search"
      ></v-text-field>

    </v-responsive>
  </v-container>
</template>

<script>
import router from "@/router";

export default {
  name: "Search",
  data() {
    return {
      search_text: ""
    }
  },
  methods: {
    send_search() {
      router.replace("/")

      router.replace("/" + localStorage.round + "/search/" + this.search_text)
    },
  }
}
</script>

<style scoped>

</style>
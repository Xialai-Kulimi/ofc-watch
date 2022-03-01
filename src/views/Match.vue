<template>
  <v-container>
    <v-card>

      <v-tabs
          v-model="tab"
          grow
      >
        <v-tabs-slider></v-tabs-slider>

        <v-tab
            v-for="item in items"
            :key="item"
        >
          {{ item.name }}
        </v-tab>
      </v-tabs>
      <v-tabs-items v-model="tab">
        <v-tab-item
            v-for="item in items"
            :key="item"
        >
          <v-card flat>
            <v-card-text v-text="item.text"></v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs-items>
    </v-card>
  </v-container>
</template>
<script>

export default {
  name: "Match",
  data() {
    return {
      search_text: "",
      tab: "",
      items: [
        {
          name: "one",
          text: "1yfgjhjkkfghjk",
        },
        {
          name: "o231ne",
          text: "142t34gyfgjhjkkfghjk",
        },
        {
          name: "o445ne",
          text: "gfdsgsdfg1yfgjhjkkfghjk",
        },
        {
          name: "on123123123e",
          text: "1yfadsfasdffgjhjkkfghjk",
        },

      ]
    }
  },
}
</script>

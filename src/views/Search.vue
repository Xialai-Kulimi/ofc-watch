<template>
  <v-container class="py-0 fill-height">
    <v-card width="800" class="pa-5">
      <v-card-title>
        搜尋
      </v-card-title>
      <v-divider></v-divider>
      <v-tabs
          v-model="tab"
      >
        <v-tab>
          玩家
        </v-tab>
        <v-tab>
          戰報
        </v-tab>
      </v-tabs>
      <v-tabs-items
          v-model="tab"
      >
        <v-tab-item class="pa-5">
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
        </v-tab-item>
        <v-tab-item class="pa-5">
          <v-expansion-panels>
            <v-expansion-panel>
              <v-expansion-panel-header>
                戰報種類
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-container>
                  <v-checkbox
                      hide-details
                      v-model="is_hunt"
                      label="狩獵戰報"
                  ></v-checkbox>
                  <v-checkbox
                      hide-details
                      v-model="is_wall"
                      label="攻城戰報"
                  ></v-checkbox>
                  <v-checkbox
                      hide-details
                      v-model="is_normal"
                      label="一般戰報"
                  ></v-checkbox>
                </v-container>
              </v-expansion-panel-content>

            </v-expansion-panel>
          </v-expansion-panels>
        </v-tab-item>
      </v-tabs-items>






    </v-card>
<!--    {{ this.$route.params}} {{this.$route.params.round}}-->

  </v-container>
</template>

<script>
import router from "@/plugins/router";

export default {
  name: "Search",
  data() {
    return {
      tab: 0,
      type: '',
      all_report: false,
      is_hunt: false,
      is_wall: false,
      is_normal: false,
      search_text: ""
    }
  },
  methods: {
    send_search() {
      let round = this.$route.params.round
      router.replace("/")

      router.replace("/" + round + "/search/" + this.search_text)
    },
  }
}
</script>

<style scoped>

</style>
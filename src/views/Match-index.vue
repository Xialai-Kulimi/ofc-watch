<template>
  <v-container>
    <v-card>

      <v-tabs
          v-model="tab"
          grow
          show-arrows
      >
        <v-tabs-slider></v-tabs-slider>

        <v-tab
            v-for="faction in matches"
            :key="faction"
        >
          {{ faction.name }}
        </v-tab>
      </v-tabs>
      <v-tabs-items v-model="tab">
        <v-tab-item
            v-for="faction in matches"
            :key="faction"
        >
          <v-simple-table>
            <template v-slot:default>
              <thead>
              <tr>
                <th class="text-left">
                  會戰編號
                </th>
                <th class="text-left">
                  發生時間
                </th>
                <th class="text-left">
                  持續時間
                </th>
                <th class="text-left">
                  進攻人數
                </th>
                <th class="text-left">
                  防守人數
                </th>
                <th class="text-left">
                  初始狀態
                </th>
                <th class="text-left">
                  結束狀態
                </th>
              </tr>
              </thead>
              <tbody>
              <tr
                  v-for="match in faction.matches"
                  :key="match"
              >
                <td><a @click="click()">{{ match.id }}</a></td>
                <td>{{ match.start_time }}</td>
                <td>{{ match.duration }}</td>
                <td>{{ match.atk_num }}</td>
                <td>{{ match.def_num }}</td>
                <td>{{ match.init_stat }}</td>
                <td>{{ match.end_stat }}</td>
              </tr>
              </tbody>
            </template>
          </v-simple-table>
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
      matches: [
        {
          name: "佛",
          matches: [
            {
              id: "佛＿ㄑㄨㄜ",
              start_time: 2,
              duration: 2,
              atk_num: 1,
              def_num: 2,
              init_stat: "fasdfsdf",
              end_stat: "fasdfasㄑ df"
            }
          ]
        },


      ]
    }
  },
}
</script>

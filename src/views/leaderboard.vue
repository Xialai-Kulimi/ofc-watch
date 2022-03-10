<template>
  <v-container>
    <v-card v-if="loading">

      <v-tabs
          v-model="tab"
          grow
          show-arrows
      >
        <v-tabs-slider></v-tabs-slider>

        <v-tab
            v-for="item in data_list"
            :key="item"
        >
          {{ item.json.name }}
        </v-tab>
      </v-tabs>
      <v-tabs-items v-model="tab">
        <v-tab-item
            v-for="c in data_list"
            :key="c"
        >
          <v-container
          >
            <v-simple-table>
              <thead>
              <tr>
                <th class="text-left">
                  陣營
                </th>
                <th class="text-left">
                  名稱
                </th>
                <th class="text-left">
                  數量
                </th>
              </tr>
              </thead>
              <tbody>
              <tr
                  v-for="item in c.json.list"
                  :key="item"
              >
                <td>{{ item.faction }}</td>
                <td><router-link :to="generate_link(item.id)">{{ item.name }}</router-link></td>
                <td>{{ item.count }}</td>
              </tr>
              </tbody>
            </v-simple-table>
          </v-container>
        </v-tab-item>
      </v-tabs-items>
    </v-card>
    <v-skeleton-loader
        v-bind="!loading"
        style="width: 100%"
        type="card-avatar, article, actions"
    ></v-skeleton-loader>
  </v-container>
</template>
<script>
// @ is an alias to /src


import api from "@/api";

export default {
  name: 'Home',
  data() {
    return {
      loading: false,
      tab: "",
      data_list: [
        {
          name: 'kill',
          json: {
            name: "擊殺排行",
            list: [
              {
                faction: "佛跳牆",
                name: "Kulimi",
                id: 1,
                count: 65656
              },
              {
                faction: "佛跳牆",
                name: "Kulimi",
                id: 1,
                count: 65656
              },
              {
                faction: "佛跳牆",
                name: "Kulimi",
                id: 1,
                count: 65656
              },
              {
                faction: "佛跳牆",
                name: "Kulimi",
                id: 1,
                count: 65656
              },
              {
                faction: "佛跳牆",
                name: "Kulimi",
                id: 1,
                count: 65656
              },
              {
                faction: "佛跳牆",
                name: "Kulimi",
                id: 1,
                count: 65656
              },
            ]
          }
        },
        {name: 'be_kill', json: {}},
        {name: 'damage', json: {}},
        {name: 'be_damage', json: {}},
        {name: 'wall_damage', json: {}},
        {name: 'all_xp', json: {}},
        {name: 'battle_xp', json: {}},
        {name: 'adventure_xp', json: {}},
        {name: 'hunt_xp', json: {}},
        {name: 'battle_count', json: {}},
        {name: 'hunt_count', json: {}},
      ]
    }
  },
  mounted: async function() {

    this.data_list = await api.getData( this.$route.params.round +"/leaderboard")
    this.loading = true
  },
  methods: {
    generate_link(id){
      return ("/" + localStorage.round + "/player/" + id.toString())
    }
  },
  components: {

  }
}
</script>
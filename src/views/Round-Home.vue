<template>
  <v-container>
    <v-container
        fluid
        row
        class="align-center justify-center"

    >

      <v-card
          width="800"
          style="display: flex"
          v-if="loading"
          class="pa-10 ma-5 justify-center align-center flex-column"
      >

        <img alt="Vue logo" src="../assets/big-eye.png" class="eye">
        <h1>Our Floating Castle Watcher</h1>
        <h1>我們的浮游城 觀察者</h1>
        <v-divider></v-divider>
        <v-container
            fluid
            row
            class="align-center justify-center"
        >
          <v-container
              class="ma-5"
              width="500"

          >
            <v-card-title>最新狩獵戰報</v-card-title>
            <v-virtual-scroll
                :bench="5"
                :items="hunt_events"
                height="400"
                item-height="32"
            >
              <template v-slot:default="{ item }">
                <v-list-item
                    :key="item"
                    link
                    dense
                    color="red"
                    :to="item.link"
                >
                  {{ (new Date(item.time)).toLocaleString() }} {{ item.text }}
                </v-list-item>
              </template>
            </v-virtual-scroll>
          </v-container>

          <v-container
              class="ma-5"
              width="500"

          >
            <v-card-title>最新攻城戰報</v-card-title>
            <v-virtual-scroll
                :bench="5"
                :items="castle_events"
                height="400"
                item-height="32"
            >
              <template v-slot:default="{ item }">
                <v-list-item
                    :key="item"
                    link
                    dense
                    color="red"
                    :to="item.link"
                >
                  [{{ item.location }}] {{ (new Date(item.time)).toLocaleString() }} {{ item.text }}
                </v-list-item>
              </template>
            </v-virtual-scroll>
          </v-container>

          <v-container
              class="ma-5"
          >
            <v-card-title>狩獵</v-card-title>

            <v-container
                v-for="hunt in hunts"
                :key="hunt"
                style="display: flex"

            >
              <v-dialog
                  :v-model="hunt.dialog"
                  width="500"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                      plain
                      v-bind="attrs"
                      v-on="on"
                  >
                    {{ hunt.name }}
                  </v-btn>
                </template>

                <v-card class="pa-5">
                  <v-container>
                    <v-card-title>
                      {{ hunt.name }}
                    </v-card-title>
                  </v-container>

                  <v-simple-table
                      fixed-header
                      height="300px"
                  >

                    <template v-slot:default>
                      <thead>
                      <tr>
                        <th class="text-left">
                          出現層數
                        </th>
                        <th class="text-left">
                          名稱
                        </th>
                        <th class="text-left">
                          種類
                        </th>
                        <th class="text-left">
                          掉落物
                        </th>
                      </tr>
                      </thead>
                      <tbody>
                      <tr
                          v-for="item in hunt.monster_list"
                          :key="item"

                      >
                        <td>{{ item.level[0] }} ~ {{ item.level[1] }}</td>
                        <td>{{ item.name }}</td>
                        <td>{{ item.type }}</td>
                        <td>
                          <v-menu

                              close-on-click
                          >
                            <template v-slot:activator="{ on, attrs }">
                              <v-btn
                                  plain
                                  v-bind="attrs"
                                  v-on="on"
                              >
                                點擊查看
                              </v-btn>
                            </template>

                            <v-list
                                width="500"
                            >
                              <v-list-item
                                  v-for="i in item.loot"
                                  :key="i"
                              >
                                <v-list-item-title>{{ i.type }}</v-list-item-title>
                                <v-list-item>{{ i.count }}</v-list-item>
                              </v-list-item>
                            </v-list>
                          </v-menu>
                        </td>
                      </tr>
                      </tbody>
                    </template>
                  </v-simple-table>

                  <v-simple-table
                      fixed-header
                      height="300px"
                  >
                    <template v-slot:default>
                      <thead>
                      <tr>
                        <th class="text-left">
                          層數
                        </th>
                        <th class="text-left">
                          總狩獵次數
                        </th>
                        <th class="text-left">
                          怪物組成
                        </th>
                      </tr>
                      </thead>
                      <tbody>
                      <tr
                          v-for="item in hunt.level_list"
                          :key="item"

                      >
                        <td>{{ item.level }}</td>
                        <td>{{ item.count }}</td>
                        <td>
                          <v-menu

                              close-on-click
                          >
                            <template v-slot:activator="{ on, attrs }">
                              <v-btn
                                  plain
                                  v-bind="attrs"
                                  v-on="on"
                              >
                                點擊查看
                              </v-btn>
                            </template>

                            <v-list
                                width="500"
                            >
                              <v-list-item
                                  v-for="i in item.monster_list"
                                  :key="i"
                              >
                                <v-list-item-title>{{ i.name }}</v-list-item-title>
                                <v-list-item>{{ i.count }}</v-list-item>
                                <v-list-item>{{ i.percent }}</v-list-item>
                              </v-list-item>
                            </v-list>
                          </v-menu>
                        </td>
                      </tr>
                      </tbody>
                    </template>
                  </v-simple-table>

                </v-card>
              </v-dialog>

            </v-container>
          </v-container>


          <v-container
              class="ma-5"
              width="500"

          >
            <v-card-title>裝備種類統計</v-card-title>
            <v-simple-table>
              <template v-slot:default>
                <thead>
                <tr>
                  <th class="text-left">
                    種類
                  </th>
                  <th class="text-left">
                    次數
                  </th>
                </tr>
                </thead>
                <tbody>
                <tr
                    v-for="item in weapon_type_count"
                    :key="item.name"

                >
                  <td>{{ item.name }}</td>
                  <td>{{ item.count }}</td>
                </tr>
                </tbody>
              </template>
            </v-simple-table>
          </v-container>
        </v-container>
      </v-card>
      <v-skeleton-loader
          v-if="!loading"
          width="800"
          type="card-avatar, article, actions"
      ></v-skeleton-loader>
    </v-container>

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
      benched: 0,
      hunt_events: [
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/history/545454"
        },
        {
          text: "Kulimi died",
          color: "FF0000",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "black",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "gray",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "danger",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "danger",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "danger",
          link: "/12/545454"
        },
        {
          text: "fsdf died",
          color: "info",
          link: "/12/54fff5454"
        },
        {
          text: "Kulimi died",
          color: "danger",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "danger",
          link: "/12/545454"
        },

      ],
      castle_events: [
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/history/545454"
        },
        {
          text: "Kulimi died",
          color: "FF0000",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "red",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "black",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "gray",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "danger",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "danger",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "danger",
          link: "/12/545454"
        },
        {
          text: "fsdf died",
          color: "info",
          link: "/12/54fff5454"
        },
        {
          text: "Kulimi died",
          color: "danger",
          link: "/12/545454"
        },
        {
          text: "Kulimi died",
          color: "danger",
          link: "/12/545454"
        },

      ],

      page: 1,
      hunts: [

        {
          name: "vul3蝙蝠動",
          dialog: false,
          dist: [
            {
              level: 1,
              count: 67890,
              monster: [
                {
                  type: "wolf",
                  count: 678,
                  percent: '69%'
                },
                {
                  type: "rabbot",
                  count: 678
                },
              ]
            },
            {
              level: 2,
              count: 67890,
              monster: [
                {
                  type: "wolf",
                  count: 678
                },
                {
                  type: "rabbot",
                  count: 678
                },
              ]
            },
            {
              level: 3,
              count: 67890,
              monster: [
                {
                  type: "wolf",
                  count: 678
                },
                {
                  type: "rabbot",
                  count: 678
                },
              ]
            },
            {
              level: 4,
              count: 67890,
              monster: [
                {
                  type: "wolf",
                  count: 678
                },
                {
                  type: "rabbot",
                  count: 678
                },
              ]
            },


          ]
        },
        {
          name: "迷宮區",
          dialog: false,
          dist: [
            {
              level: 1,
              count: 67890,
              monster: [
                {
                  type: "wolf",
                  count: 678
                },
                {
                  type: "rabbot",
                  count: 678
                },
              ]
            },
            {
              level: 2,
              count: 67890,
              monster: [
                {
                  type: "wolf",
                  count: 678
                },
                {
                  type: "rabbot",
                  count: 678
                },
              ]
            },
            {
              level: 3,
              count: 67890,
              monster: [
                {
                  type: "wolf",
                  count: 678
                },
                {
                  type: "rabbot",
                  count: 678
                },
              ]
            },
            {
              level: 4,
              count: 67890,
              monster: [
                {
                  type: "wolf",
                  count: 678
                },
                {
                  type: "rabbot",
                  count: 678
                },
              ]
            },


          ]
        }
      ],
      weapon_type_count: [
        {name: "水龍頭", count: 87878787},
        {name: "單手劍", count: 69696969},
        {name: "單手劍", count: 69696969},
        {name: "單手劍", count: 69696969},
        {name: "單手劍", count: 69696969},
        {name: "單手劍", count: 69696969},
        {name: "單手劍", count: 69696969},
        {name: "單手劍", count: 69696969},
        {name: "單手劍", count: 69696969},
        {name: "單手劍", count: 69696969},
      ]
    }
  },
  mounted: async function () {
    this.hunt_events = await api.getData(this.$route.params.round + "/hunt_events")
    this.castle_events = await api.getData(this.$route.params.round + "/castle_events")
    this.hunts = await api.getData(this.$route.params.round + "/hunts")
    this.weapon_type_count = await api.getData(this.$route.params.round + "/weapon_type_count")
    this.loading = true

  },
  components: {}
}
</script>

<style scoped lang="scss">

@keyframes eye-open {
  0% {
    transform: matrix(1, 0, 0, 0, 0, 0);
  }
  50% {
    transform: matrix(1, 0, 0, 0.0001, 0, 0);
  }
  60% {
    transform: matrix(1, 0, 0, 0.3, 0, 0);
  }
  70% {
    transform: matrix(1, 0, 0, 0.3, 0, 0);
  }
  80% {
    transform: matrix(1.01, 0, 0, 0.01, 0, 0);
  }

  100% {
    transform: matrix(1, 0, 0, 1, 0, 0);
  }
}

.eye {
  width: 500px;
  height: 500px;
  animation-name: eye-open;
  animation-duration: 2.5s;

}

.eye2 {
  width: 500px;
  height: 500px;
  //animation-name: eye-open;
  //animation-duration: 2.5s;

}

</style>

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
                v-if="hunt_events_loading"
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
            <v-skeleton-loader
                v-if="!hunt_events_loading"

                type="article"
            ></v-skeleton-loader>
          </v-container>

          <v-container
              class="ma-5"
              width="500"

          >
            <v-card-title>最新攻城戰報</v-card-title>
            <v-virtual-scroll
                v-if="castle_events_loading"
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
            <v-skeleton-loader
                v-if="!castle_events_loading"

                type="article"
            ></v-skeleton-loader>
          </v-container>

          <v-container
              class="ma-5"
          >
            <v-card-title>狩獵</v-card-title>
            <v-container
                v-if="hunts_loading"
            >
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
                                    outlined
                                    v-bind="attrs"
                                    v-on="on"
                                >
                                  點擊查看
                                </v-btn>
<!--                                <v-btn-->
<!--                                    plain-->
<!--                                    v-bind="attrs"-->
<!--                                    v-on="on"-->
<!--                                >-->
<!--                                  點擊查看-->
<!--                                </v-btn>-->
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
                                    outlined
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

            <v-skeleton-loader
                v-if="!hunts_loading"

                type="article"
            ></v-skeleton-loader>
          </v-container>


          <v-container
              class="ma-5"
              width="500"

          >
            <v-card-title>裝備種類統計</v-card-title>
            <v-simple-table
                v-if="weapon_type_count_loading"
            >
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
            <v-skeleton-loader
                v-if="!weapon_type_count_loading"
                type="article"
            ></v-skeleton-loader>
          </v-container>
        </v-container>
      </v-card>
      <v-skeleton-loader
          v-if="!loading"
          width="800"
          type="article"
      ></v-skeleton-loader>
    </v-container>

  </v-container>
</template>

<script>
// @ is an alias to /src


import api from "@/api";

export default {
  name: 'Round-Home',
  data() {
    return {
      loading: true,
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
      hunts:[{"name":"大草原","dialog":false,"monster_list":[{"level":[1,38],"name":"小白兔","type":"動物","loot":[{"type":"兔肉","count":3225},{"type":"S級兔皮","count":810},{"type":"稀有兔肉","count":788},{"type":"兔皮","count":9057}]},{"level":[1,39],"name":"黑兔","type":"動物","loot":[{"type":"黑兔皮","count":6572},{"type":"兔肉","count":3646},{"type":"稀有兔肉","count":809}]},{"level":[1,33],"name":"超稀有肥兔","type":"動物","loot":[{"type":"S級兔皮","count":322},{"type":"稀有兔肉","count":141},{"type":"兔皮","count":211},{"type":"S級超稀有兔肉","count":56},{"type":"兔肉","count":296}]},{"level":[1,32],"name":"雜燴兔","type":"動物","loot":[{"type":"S級超稀有兔肉","count":126},{"type":"稀有兔肉","count":384},{"type":"S級兔皮","count":185},{"type":"樂高積木","count":156},{"type":"好運石","count":864}]},{"level":[9,40],"name":"菇菇寶貝","type":"魔物","loot":[{"type":"鐵礦","count":215},{"type":"菇菇寶貝的傘","count":1170},{"type":"銅礦","count":148},{"type":"桐木","count":856},{"type":"強身迷幻草","count":19}]},{"level":[13,40],"name":"狂躁山豬","type":"動物","loot":[{"type":"紋身貼紙","count":133},{"type":"石頭","count":1610},{"type":"強身迷幻草","count":23},{"type":"山豬肉","count":321},{"type":"山豬獠牙","count":339},{"type":"好運石","count":377},{"type":"採礦入門書","count":89},{"type":"採礦密技","count":62}]},{"level":[19,37],"name":"草原狼","type":"動物","loot":[{"type":"山豬肉","count":16},{"type":"稀有兔肉","count":54},{"type":"銀礦","count":67},{"type":"狼牙","count":100},{"type":"技能書：蛇噬","count":5}]},{"level":[37,37],"name":"大樹守衛","type":"不明","loot":[]}],"level_list":[{"level":1,"count":1880,"monster_list":[{"name":"小白兔","count":1113,"percent":"59.2%"},{"name":"黑兔","count":733,"percent":"39.0%"},{"name":"雜燴兔","count":25,"percent":"1.3%"},{"name":"超稀有肥兔","count":9,"percent":"0.5%"}]},{"level":2,"count":1753,"monster_list":[{"name":"小白兔","count":1053,"percent":"60.1%"},{"name":"黑兔","count":668,"percent":"38.1%"},{"name":"超稀有肥兔","count":17,"percent":"1.0%"},{"name":"雜燴兔","count":15,"percent":"0.9%"}]},{"level":3,"count":1743,"monster_list":[{"name":"黑兔","count":673,"percent":"38.6%"},{"name":"小白兔","count":1040,"percent":"59.7%"},{"name":"超稀有肥兔","count":19,"percent":"1.1%"},{"name":"雜燴兔","count":11,"percent":"0.6%"}]},{"level":4,"count":1746,"monster_list":[{"name":"小白兔","count":1064,"percent":"60.9%"},{"name":"黑兔","count":629,"percent":"36.0%"},{"name":"雜燴兔","count":27,"percent":"1.5%"},{"name":"超稀有肥兔","count":26,"percent":"1.5%"}]},{"level":5,"count":1682,"monster_list":[{"name":"小白兔","count":1010,"percent":"60.0%"},{"name":"超稀有肥兔","count":23,"percent":"1.4%"},{"name":"黑兔","count":635,"percent":"37.8%"},{"name":"雜燴兔","count":14,"percent":"0.8%"}]},{"level":6,"count":1617,"monster_list":[{"name":"小白兔","count":985,"percent":"60.9%"},{"name":"黑兔","count":589,"percent":"36.4%"},{"name":"超稀有肥兔","count":22,"percent":"1.4%"},{"name":"雜燴兔","count":21,"percent":"1.3%"}]},{"level":7,"count":1524,"monster_list":[{"name":"小白兔","count":912,"percent":"59.8%"},{"name":"黑兔","count":569,"percent":"37.3%"},{"name":"超稀有肥兔","count":26,"percent":"1.7%"},{"name":"雜燴兔","count":17,"percent":"1.1%"}]},{"level":8,"count":1415,"monster_list":[{"name":"小白兔","count":841,"percent":"59.4%"},{"name":"黑兔","count":539,"percent":"38.1%"},{"name":"超稀有肥兔","count":20,"percent":"1.4%"},{"name":"雜燴兔","count":15,"percent":"1.1%"}]},{"level":9,"count":1296,"monster_list":[{"name":"小白兔","count":722,"percent":"55.7%"},{"name":"菇菇寶貝","count":295,"percent":"22.8%"},{"name":"黑兔","count":251,"percent":"19.4%"},{"name":"超稀有肥兔","count":17,"percent":"1.3%"},{"name":"雜燴兔","count":11,"percent":"0.8%"}]},{"level":10,"count":1167,"monster_list":[{"name":"小白兔","count":660,"percent":"56.6%"},{"name":"菇菇寶貝","count":273,"percent":"23.4%"},{"name":"黑兔","count":218,"percent":"18.7%"},{"name":"超稀有肥兔","count":9,"percent":"0.8%"},{"name":"雜燴兔","count":7,"percent":"0.6%"}]},{"level":11,"count":1046,"monster_list":[{"name":"小白兔","count":616,"percent":"58.9%"},{"name":"黑兔","count":186,"percent":"17.8%"},{"name":"菇菇寶貝","count":227,"percent":"21.7%"},{"name":"超稀有肥兔","count":12,"percent":"1.1%"},{"name":"雜燴兔","count":5,"percent":"0.5%"}]},{"level":12,"count":900,"monster_list":[{"name":"黑兔","count":170,"percent":"18.9%"},{"name":"小白兔","count":526,"percent":"58.4%"},{"name":"菇菇寶貝","count":196,"percent":"21.8%"},{"name":"雜燴兔","count":4,"percent":"0.4%"},{"name":"超稀有肥兔","count":4,"percent":"0.4%"}]},{"level":13,"count":796,"monster_list":[{"name":"小白兔","count":402,"percent":"50.5%"},{"name":"菇菇寶貝","count":51,"percent":"6.4%"},{"name":"狂躁山豬","count":150,"percent":"18.8%"},{"name":"黑兔","count":164,"percent":"20.6%"},{"name":"超稀有肥兔","count":14,"percent":"1.8%"},{"name":"雜燴兔","count":15,"percent":"1.9%"}]},{"level":14,"count":693,"monster_list":[{"name":"小白兔","count":431,"percent":"62.2%"},{"name":"黑兔","count":103,"percent":"14.9%"},{"name":"狂躁山豬","count":107,"percent":"15.4%"},{"name":"雜燴兔","count":8,"percent":"1.2%"},{"name":"菇菇寶貝","count":32,"percent":"4.6%"},{"name":"超稀有肥兔","count":12,"percent":"1.7%"}]},{"level":15,"count":582,"monster_list":[{"name":"小白兔","count":326,"percent":"56.0%"},{"name":"狂躁山豬","count":110,"percent":"18.9%"},{"name":"黑兔","count":112,"percent":"19.2%"},{"name":"菇菇寶貝","count":21,"percent":"3.6%"},{"name":"超稀有肥兔","count":7,"percent":"1.2%"},{"name":"雜燴兔","count":6,"percent":"1.0%"}]},{"level":16,"count":517,"monster_list":[{"name":"小白兔","count":292,"percent":"56.5%"},{"name":"黑兔","count":117,"percent":"22.6%"},{"name":"狂躁山豬","count":90,"percent":"17.4%"},{"name":"雜燴兔","count":4,"percent":"0.8%"},{"name":"菇菇寶貝","count":11,"percent":"2.1%"},{"name":"超稀有肥兔","count":3,"percent":"0.6%"}]},{"level":17,"count":448,"monster_list":[{"name":"小白兔","count":235,"percent":"52.5%"},{"name":"狂躁山豬","count":89,"percent":"19.9%"},{"name":"黑兔","count":104,"percent":"23.2%"},{"name":"菇菇寶貝","count":17,"percent":"3.8%"},{"name":"雜燴兔","count":3,"percent":"0.7%"}]},{"level":18,"count":390,"monster_list":[{"name":"小白兔","count":209,"percent":"53.6%"},{"name":"黑兔","count":77,"percent":"19.7%"},{"name":"狂躁山豬","count":87,"percent":"22.3%"},{"name":"雜燴兔","count":3,"percent":"0.8%"},{"name":"菇菇寶貝","count":13,"percent":"3.3%"},{"name":"超稀有肥兔","count":1,"percent":"0.3%"}]},{"level":19,"count":337,"monster_list":[{"name":"狂躁山豬","count":39,"percent":"11.6%"},{"name":"小白兔","count":171,"percent":"50.7%"},{"name":"黑兔","count":70,"percent":"20.8%"},{"name":"草原狼","count":27,"percent":"8.0%"},{"name":"菇菇寶貝","count":23,"percent":"6.8%"},{"name":"超稀有肥兔","count":5,"percent":"1.5%"},{"name":"雜燴兔","count":2,"percent":"0.6%"}]},{"level":20,"count":299,"monster_list":[{"name":"超稀有肥兔","count":7,"percent":"2.3%"},{"name":"小白兔","count":139,"percent":"46.5%"},{"name":"狂躁山豬","count":52,"percent":"17.4%"},{"name":"黑兔","count":67,"percent":"22.4%"},{"name":"草原狼","count":22,"percent":"7.4%"},{"name":"菇菇寶貝","count":9,"percent":"3.0%"},{"name":"雜燴兔","count":3,"percent":"1.0%"}]},{"level":21,"count":249,"monster_list":[{"name":"黑兔","count":40,"percent":"16.1%"},{"name":"菇菇寶貝","count":16,"percent":"6.4%"},{"name":"草原狼","count":23,"percent":"9.2%"},{"name":"小白兔","count":142,"percent":"57.0%"},{"name":"超稀有肥兔","count":5,"percent":"2.0%"},{"name":"狂躁山豬","count":13,"percent":"5.2%"},{"name":"雜燴兔","count":10,"percent":"4.0%"}]},{"level":22,"count":201,"monster_list":[{"name":"小白兔","count":108,"percent":"53.7%"},{"name":"菇菇寶貝","count":8,"percent":"4.0%"},{"name":"黑兔","count":47,"percent":"23.4%"},{"name":"草原狼","count":11,"percent":"5.5%"},{"name":"狂躁山豬","count":24,"percent":"11.9%"},{"name":"雜燴兔","count":3,"percent":"1.5%"}]},{"level":23,"count":155,"monster_list":[{"name":"小白兔","count":81,"percent":"52.3%"},{"name":"狂躁山豬","count":21,"percent":"13.5%"},{"name":"黑兔","count":27,"percent":"17.4%"},{"name":"菇菇寶貝","count":10,"percent":"6.5%"},{"name":"超稀有肥兔","count":7,"percent":"4.5%"},{"name":"草原狼","count":9,"percent":"5.8%"}]},{"level":24,"count":130,"monster_list":[{"name":"小白兔","count":72,"percent":"55.4%"},{"name":"草原狼","count":19,"percent":"14.6%"},{"name":"菇菇寶貝","count":2,"percent":"1.5%"},{"name":"超稀有肥兔","count":2,"percent":"1.5%"},{"name":"黑兔","count":23,"percent":"17.7%"},{"name":"狂躁山豬","count":12,"percent":"9.2%"}]},{"level":25,"count":104,"monster_list":[{"name":"菇菇寶貝","count":22,"percent":"21.2%"},{"name":"小白兔","count":43,"percent":"41.3%"},{"name":"狂躁山豬","count":11,"percent":"10.6%"},{"name":"黑兔","count":21,"percent":"20.2%"},{"name":"雜燴兔","count":2,"percent":"1.9%"},{"name":"草原狼","count":4,"percent":"3.8%"},{"name":"超稀有肥兔","count":1,"percent":"1.0%"}]},{"level":26,"count":71,"monster_list":[{"name":"小白兔","count":29,"percent":"40.8%"},{"name":"菇菇寶貝","count":13,"percent":"18.3%"},{"name":"草原狼","count":4,"percent":"5.6%"},{"name":"黑兔","count":17,"percent":"23.9%"},{"name":"狂躁山豬","count":7,"percent":"9.9%"},{"name":"雜燴兔","count":1,"percent":"1.4%"}]},{"level":27,"count":61,"monster_list":[{"name":"超稀有肥兔","count":2,"percent":"3.3%"},{"name":"黑兔","count":13,"percent":"21.3%"},{"name":"狂躁山豬","count":7,"percent":"11.5%"},{"name":"小白兔","count":20,"percent":"32.8%"},{"name":"菇菇寶貝","count":12,"percent":"19.7%"},{"name":"草原狼","count":6,"percent":"9.8%"},{"name":"雜燴兔","count":1,"percent":"1.6%"}]},{"level":28,"count":45,"monster_list":[{"name":"小白兔","count":20,"percent":"44.4%"},{"name":"狂躁山豬","count":7,"percent":"15.6%"},{"name":"菇菇寶貝","count":7,"percent":"15.6%"},{"name":"草原狼","count":4,"percent":"8.9%"},{"name":"黑兔","count":7,"percent":"15.6%"}]},{"level":29,"count":31,"monster_list":[{"name":"小白兔","count":8,"percent":"25.8%"},{"name":"狂躁山豬","count":8,"percent":"25.8%"},{"name":"菇菇寶貝","count":4,"percent":"12.9%"},{"name":"黑兔","count":9,"percent":"29.0%"},{"name":"雜燴兔","count":2,"percent":"6.5%"}]},{"level":30,"count":27,"monster_list":[{"name":"黑兔","count":9,"percent":"33.3%"},{"name":"菇菇寶貝","count":6,"percent":"22.2%"},{"name":"雜燴兔","count":2,"percent":"7.4%"},{"name":"小白兔","count":5,"percent":"18.5%"},{"name":"草原狼","count":3,"percent":"11.1%"},{"name":"超稀有肥兔","count":1,"percent":"3.7%"},{"name":"狂躁山豬","count":1,"percent":"3.7%"}]},{"level":31,"count":22,"monster_list":[{"name":"菇菇寶貝","count":2,"percent":"9.1%"},{"name":"小白兔","count":12,"percent":"54.5%"},{"name":"狂躁山豬","count":5,"percent":"22.7%"},{"name":"超稀有肥兔","count":1,"percent":"4.5%"},{"name":"黑兔","count":1,"percent":"4.5%"},{"name":"草原狼","count":1,"percent":"4.5%"}]},{"level":32,"count":22,"monster_list":[{"name":"菇菇寶貝","count":7,"percent":"31.8%"},{"name":"小白兔","count":4,"percent":"18.2%"},{"name":"草原狼","count":5,"percent":"22.7%"},{"name":"黑兔","count":4,"percent":"18.2%"},{"name":"狂躁山豬","count":1,"percent":"4.5%"},{"name":"雜燴兔","count":1,"percent":"4.5%"}]},{"level":33,"count":19,"monster_list":[{"name":"黑兔","count":9,"percent":"47.4%"},{"name":"小白兔","count":2,"percent":"10.5%"},{"name":"狂躁山豬","count":4,"percent":"21.1%"},{"name":"菇菇寶貝","count":1,"percent":"5.3%"},{"name":"草原狼","count":2,"percent":"10.5%"},{"name":"超稀有肥兔","count":1,"percent":"5.3%"}]},{"level":34,"count":14,"monster_list":[{"name":"狂躁山豬","count":4,"percent":"28.6%"},{"name":"黑兔","count":8,"percent":"57.1%"},{"name":"小白兔","count":2,"percent":"14.3%"}]},{"level":35,"count":10,"monster_list":[{"name":"小白兔","count":4,"percent":"40.0%"},{"name":"黑兔","count":4,"percent":"40.0%"},{"name":"狂躁山豬","count":2,"percent":"20.0%"}]},{"level":36,"count":14,"monster_list":[{"name":"黑兔","count":2,"percent":"14.3%"},{"name":"狂躁山豬","count":10,"percent":"71.4%"},{"name":"小白兔","count":1,"percent":"7.1%"},{"name":"菇菇寶貝","count":1,"percent":"7.1%"}]},{"level":37,"count":9,"monster_list":[{"name":"大樹守衛","count":2,"percent":"22.2%"},{"name":"小白兔","count":5,"percent":"55.6%"},{"name":"黑兔","count":1,"percent":"11.1%"},{"name":"草原狼","count":1,"percent":"11.1%"}]},{"level":38,"count":6,"monster_list":[{"name":"小白兔","count":4,"percent":"66.7%"},{"name":"黑兔","count":2,"percent":"33.3%"}]},{"level":39,"count":2,"monster_list":[{"name":"黑兔","count":1,"percent":"50.0%"},{"name":"狂躁山豬","count":1,"percent":"50.0%"}]},{"level":40,"count":2,"monster_list":[{"name":"菇菇寶貝","count":1,"percent":"50.0%"},{"name":"狂躁山豬","count":1,"percent":"50.0%"}]}]},{"name":"迷宮區","dialog":false,"monster_list":[{"level":[1,37],"name":"闇矮人礦工","type":"魔物","loot":[{"type":"太陽石","count":196},{"type":"鐵礦","count":3287},{"type":"慢工出細活","count":25},{"type":"銅礦","count":1681},{"type":"銀礦","count":790},{"type":"月光石","count":297},{"type":"黑曜石","count":716},{"type":"虎眼石","count":163},{"type":"礦裝製作入門","count":29},{"type":"十字鎬戰鬥術","count":66}]},{"level":[1,40],"name":"礦石元素","type":"魔物","loot":[{"type":"石頭","count":3007},{"type":"鐵礦","count":1279},{"type":"銠","count":185},{"type":"銥","count":313},{"type":"鋨","count":289},{"type":"魔岩","count":243},{"type":"魔鐵","count":156},{"type":"鈹","count":90}]},{"level":[1,40],"name":"枉死怨靈","type":"不明","loot":[{"type":"技能書：重擊","count":20},{"type":"唐家霸王槍法","count":47},{"type":"技能書：盾牌格檔","count":27},{"type":"禁衛令牌","count":10},{"type":"技能書：蛇噬","count":19},{"type":"技能書：銳爪","count":11}]},{"level":[11,37],"name":"隱藏寶箱","type":"寶箱","loot":[{"type":"鑽石","count":104},{"type":"死人骨頭","count":82},{"type":"黃水晶","count":150},{"type":"金礦","count":219},{"type":"銀礦","count":304},{"type":"銅礦","count":185}]},{"level":[18,35],"name":"發瘋劍士","type":"人類","loot":[{"type":"技能書：奪命擊","count":14},{"type":"技能書：銳爪","count":11},{"type":"技能書：迴旋盾","count":7},{"type":"強身迷幻草","count":5}]},{"level":[27,38],"name":"熔爐騎士","type":"不明","loot":[]}],"level_list":[{"level":1,"count":177,"monster_list":[{"name":"闇矮人礦工","count":96,"percent":"54.2%"},{"name":"礦石元素","count":73,"percent":"41.2%"},{"name":"枉死怨靈","count":8,"percent":"4.5%"}]},{"level":2,"count":135,"monster_list":[{"name":"礦石元素","count":52,"percent":"38.5%"},{"name":"闇矮人礦工","count":76,"percent":"56.3%"},{"name":"枉死怨靈","count":7,"percent":"5.2%"}]},{"level":3,"count":130,"monster_list":[{"name":"礦石元素","count":47,"percent":"36.2%"},{"name":"闇矮人礦工","count":75,"percent":"57.7%"},{"name":"枉死怨靈","count":8,"percent":"6.2%"}]},{"level":4,"count":131,"monster_list":[{"name":"礦石元素","count":56,"percent":"42.7%"},{"name":"闇矮人礦工","count":61,"percent":"46.6%"},{"name":"枉死怨靈","count":14,"percent":"10.7%"}]},{"level":5,"count":123,"monster_list":[{"name":"礦石元素","count":55,"percent":"44.7%"},{"name":"枉死怨靈","count":8,"percent":"6.5%"},{"name":"闇矮人礦工","count":60,"percent":"48.8%"}]},{"level":6,"count":113,"monster_list":[{"name":"闇矮人礦工","count":43,"percent":"38.1%"},{"name":"礦石元素","count":57,"percent":"50.4%"},{"name":"枉死怨靈","count":13,"percent":"11.5%"}]},{"level":7,"count":113,"monster_list":[{"name":"枉死怨靈","count":3,"percent":"2.7%"},{"name":"礦石元素","count":63,"percent":"55.8%"},{"name":"闇矮人礦工","count":47,"percent":"41.6%"}]},{"level":8,"count":107,"monster_list":[{"name":"礦石元素","count":43,"percent":"40.2%"},{"name":"闇矮人礦工","count":54,"percent":"50.5%"},{"name":"枉死怨靈","count":10,"percent":"9.3%"}]},{"level":9,"count":104,"monster_list":[{"name":"礦石元素","count":54,"percent":"51.9%"},{"name":"闇矮人礦工","count":38,"percent":"36.5%"},{"name":"枉死怨靈","count":12,"percent":"11.5%"}]},{"level":10,"count":103,"monster_list":[{"name":"礦石元素","count":39,"percent":"37.9%"},{"name":"闇矮人礦工","count":48,"percent":"46.6%"},{"name":"枉死怨靈","count":16,"percent":"15.5%"}]},{"level":11,"count":101,"monster_list":[{"name":"隱藏寶箱","count":8,"percent":"7.9%"},{"name":"礦石元素","count":24,"percent":"23.8%"},{"name":"闇矮人礦工","count":55,"percent":"54.5%"},{"name":"枉死怨靈","count":14,"percent":"13.9%"}]},{"level":12,"count":98,"monster_list":[{"name":"闇矮人礦工","count":42,"percent":"42.9%"},{"name":"枉死怨靈","count":12,"percent":"12.2%"},{"name":"隱藏寶箱","count":7,"percent":"7.1%"},{"name":"礦石元素","count":37,"percent":"37.8%"}]},{"level":13,"count":94,"monster_list":[{"name":"闇矮人礦工","count":48,"percent":"51.1%"},{"name":"枉死怨靈","count":9,"percent":"9.6%"},{"name":"礦石元素","count":34,"percent":"36.2%"},{"name":"隱藏寶箱","count":3,"percent":"3.2%"}]},{"level":14,"count":92,"monster_list":[{"name":"闇矮人礦工","count":53,"percent":"57.6%"},{"name":"礦石元素","count":20,"percent":"21.7%"},{"name":"枉死怨靈","count":13,"percent":"14.1%"},{"name":"隱藏寶箱","count":6,"percent":"6.5%"}]},{"level":15,"count":89,"monster_list":[{"name":"礦石元素","count":38,"percent":"42.7%"},{"name":"枉死怨靈","count":12,"percent":"13.5%"},{"name":"闇矮人礦工","count":34,"percent":"38.2%"},{"name":"隱藏寶箱","count":5,"percent":"5.6%"}]},{"level":16,"count":84,"monster_list":[{"name":"礦石元素","count":48,"percent":"57.1%"},{"name":"隱藏寶箱","count":6,"percent":"7.1%"},{"name":"闇矮人礦工","count":25,"percent":"29.8%"},{"name":"枉死怨靈","count":5,"percent":"6.0%"}]},{"level":17,"count":84,"monster_list":[{"name":"礦石元素","count":36,"percent":"42.9%"},{"name":"枉死怨靈","count":16,"percent":"19.0%"},{"name":"闇矮人礦工","count":28,"percent":"33.3%"},{"name":"隱藏寶箱","count":4,"percent":"4.8%"}]},{"level":18,"count":85,"monster_list":[{"name":"礦石元素","count":34,"percent":"40.0%"},{"name":"闇矮人礦工","count":39,"percent":"45.9%"},{"name":"枉死怨靈","count":9,"percent":"10.6%"},{"name":"發瘋劍士","count":1,"percent":"1.2%"},{"name":"隱藏寶箱","count":2,"percent":"2.4%"}]},{"level":19,"count":81,"monster_list":[{"name":"枉死怨靈","count":9,"percent":"11.1%"},{"name":"礦石元素","count":36,"percent":"44.4%"},{"name":"闇矮人礦工","count":29,"percent":"35.8%"},{"name":"隱藏寶箱","count":6,"percent":"7.4%"},{"name":"發瘋劍士","count":1,"percent":"1.2%"}]},{"level":20,"count":78,"monster_list":[{"name":"礦石元素","count":26,"percent":"33.3%"},{"name":"闇矮人礦工","count":27,"percent":"34.6%"},{"name":"枉死怨靈","count":14,"percent":"17.9%"},{"name":"隱藏寶箱","count":9,"percent":"11.5%"},{"name":"發瘋劍士","count":2,"percent":"2.6%"}]},{"level":21,"count":77,"monster_list":[{"name":"闇矮人礦工","count":22,"percent":"28.6%"},{"name":"礦石元素","count":30,"percent":"39.0%"},{"name":"枉死怨靈","count":11,"percent":"14.3%"},{"name":"隱藏寶箱","count":9,"percent":"11.7%"},{"name":"發瘋劍士","count":5,"percent":"6.5%"}]},{"level":22,"count":74,"monster_list":[{"name":"礦石元素","count":29,"percent":"39.2%"},{"name":"闇矮人礦工","count":28,"percent":"37.8%"},{"name":"枉死怨靈","count":15,"percent":"20.3%"},{"name":"隱藏寶箱","count":1,"percent":"1.4%"},{"name":"發瘋劍士","count":1,"percent":"1.4%"}]},{"level":23,"count":71,"monster_list":[{"name":"闇矮人礦工","count":23,"percent":"32.4%"},{"name":"礦石元素","count":35,"percent":"49.3%"},{"name":"枉死怨靈","count":8,"percent":"11.3%"},{"name":"隱藏寶箱","count":4,"percent":"5.6%"},{"name":"發瘋劍士","count":1,"percent":"1.4%"}]},{"level":24,"count":70,"monster_list":[{"name":"枉死怨靈","count":9,"percent":"12.9%"},{"name":"礦石元素","count":31,"percent":"44.3%"},{"name":"闇矮人礦工","count":19,"percent":"27.1%"},{"name":"隱藏寶箱","count":9,"percent":"12.9%"},{"name":"發瘋劍士","count":2,"percent":"2.9%"}]},{"level":25,"count":69,"monster_list":[{"name":"枉死怨靈","count":13,"percent":"18.8%"},{"name":"礦石元素","count":25,"percent":"36.2%"},{"name":"闇矮人礦工","count":22,"percent":"31.9%"},{"name":"發瘋劍士","count":5,"percent":"7.2%"},{"name":"隱藏寶箱","count":4,"percent":"5.8%"}]},{"level":26,"count":62,"monster_list":[{"name":"礦石元素","count":29,"percent":"46.8%"},{"name":"闇矮人礦工","count":25,"percent":"40.3%"},{"name":"隱藏寶箱","count":5,"percent":"8.1%"},{"name":"枉死怨靈","count":2,"percent":"3.2%"},{"name":"發瘋劍士","count":1,"percent":"1.6%"}]},{"level":27,"count":61,"monster_list":[{"name":"闇矮人礦工","count":20,"percent":"32.8%"},{"name":"礦石元素","count":18,"percent":"29.5%"},{"name":"發瘋劍士","count":6,"percent":"9.8%"},{"name":"隱藏寶箱","count":7,"percent":"11.5%"},{"name":"熔爐騎士","count":4,"percent":"6.6%"},{"name":"枉死怨靈","count":6,"percent":"9.8%"}]},{"level":28,"count":50,"monster_list":[{"name":"礦石元素","count":22,"percent":"44.0%"},{"name":"闇矮人礦工","count":12,"percent":"24.0%"},{"name":"枉死怨靈","count":10,"percent":"20.0%"},{"name":"隱藏寶箱","count":5,"percent":"10.0%"},{"name":"發瘋劍士","count":1,"percent":"2.0%"}]},{"level":29,"count":52,"monster_list":[{"name":"礦石元素","count":24,"percent":"46.2%"},{"name":"闇矮人礦工","count":14,"percent":"26.9%"},{"name":"枉死怨靈","count":8,"percent":"15.4%"},{"name":"隱藏寶箱","count":5,"percent":"9.6%"},{"name":"熔爐騎士","count":1,"percent":"1.9%"}]},{"level":30,"count":49,"monster_list":[{"name":"闇矮人礦工","count":13,"percent":"26.5%"},{"name":"礦石元素","count":25,"percent":"51.0%"},{"name":"隱藏寶箱","count":6,"percent":"12.2%"},{"name":"枉死怨靈","count":5,"percent":"10.2%"}]},{"level":31,"count":47,"monster_list":[{"name":"闇矮人礦工","count":16,"percent":"34.0%"},{"name":"隱藏寶箱","count":5,"percent":"10.6%"},{"name":"礦石元素","count":23,"percent":"48.9%"},{"name":"枉死怨靈","count":2,"percent":"4.3%"},{"name":"發瘋劍士","count":1,"percent":"2.1%"}]},{"level":32,"count":41,"monster_list":[{"name":"隱藏寶箱","count":6,"percent":"14.6%"},{"name":"枉死怨靈","count":3,"percent":"7.3%"},{"name":"闇矮人礦工","count":7,"percent":"17.1%"},{"name":"礦石元素","count":20,"percent":"48.8%"},{"name":"熔爐騎士","count":3,"percent":"7.3%"},{"name":"發瘋劍士","count":2,"percent":"4.9%"}]},{"level":33,"count":34,"monster_list":[{"name":"發瘋劍士","count":2,"percent":"5.9%"},{"name":"礦石元素","count":17,"percent":"50.0%"},{"name":"隱藏寶箱","count":6,"percent":"17.6%"},{"name":"枉死怨靈","count":4,"percent":"11.8%"},{"name":"闇矮人礦工","count":3,"percent":"8.8%"},{"name":"熔爐騎士","count":2,"percent":"5.9%"}]},{"level":34,"count":26,"monster_list":[{"name":"枉死怨靈","count":9,"percent":"34.6%"},{"name":"隱藏寶箱","count":5,"percent":"19.2%"},{"name":"礦石元素","count":5,"percent":"19.2%"},{"name":"闇矮人礦工","count":4,"percent":"15.4%"},{"name":"熔爐騎士","count":2,"percent":"7.7%"},{"name":"發瘋劍士","count":1,"percent":"3.8%"}]},{"level":35,"count":30,"monster_list":[{"name":"礦石元素","count":13,"percent":"43.3%"},{"name":"隱藏寶箱","count":4,"percent":"13.3%"},{"name":"發瘋劍士","count":5,"percent":"16.7%"},{"name":"闇矮人礦工","count":6,"percent":"20.0%"},{"name":"枉死怨靈","count":2,"percent":"6.7%"}]},{"level":36,"count":18,"monster_list":[{"name":"礦石元素","count":9,"percent":"50.0%"},{"name":"枉死怨靈","count":2,"percent":"11.1%"},{"name":"闇矮人礦工","count":5,"percent":"27.8%"},{"name":"隱藏寶箱","count":1,"percent":"5.6%"},{"name":"熔爐騎士","count":1,"percent":"5.6%"}]},{"level":37,"count":12,"monster_list":[{"name":"礦石元素","count":4,"percent":"33.3%"},{"name":"闇矮人礦工","count":3,"percent":"25.0%"},{"name":"枉死怨靈","count":1,"percent":"8.3%"},{"name":"熔爐騎士","count":3,"percent":"25.0%"},{"name":"隱藏寶箱","count":1,"percent":"8.3%"}]},{"level":38,"count":5,"monster_list":[{"name":"枉死怨靈","count":2,"percent":"40.0%"},{"name":"礦石元素","count":2,"percent":"40.0%"},{"name":"熔爐騎士","count":1,"percent":"20.0%"}]},{"level":39,"count":2,"monster_list":[{"name":"礦石元素","count":1,"percent":"50.0%"},{"name":"枉死怨靈","count":1,"percent":"50.0%"}]},{"level":40,"count":3,"monster_list":[{"name":"枉死怨靈","count":1,"percent":"33.3%"},{"name":"礦石元素","count":2,"percent":"66.7%"}]}]},{"name":"蝙蝠洞","dialog":false,"monster_list":[{"level":[1,25],"name":"老鼠","type":"動物","loot":[{"type":"好運石","count":147},{"type":"黑曜石","count":34},{"type":"蘋果","count":301},{"type":"銅礦","count":344},{"type":"採礦入門書","count":119},{"type":"採礦密技","count":30},{"type":"技能書：重擊","count":21}]},{"level":[1,32],"name":"蝙蝠","type":"動物","loot":[{"type":"荔枝","count":1007},{"type":"黑曜石","count":221},{"type":"蘋果","count":157},{"type":"夜明砂","count":835},{"type":"採礦入門書","count":125},{"type":"採礦密技","count":55},{"type":"生化藥劑","count":6}]},{"level":[1,28],"name":"大老鼠","type":"動物","loot":[{"type":"蘋果","count":382},{"type":"好運石","count":125},{"type":"採礦密技","count":43},{"type":"銅礦","count":271},{"type":"技能書：重擊","count":78},{"type":"金礦","count":136},{"type":"黑曜石","count":25},{"type":"採礦入門書","count":46}]},{"level":[1,33],"name":"大蝙蝠","type":"動物","loot":[{"type":"生化藥劑","count":23},{"type":"採礦密技","count":281},{"type":"黑曜石","count":174},{"type":"夜明砂","count":981},{"type":"荔枝","count":1474},{"type":"蘋果","count":195},{"type":"老礦工的日記","count":46}]},{"level":[15,27],"name":"小拳石","type":"不明","loot":[{"type":"採礦入門書","count":4},{"type":"鑽石","count":13},{"type":"石頭","count":129},{"type":"採礦密技","count":3},{"type":"鈹","count":15},{"type":"好運石","count":2}]},{"level":[17,29],"name":"蝙蝠俠","type":"人類","loot":[{"type":"克維拉","count":18},{"type":"黑曜石","count":2},{"type":"夜明砂","count":3}]},{"level":[21,21],"name":"米老鼠","type":"不明","loot":[]}],"level_list":[{"level":1,"count":387,"monster_list":[{"name":"老鼠","count":76,"percent":"19.6%"},{"name":"蝙蝠","count":198,"percent":"51.2%"},{"name":"大蝙蝠","count":82,"percent":"21.2%"},{"name":"大老鼠","count":31,"percent":"8.0%"}]},{"level":2,"count":382,"monster_list":[{"name":"蝙蝠","count":204,"percent":"53.4%"},{"name":"大蝙蝠","count":65,"percent":"17.0%"},{"name":"大老鼠","count":40,"percent":"10.5%"},{"name":"老鼠","count":73,"percent":"19.1%"}]},{"level":3,"count":378,"monster_list":[{"name":"老鼠","count":62,"percent":"16.4%"},{"name":"蝙蝠","count":191,"percent":"50.5%"},{"name":"大蝙蝠","count":86,"percent":"22.8%"},{"name":"大老鼠","count":39,"percent":"10.3%"}]},{"level":4,"count":374,"monster_list":[{"name":"老鼠","count":79,"percent":"21.1%"},{"name":"蝙蝠","count":203,"percent":"54.3%"},{"name":"大蝙蝠","count":71,"percent":"19.0%"},{"name":"大老鼠","count":21,"percent":"5.6%"}]},{"level":5,"count":370,"monster_list":[{"name":"大老鼠","count":60,"percent":"16.2%"},{"name":"蝙蝠","count":174,"percent":"47.0%"},{"name":"老鼠","count":67,"percent":"18.1%"},{"name":"大蝙蝠","count":69,"percent":"18.6%"}]},{"level":6,"count":368,"monster_list":[{"name":"蝙蝠","count":181,"percent":"49.2%"},{"name":"老鼠","count":80,"percent":"21.7%"},{"name":"大老鼠","count":52,"percent":"14.1%"},{"name":"大蝙蝠","count":55,"percent":"14.9%"}]},{"level":7,"count":358,"monster_list":[{"name":"老鼠","count":82,"percent":"22.9%"},{"name":"蝙蝠","count":172,"percent":"48.0%"},{"name":"大蝙蝠","count":69,"percent":"19.3%"},{"name":"大老鼠","count":35,"percent":"9.8%"}]},{"level":8,"count":352,"monster_list":[{"name":"大蝙蝠","count":54,"percent":"15.3%"},{"name":"大老鼠","count":39,"percent":"11.1%"},{"name":"老鼠","count":75,"percent":"21.3%"},{"name":"蝙蝠","count":184,"percent":"52.3%"}]},{"level":9,"count":323,"monster_list":[{"name":"蝙蝠","count":173,"percent":"53.6%"},{"name":"老鼠","count":79,"percent":"24.5%"},{"name":"大蝙蝠","count":57,"percent":"17.6%"},{"name":"大老鼠","count":14,"percent":"4.3%"}]},{"level":10,"count":298,"monster_list":[{"name":"老鼠","count":62,"percent":"20.8%"},{"name":"大蝙蝠","count":67,"percent":"22.5%"},{"name":"蝙蝠","count":133,"percent":"44.6%"},{"name":"大老鼠","count":36,"percent":"12.1%"}]},{"level":11,"count":260,"monster_list":[{"name":"蝙蝠","count":134,"percent":"51.5%"},{"name":"大老鼠","count":27,"percent":"10.4%"},{"name":"大蝙蝠","count":38,"percent":"14.6%"},{"name":"老鼠","count":61,"percent":"23.5%"}]},{"level":12,"count":229,"monster_list":[{"name":"大老鼠","count":20,"percent":"8.7%"},{"name":"蝙蝠","count":109,"percent":"47.6%"},{"name":"大蝙蝠","count":48,"percent":"21.0%"},{"name":"老鼠","count":52,"percent":"22.7%"}]},{"level":13,"count":199,"monster_list":[{"name":"蝙蝠","count":103,"percent":"51.8%"},{"name":"大蝙蝠","count":42,"percent":"21.1%"},{"name":"大老鼠","count":27,"percent":"13.6%"},{"name":"老鼠","count":27,"percent":"13.6%"}]},{"level":14,"count":184,"monster_list":[{"name":"蝙蝠","count":82,"percent":"44.6%"},{"name":"大蝙蝠","count":32,"percent":"17.4%"},{"name":"大老鼠","count":17,"percent":"9.2%"},{"name":"老鼠","count":53,"percent":"28.8%"}]},{"level":15,"count":167,"monster_list":[{"name":"小拳石","count":13,"percent":"7.8%"},{"name":"蝙蝠","count":61,"percent":"36.5%"},{"name":"老鼠","count":46,"percent":"27.5%"},{"name":"大老鼠","count":16,"percent":"9.6%"},{"name":"大蝙蝠","count":31,"percent":"18.6%"}]},{"level":16,"count":133,"monster_list":[{"name":"大蝙蝠","count":21,"percent":"15.8%"},{"name":"蝙蝠","count":55,"percent":"41.4%"},{"name":"老鼠","count":35,"percent":"26.3%"},{"name":"大老鼠","count":10,"percent":"7.5%"},{"name":"小拳石","count":12,"percent":"9.0%"}]},{"level":17,"count":102,"monster_list":[{"name":"老鼠","count":29,"percent":"28.4%"},{"name":"小拳石","count":13,"percent":"12.7%"},{"name":"蝙蝠","count":31,"percent":"30.4%"},{"name":"大蝙蝠","count":10,"percent":"9.8%"},{"name":"大老鼠","count":12,"percent":"11.8%"},{"name":"蝙蝠俠","count":7,"percent":"6.9%"}]},{"level":18,"count":79,"monster_list":[{"name":"大老鼠","count":8,"percent":"10.1%"},{"name":"蝙蝠","count":29,"percent":"36.7%"},{"name":"小拳石","count":9,"percent":"11.4%"},{"name":"大蝙蝠","count":9,"percent":"11.4%"},{"name":"蝙蝠俠","count":5,"percent":"6.3%"},{"name":"老鼠","count":19,"percent":"24.1%"}]},{"level":19,"count":54,"monster_list":[{"name":"小拳石","count":4,"percent":"7.4%"},{"name":"蝙蝠俠","count":3,"percent":"5.6%"},{"name":"老鼠","count":19,"percent":"35.2%"},{"name":"蝙蝠","count":21,"percent":"38.9%"},{"name":"大蝙蝠","count":4,"percent":"7.4%"},{"name":"大老鼠","count":3,"percent":"5.6%"}]},{"level":20,"count":43,"monster_list":[{"name":"小拳石","count":4,"percent":"9.3%"},{"name":"老鼠","count":13,"percent":"30.2%"},{"name":"大蝙蝠","count":3,"percent":"7.0%"},{"name":"蝙蝠","count":20,"percent":"46.5%"},{"name":"蝙蝠俠","count":2,"percent":"4.7%"},{"name":"大老鼠","count":1,"percent":"2.3%"}]},{"level":21,"count":37,"monster_list":[{"name":"蝙蝠","count":8,"percent":"21.6%"},{"name":"大蝙蝠","count":9,"percent":"24.3%"},{"name":"老鼠","count":7,"percent":"18.9%"},{"name":"小拳石","count":4,"percent":"10.8%"},{"name":"大老鼠","count":7,"percent":"18.9%"},{"name":"米老鼠","count":1,"percent":"2.7%"},{"name":"蝙蝠俠","count":1,"percent":"2.7%"}]},{"level":22,"count":27,"monster_list":[{"name":"蝙蝠","count":9,"percent":"33.3%"},{"name":"老鼠","count":9,"percent":"33.3%"},{"name":"小拳石","count":4,"percent":"14.8%"},{"name":"大老鼠","count":4,"percent":"14.8%"},{"name":"大蝙蝠","count":1,"percent":"3.7%"}]},{"level":23,"count":20,"monster_list":[{"name":"蝙蝠","count":7,"percent":"35.0%"},{"name":"老鼠","count":6,"percent":"30.0%"},{"name":"蝙蝠俠","count":3,"percent":"15.0%"},{"name":"小拳石","count":2,"percent":"10.0%"},{"name":"大蝙蝠","count":2,"percent":"10.0%"}]},{"level":24,"count":14,"monster_list":[{"name":"老鼠","count":3,"percent":"21.4%"},{"name":"小拳石","count":2,"percent":"14.3%"},{"name":"大蝙蝠","count":2,"percent":"14.3%"},{"name":"蝙蝠","count":4,"percent":"28.6%"},{"name":"蝙蝠俠","count":2,"percent":"14.3%"},{"name":"大老鼠","count":1,"percent":"7.1%"}]},{"level":25,"count":8,"monster_list":[{"name":"老鼠","count":2,"percent":"25.0%"},{"name":"小拳石","count":2,"percent":"25.0%"},{"name":"蝙蝠","count":2,"percent":"25.0%"},{"name":"大蝙蝠","count":1,"percent":"12.5%"},{"name":"大老鼠","count":1,"percent":"12.5%"}]},{"level":26,"count":4,"monster_list":[{"name":"蝙蝠","count":3,"percent":"75.0%"},{"name":"小拳石","count":1,"percent":"25.0%"}]},{"level":27,"count":3,"monster_list":[{"name":"蝙蝠","count":1,"percent":"33.3%"},{"name":"小拳石","count":1,"percent":"33.3%"},{"name":"大蝙蝠","count":1,"percent":"33.3%"}]},{"level":28,"count":2,"monster_list":[{"name":"大老鼠","count":2,"percent":"100.0%"}]},{"level":29,"count":1,"monster_list":[{"name":"蝙蝠俠","count":1,"percent":"100.0%"}]},{"level":30,"count":1,"monster_list":[{"name":"大蝙蝠","count":1,"percent":"100.0%"}]},{"level":31,"count":1,"monster_list":[{"name":"大蝙蝠","count":1,"percent":"100.0%"}]},{"level":32,"count":1,"monster_list":[{"name":"蝙蝠","count":1,"percent":"100.0%"}]},{"level":33,"count":1,"monster_list":[{"name":"大蝙蝠","count":1,"percent":"100.0%"}]}]}],
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
      ],
      hunt_events_loading: false,
      castle_events_loading: false,
      hunts_loading: false,
      weapon_type_count_loading: false,
    }
  },
  mounted: async function () {
    this.hunt_events = await api.getData(this.$route.params.round + "/hunt_events")
    this.hunt_events_loading = true
    this.castle_events = await api.getData(this.$route.params.round + "/castle_events")
    this.castle_events_loading = true
    this.hunts = await api.getData(this.$route.params.round + "/hunts")
    this.hunts_loading = true
    this.weapon_type_count = await api.getData(this.$route.params.round + "/weapon_type_count")
    this.weapon_type_count_loading = true

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

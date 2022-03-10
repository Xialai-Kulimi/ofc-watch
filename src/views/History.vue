<template>
  <v-container
  >
    <v-card v-if="loading" class="pa-5">
      <v-card-title>戰報</v-card-title>
      <v-card-subtitle>還原歷史經過</v-card-subtitle>
      <v-card-text>在：<strong>{{report.report.location}}</strong></v-card-text>
      <v-divider></v-divider>
      <v-container
          fluid
          style="display: flex"
          class="align-left wrap"
      >
        <v-container>
          <v-card-title>攻擊方</v-card-title>
          <v-simple-table
              dense
          >
            <template v-slot:default>

              <tbody>
              <tr><th>陣營</th><td>{{report.report.aFactionName}}</td></tr>
              <tr><th>玩家</th><td><router-link :to="compose_player_link(report.report.aId)">{{report.report.messages.stats.a.name}}</router-link></td></tr>
              <tr><th>職業</th><td>{{report.report.messages.stats.a.role}}</td></tr>
              <tr v-if="report.report.messages.stats.a.role2"><th>副職</th><td>{{report.report.messages.stats.a.role2}}</td></tr>
              <tr><th>HP</th><td>{{report.report.messages.stats.a.hp}}</td></tr>
              <tr><th>熟練</th><td>{{report.report.messages.stats.a.fightExp}}</td></tr>
              <tr><th>ID</th><td>{{report.report.aId}}</td></tr>
              <tr>
                <th>裝備</th>
                <td>
                  <p v-for="(item) in report.report.messages.stats.a.equipments" :key="item">
                    {{item.quality}}的 <b>{{item.name}}</b>（{{item.type}}）<b>攻擊</b>{{item.atk}}、<b>防禦</b>{{item.def}}、<b>礦力</b>{{item.minePower}}
                  </p>
                </td>
              </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-container>
        <v-container>
          <v-card-title>防守方</v-card-title>
          <v-simple-table
              dense
          >
            <template v-slot:default>

              <tbody>
              <tr><th>陣營</th><td>{{report.report.bFactionName}}</td></tr>
              <tr><th>玩家</th><td><router-link :to="compose_player_link(report.report.bId)">{{report.report.messages.stats.b.name}}</router-link></td></tr>
              <tr><th>職業</th><td>{{report.report.messages.stats.b.role}}</td></tr>
              <tr v-if="report.report.messages.stats.b.role2"><th>副職</th><td>{{report.report.messages.stats.b.role2}}</td></tr>
              <tr><th>HP</th><td>{{report.report.messages.stats.b.hp}}</td></tr>
              <tr><th>熟練</th><td>{{report.report.messages.stats.b.fightExp}}</td></tr>
              <tr><th>ID</th><td>{{report.report.bId}}</td></tr>
              <tr><th>裝備</th><td><p v-for="(item) in report.report.messages.stats.b.equipments" :key="item">
                {{item.quality}}的 <b>{{item.name}}</b>（{{item.type}}）<b>攻擊</b>{{item.atk}}、<b>防禦</b>{{item.def}}、<b>礦力</b>{{item.minePower}}
              </p></td></tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-container>
      </v-container>
        <v-container>
          <v-card-subtitle>{{format_time}}</v-card-subtitle>
          <table>
            <tr v-for="(item, index) in report.report.messages.messages" :key="item">
              <th>{{index+1}}</th><td :class="color_to_class(item.s)">{{item.m}}</td>
            </tr>
          </table>
        </v-container>
    </v-card>
    <v-card v-if="!loading"><p>正在載入戰報</p></v-card>
  </v-container>

</template>

<script>
import api from "@/api";

export default {
  name: "History",
  components: {},
  data() {
    return {
      loading: true,
      format_time: "54545454",
      report: {"report":{"id":38856,"messages":{"messages":[{"m":"大舉進攻攻擊用臉接球造成 103 點傷害"},{"m":"用臉接球攻擊，但是大舉進攻完全不痛不癢"},{"m":"大舉進攻的RM你好遜 又好爛 好輸散出毒孢子","s":"skill"},{"m":"大舉進攻攻擊用臉接球造成 376 點傷害"},{"m":"用臉接球被擊殺身亡了，大舉進攻還有 200 點體力","s":"critical"},{"m":"斯耗損了 7 點耐久","s":"info"},{"m":"肥桐的屁眼耗損了 7 點耐久","s":"info"},{"m":"RM你好遜 又好爛 好輸耗損了 5 點耐久","s":"info"},{"m":"RM你好遜 又好爛 好輸耗損了 5 點耐久","s":"info"},{"m":"回收耗損了 5 點耐久","s":"info"},{"m":"你真的太無情了耗損了 4 點耐久","s":"info"},{"m":"野人山田耗損了 6 點耐久","s":"info"},{"m":"王冠耗損了 8 點耐久","s":"info"},{"m":"捏捏不死於過胖耗損了 6 點耐久","s":"info"},{"m":"用臉接球獲得了 7 點經驗值","s":"info"}],"stats":{"a":{"name":"大舉進攻","role":"戰鬥員","hp":200,"fightExp":3962,"equipments":[{"name":"RM你好遜 又好爛 好輸","quality":"精良","type":"單手劍","atk":3251,"def":3295,"minePower":599},{"name":"RM你好遜 又好爛 好輸","quality":"普通","type":"毒菇九劍","atk":1033,"def":1013,"minePower":79},{"name":"你真的太無情了","quality":"上等","type":"口罩","atk":206,"def":88,"minePower":167},{"name":"王冠","quality":"普通","type":"礦工帽","atk":7,"def":53,"minePower":36}],"role2":"衛兵"},"b":{"name":"用臉接球","role":"戰鬥員","hp":200,"fightExp":241,"equipments":[{"name":"斯","quality":"傳說","type":"礦靴","atk":192,"def":177,"minePower":232},{"name":"肥桐的屁眼","quality":"上等","type":"臭豆斧","atk":418,"def":290,"minePower":123},{"name":"回收","quality":"普通","type":"口罩","atk":72,"def":43,"minePower":63},{"name":"野人山田","quality":"上等","type":"礦工帽","atk":609,"def":431,"minePower":756},{"name":"捏捏不死於過胖","quality":"上等","type":"寒冰屠龍劍","atk":804,"def":891,"minePower":622}]}}},"location":"我的桐人3的城堡","time":1646831460863,"aFactionName":"我的桐人3","bFactionName":"浮游城2","aName":"大舉進攻","bName":"用臉接球","aId":587,"bId":1192,"aBadgeColor":null,"bBadgeColor":null}}

    }
  },
  methods: {
    color_to_class(color) {
      if (color === "critical") {
        color = 'red'
      }
      if (color === "skill") {
        color = 'cyan'
      }
      return color + '--text'
    },
    compose_player_link(id) {
      return '/'+localStorage.round+'/player/'+id
    }
  },
  mounted: async function () {
    this.report = await api.getData( this.$route.params.round +"/history/"+this.$route.params.id)
    this.format_time = (new Date(this.report.report.time)).toLocaleString()
    this.loading = true
  }

}
</script>

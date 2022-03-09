<template>
  <v-container>
    <v-card v-if="loading" class="pa-5">
      <v-card-title>戰報</v-card-title>
      <v-card-subtitle>還原歷史經過</v-card-subtitle>
      <v-card-text>在：<strong>{{report.report.location}}</strong></v-card-text>
      <v-divider></v-divider>
      <v-card-title>攻擊方</v-card-title>
      <table>
        <tr><th>陣營</th><td>{{report.report.aFactionName}}</td></tr>
        <tr><th>玩家</th><td>{{report.report.messages.stats.a.name}}</td></tr>
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

      </table>
          <hr>
          <div>
            <b><i>防守方</i></b>
            <div v-if="report.report.messages.stats.b"><table class="player-table">
              <tr><th>陣營</th><td>{{report.report.bFactionName}}</td></tr>
              <tr><th>玩家</th><td>{{report.report.messages.stats.b.name}}</td></tr>
              <tr><th>職業</th><td>{{report.report.messages.stats.b.role}}</td></tr>
              <tr v-if="report.report.messages.stats.b.role2"><th>副職</th><td>{{report.report.messages.stats.b.role2}}</td></tr>
              <tr><th>HP</th><td>{{report.report.messages.stats.b.hp}}</td></tr>
              <tr><th>熟練</th><td>{{report.report.messages.stats.b.fightExp}}</td></tr>
              <tr><th>ID</th><td>{{report.report.bId}}</td></tr>
              <tr><th>裝備</th><td><p v-for="(item) in report.report.messages.stats.b.equipments" :key="item">
                {{item.quality}}的 <b>{{item.name}}</b>（{{item.type}}）<b>攻擊</b>{{item.atk}}、<b>防禦</b>{{item.def}}、<b>礦力</b>{{item.minePower}}
              </p></td></tr>
            </table></div>
            <div v-if="!report.report.messages.stats.b">{{report.report.location}}</div>
          </div>

        <hr>
        <div>
          <p>{{format_time}}</p>
          <table>
            <tr v-for="(item, index) in report.report.messages.messages" :key="item">
              <th>{{index+1}}</th><td :class="color_to_class(item.s)">{{item.m}}</td>
            </tr>
          </table>
        </div>

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
      report: {"report": {"id": 352, "messages": {"messages": [{"m": "芒果乾j1攻擊，但是魔三玖完全不痛不癢"}, {"m": "魔三玖攻擊芒果乾j1造成 129 點傷害"}, {"m": "芒果乾j1攻擊，但是被魔三玖格擋了"}, {"m": "魔三玖攻擊芒果乾j1造成 156 點傷害"}, {"m": "芒果乾j1被擊殺身亡了，魔三玖還有 200 點體力", "s": "critical"}, {"m": "武漢肺炎耗損了 5 點耐久", "s": "info"}, {"m": "黑夜大衣耗損了 8 點耐久", "s": "info"}, {"m": "芒果乾j1獲得了 2 點經驗值", "s": "info"}], "stats": {"a": {"name": "芒果乾j1", "role": "戰鬥員", "hp": 200, "fightExp": 0, "equipments": []}, "b": {"name": "魔三玖", "role": "戰鬥員", "hp": 200, "fightExp": 123, "equipments": [{"name": "武漢肺炎", "quality": "普通", "type": "長槍", "atk": 522, "def": 516, "minePower": 11}, {"name": "黑夜大衣", "quality": "頂級", "type": "大衣", "atk": 10, "def": 150, "minePower": 25}]}}}, "location": "中国共产党的城堡", "time": 1620540688736, "aFactionName": "時代力量", "bFactionName": "中国共产党", "aName": "芒果乾j1", "bName": "魔三玖", "aId": 2440, "bId": 94, "aBadgeColor": null, "bBadgeColor": null}}

    }
  },
  methods: {
    color_to_class(color) {
      if (color === "critical") {
        color = 'red'
      }
      return color + '--text'
    }
  },
  mounted: async function () {
    this.report = await api.getReport( this.$route.params.round +"/"+this.$route.params.id + ".json")
    this.format_time = (new Date(this.report.report.time)).toLocaleString()
    this.loading = true
  }

}
</script>

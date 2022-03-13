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
              <tr v-if="report.report.bFactionName"><th>陣營</th><td>{{report.report.bFactionName}}</td></tr>
              <tr><th>玩家</th><td><router-link v-if="report.report.bId" :to="compose_player_link(report.report.bId)">{{report.report.messages.stats.b.name}}</router-link><div v-if="!report.report.bId">{{report.report.messages.stats.b.name}}</div></td></tr>
              <tr><th>職業</th><td>{{report.report.messages.stats.b.role}}</td></tr>
              <tr v-if="report.report.messages.stats.b.role2"><th>副職</th><td>{{report.report.messages.stats.b.role2}}</td></tr>
              <tr><th>HP</th><td>{{report.report.messages.stats.b.hp}}</td></tr>
              <tr v-if="report.report.messages.stats.b.atk"><th>攻擊</th><td>{{report.report.messages.stats.b.atk}}</td></tr>
              <tr v-if="report.report.messages.stats.b.def"><th>防禦</th><td>{{report.report.messages.stats.b.def}}</td></tr>
              <tr><th>熟練</th><td>{{report.report.messages.stats.b.fightExp}}</td></tr>
              <tr v-if="report.report.bId"><th>ID</th><td>{{report.report.bId}}</td></tr>
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
      loading: false,
      format_time: "54545454",
      report: {}
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
      return '/'+this.$route.params.round+'/player/'+id
    }
  },
  mounted: async function () {
    this.report = await api.getData( this.$route.params.round +"/report/"+this.$route.params.id)
    this.format_time = (new Date(this.report.report.time)).toLocaleString()
    this.loading = true
  }

}
</script>

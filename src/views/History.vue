<template>
  <div class="row-div2" id="base" v-if="loading">
    <div id="report-box">
      <div class="row2"><h1>戰報</h1><p>還原歷史經過</p></div>
      <table>
        <tr><th>在 </th><td>{{report.report.location}}</td></tr>
      </table>
      <div id="info-box" class="row">

        <div class="player">
          <b><i>攻擊方</i></b>
          <table class="player-table">
            <tr><th>陣營</th><td>{{report.report.aFactionName}}</td></tr>
            <tr><th>玩家</th><td>{{report.report.messages.stats.a.name}}</td></tr>
            <tr><th>職業</th><td>{{report.report.messages.stats.a.role}}</td></tr>
            <tr v-if="report.report.messages.stats.a.role2"><th>副職</th><td>{{report.report.messages.stats.a.role2}}</td></tr>
            <tr><th>HP</th><td>{{report.report.messages.stats.a.hp}}</td></tr>
            <tr><th>熟練</th><td>{{report.report.messages.stats.a.fightExp}}</td></tr>
            <tr><th>ID</th><td>{{report.report.aId}}</td></tr>
            <tr><th>裝備</th><td><p v-for="(item) in report.report.messages.stats.a.equipments" :key="item">
              {{item.quality}}的 <b>{{item.name}}</b>（{{item.type}}）<b>攻擊</b>{{item.atk}}、<b>防禦</b>{{item.def}}、<b>礦力</b>{{item.minePower}}
            </p></td></tr>
         </table>
        </div>
        <hr align="center" width="87%" id="player-split" >
        <div class="player">
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
      </div>
      <hr align="center" width="87%" style="margin-bottom: 25px;margin-top: 25px;border-color: rgba(12, 34, 56, 0.5)">
      <div id="message-box">
        <p>{{format_time}}</p>
        <table id="message-table">
          <tr v-for="(item, index) in report.report.messages.messages" :key="item">
            <th>{{index+1}}</th><td :class="item.s">{{item.m}}</td>
          </tr>
        </table>
      </div>
    </div>
    <div v-if="!loading"><p>正在載入戰報</p></div>
  </div>

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

  mounted: async function () {
    this.report = await api.getReport( this.$route.params.round +"/"+this.$route.params.id + ".json")
    this.format_time = (new Date(this.report.report.time)).toLocaleString()
    this.loading = true
  }

}
</script>

<style scoped lang="scss">

h1 {
  margin-top: 0;
  margin-bottom: 10px;
  display: flex;

}

#player-split{
  display: none;

  border-color: rgba(12, 34, 56, 0.2);
  @include phone-width{
    display: block;
  }
  @include small-pad-width {
    display: block;
  }
}

#report-box{
  box-shadow:3px 3px 5px 6px #cccccc;
  width: 60%;
  padding: 30px;
  @include phone-width{
    padding: 10px;
    width: 90%;
  }
  @include small-pad-width {
    padding: 10px;
    width: 90%;
  }

}

.player{
  width: 50%;
  display: flex;
  text-align: left;
  flex-flow: column;

  @include phone-width{
    width: 100%;
  }
  @include small-pad-width {
    width: 100%;
  }
}

.player-table > tr > td{
  display: flex;
  flex-flow: column;
  text-align: left;
  padding-left: 10px;

}

.player-table > tr > th {
}

.player-table > tr > * {


}

#message-table > tr > td{
  display: flex;

  text-align: left;
  padding-left: 12px;
}

.player-table > tr > th{
  min-width: 50px;
}

.player-table > tr > td > p{
  margin: 0;
}


#base{
  margin-bottom: 20px;
}


.row{
  display: flex;
  flex-direction: row;
  @include phone-width{
    flex-flow: column;
  }
  @include small-pad-width {
    flex-flow: column;
  }
}

.row2{
  display: flex;
  flex-direction: row;
}

.skill{
  color: #00887e;
}

.info{
  color: #006da7;
}

.critical{
  color: #ff1200;
}

p{
  margin: 15px;
}

</style>
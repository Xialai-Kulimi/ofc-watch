<template>
  <v-container>
    <v-card v-if="loading">
      <v-card-title>會戰紀錄</v-card-title>
        <v-card-text>
            在 <b>{{ match.location }}</b> <br>
            會戰編號：<b>{{ match.id }}</b><br>
            從 <b>{{ format_time(match.startTime) }}</b> 到
            <b>{{ format_time(match.endTime) }}</b>，歷時{{ format_past_time(match.endTime - match.startTime) }}<br>
            攻擊方共<b>{{ match.atk_player.length }}</b>人，防守方共<b>{{ match.def_player.length }}</b>人<br>
            從第 <b>{{ match.initCastle[0] }}</b> 層，血量 <b>{{ match.initCastle[1] }}</b>，打到第
            <b>{{ match.finalCastle[0] }}</b> 層，血量 <b>{{ match.finalCastle[1] }}</b>
        </v-card-text>


      <!--scoreboard-->

      <v-container
          fluid
          row
      >
        <v-container>
          <v-card-title>攻擊方</v-card-title>
          <v-simple-table>
            <template v-slot:default>
              <thead>
              <tr>
                <th>名稱</th>
                <th>職業</th>
                <th>副職業</th>
                <th>陣營</th>
                <th>擊殺</th>
                <th>被擊殺</th>
                <th>助攻</th>
                <th>造成傷害</th>
                <th>承受傷害</th>
                <th>對城傷害</th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="player in match.atk_player" v-bind:key="player">
                <td>{{ player.name }}</td>
                <td>{{ player.role }}</td>
                <td>{{ player.role2 }}</td>
                <td>{{ player.faction }}</td>
                <td>{{ player.kill }}</td>
                <td>{{ player.killed }}</td>
                <td>{{ player.assist }}</td>
                <td>{{ player.damage }}</td>
                <td>{{ player.damaged }}</td>
                <td>{{ player.castleDamage }}</td>
              </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-container>
        <v-divider></v-divider>
        <v-container>
          <v-card-title>防守方</v-card-title>
          <v-simple-table>
            <template v-slot:default>
              <thead>
              <tr>
                <th>名稱</th>
                <th>職業</th>
                <th>副職業</th>
                <th>陣營</th>
                <th>擊殺</th>
                <th>被擊殺</th>
                <th>助攻</th>
                <th>造成傷害</th>
                <th>承受傷害</th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="player in match.def_player" v-bind:key="player">
                <td>{{ player.name }}</td>
                <td>{{ player.role }}</td>
                <td>{{ player.role2 }}</td>
                <td>{{ player.faction }}</td>
                <td>{{ player.kill }}</td>
                <td>{{ player.killed }}</td>
                <td>{{ player.assist }}</td>
                <td>{{ player.damage }}</td>
                <td>{{ player.damaged }}</td>
              </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-container>

      </v-container>
      <!--loot_list-->
        <v-container>
          <v-card-title>獲得樓層獎勵</v-card-title>
          <v-simple-table>
            <template v-slot:default>
              <thead>
              <tr>
                <th>層數</th>
                <th>種類</th>
                <th>品質</th>
                <th>名稱</th>
                <th>攻擊</th>
                <th>防禦</th>
                <th>挖礦</th>
                <th>獲得者</th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="(item) in match.loot" :key="item">
                <td>{{ item.floor }}</td>
                <td>{{ item.name }}</td>
                <td>{{ item.quality }}</td>
                <td>{{ item.type }}
                <td>{{ item.atk }}</td>
                <td>{{ item.def }}</td>
                <td>{{ item.minePower }}</td>
                <td>{{ item.owner }}</td>
              </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-container>
      <!--report_list-->
        <v-container>
          <v-card-subtitle>暱稱為紅色者代表在戰鬥中死亡。</v-card-subtitle>
          <v-simple-table>
            <template v-slot:default>
              <thead>
              <tr><th>時間</th><th>進攻方</th><th>防守方</th><th>備註</th><th>id</th></tr>
              </thead>
              <tbody>
              <tr v-for="report in match.report_list" v-bind:key="report">
                <td>{{format_time(report.time)}}</td>
                <td>{{report.atk_f}} 的
                  <router-link
                    v-bind:to="'/player/'+report.atk_id"
                    v-bind:class="{'red--text': report.dead.includes(report.atk_name)}"
                  >
                    {{report.atk_name}}
                  </router-link></td>
                <td
                    v-bind:class="{'red--text': report.dead.includes(report.def_name)}"
                >
                  {{report.def_f}} 的
                  <router-link v-if="report.def_name" v-bind:to="'/player/'+report.def_id">{{report.def_name}}</router-link>
                  {{(report.def_name) ? none : "牆壁"}}
                </td>
                <td>{{report.remarks}}</td>
                <td><router-link class="player-link" v-bind:to="compose_report_link(report.id)">{{report.id}}</router-link></td>
              </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-container>
    </v-card>
    <div v-if="!loading">資料載入中</div>
    <v-card>

    </v-card>
<!--    {{this.$route.params}} {{this.$route.params.round}}-->
  </v-container>
</template>
<script>

export default {
  name: "Search",
  data() {
    return {
      loading: true,
      match: {
        startTime: 234566809898,
        endTime: 234567809898,
        location: "94ru -3",
        initCastle: [1, 2500],
        finalCastle: [1, 2400],
        id: "B_02",
        loot: [
          {
            floor: 1,
            name: "火龍頭",
            quality: "垃圾般的",
            type: "水龍頭",
            atk: "8787",
            def: "7414",
            minePower: "400",
            owner: "Kulimi"
          }
        ],
        atk_player: [
          {
            name: "Kulimi",
            role: "鍛造師",
            role2: "將軍",
            faction: "j6",
            kill: 456,
            killed: 0,
            assist: 2345,
            castleDamage: 4567,
            damage: 23414,
            damaged: 12456,
          }
        ],
        def_player: [
          {
            name: "Kulimi456",
            role: "戰鬥員",
            role2: "將軍",
            faction: "j6",
            kill: 456,
            killed: 0,
            assist: 2345,
            damage: 23414,
            damaged: 12456,
          }
        ],
        report_list: [
          {
            atk_f : "艾基爾",
            def_f: "吳",
            atk_name: "Kulimi2",
            atk_id: 20,
            def_name: "Kulimi",
            def_id: 1,
            dead: ["Kulimi2"],
            remarks: "城牆耗損了200點血量",
            time: 1617653222268.1222,
            id: 2
          }
        ],
      }
    }
  },
  methods: {
    format_time(ori_time) {
      return (new Date(ori_time)).toLocaleString()
    },
    format_past_time(ori_time) {
      let text = ''
      if (Math.floor(ori_time / 1000 / 60 / 60) > 0) {
        text = text + Math.floor(ori_time / 1000 / 60 / 60) + '時'
      }
      if (Math.floor(ori_time / 1000 / 60) % 60 > 0) {
        text = text + Math.floor(ori_time / 1000 / 60) % 60 + '分'
      }
      if (Math.floor(ori_time / 1000) % 60 > 0) {
        text = text + Math.floor(ori_time / 1000) % 60 + '秒'
      }
      return text
    },
    compose_report_link(id) {
      return '/'+localStorage.round+"/history/"+id
    }
  }
}
</script>
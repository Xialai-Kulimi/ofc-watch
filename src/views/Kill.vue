<template>
  <div v-if="loading">

    <RanksMenu></RanksMenu>
    <p>不計算不死劍阻止的擊殺。</p>
    <div class="row-div2">
      <table cellpadding="3">
        <tr>
          <th>名次</th><th>陣營（最終）</th><th>暱稱</th><th>擊殺數</th>
        <tr v-for="(item, index) in killBoardList" :key="item">
        <td>{{ index+1 }}</td><td>{{item.faction}}<td>{{ item.name }}</td><td>{{ item.kill }}</td>
        </tr>
      </table>

    </div>

  </div>

</template>

<script>

import RanksMenu from '@/components/RanksMenu.vue'
import api from "../api";
export default {
  name: "Kill",
  components:{
    RanksMenu
  },
  data() {
    return {
      loading: false,
      killBoardList: [
        {name: "Kulimi",faction:"吳", kill: 48763},
        {name: "Kulidfasdfasdfasdfmi2",faction:"吳", kill: 8888},
      ],

    }
  },
  watch: {
    "$store.state.round": async function () {
      this.loading = false
      this.killBoardList = await api.getData("Kill.json")
      this.loading = true
    },
  },
  mounted: async function () {
    this.killBoardList = await api.getData("Kill.json")
    this.loading = true
  }
}
</script>

<style scoped>

</style>

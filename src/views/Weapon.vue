<template>
  <div v-if="loading">
    <div class="row-div chart-p row-div2">
      <VueApexCharts
          class="charts" type="donut"
          :options="options1" :series="series1"
      >
      </VueApexCharts>
      <VueApexCharts
          class="charts" type="donut"
          :options="options2" :series="series2"
      >
      </VueApexCharts>
    </div>

    <div class="row-div">
      <div>
        <p>統計各種裝備種類的名稱出場數。</p>
        <table cellpadding="3">
          <tr>
            <th>名次</th><th>名稱</th><th>陣營</th><th>種類</th><th>出場數</th>
          <tr v-for="(item, index) in itemBoardList" :key="item">
            <td>{{ index+1 }}</td><td>{{item.name}}<td>{{ item.faction }}</td><td>{{item.type}}</td><td>{{ item.times }}</td>
          </tr>
        </table>
      </div>

    </div>
  </div>


</template>

<script>
import VueApexCharts from "vue-apexcharts";
import api from "../api";


export default {
  name: "Weapon",
  components: {
    VueApexCharts
  },
  data() {
    return {
      loading: false,
      series1: [5],
      series2: [5],
      itemBoardList: [
          {"name": "金剛輪宝仁王", "faction": "進擊的巨人", "type": "長槍", "times": 533}
          ],
      options1: {
        chart: {
          width: '100%',
          type: 'pie',
        },
        labels: ["單手劍"],
        theme: {

        },
        plotOptions: {
          pie: {
            dataLabels: {
              offset: -5
            }
          }
        },
        title: {
          text: "裝備出場分布"
        },
        dataLabels: {
          formatter(val, opts) {
            const name = opts.w.globals.labels[opts.seriesIndex]
            return [name, val.toFixed(1) + '%']
          }
        },
        legend: {
          show: false
        }
      },
      options2: {
        chart: {
          width: '100%',
          type: 'pie',
        },
        labels: ["普通裝備出場率", "樓層獎勵出場率"],
        theme: {

        },
        plotOptions: {
          pie: {
            dataLabels: {
              offset: -5
            }
          }
        },
        title: {
          text: "所有戰報中有使用樓層獎勵裝備的占比"
        },
        dataLabels: {
          formatter(val, opts) {
            const name = opts.w.globals.labels[opts.seriesIndex]
            return [name, val.toFixed(1) + '%']
          }
        },
        legend: {
          show: false
        }
      },
    }
  },
  watch: {
    "$store.state.round": async function () {
      this.loading = false
      this.series1 =  await api.getData("Weapon1.json")
      this.options1.labels =  await api.getData("Weapon2.json")
      this.series2 =  await api.getData("Weapon3.json")
      this.itemBoardList =  await api.getData("Weapon4.json")
      this.loading = true
    },
  },
  mounted:async function () {
    this.series1 =  await api.getData("Weapon1.json")
    this.options1.labels =  await api.getData("Weapon2.json")
    this.series2 =  await api.getData("Weapon3.json")
    this.itemBoardList =  await api.getData("Weapon4.json")
    this.loading = true
  }
}
</script>

<style scoped>
.chart-p {
  margin: 40px;
}
</style>

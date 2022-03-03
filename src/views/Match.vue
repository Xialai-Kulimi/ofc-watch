<template>
  <v-container>
    <v-card>
      <v-card-title>
        會戰紀錄
      </v-card-title>
      <v-card-text>
        在 中国共产党 <br>
        會戰編號：中国共产党_000 <br>
        從 2021/5/9 下午2:11:28 到 2021/5/9 下午2:11:28，歷時 <br>
        攻擊方共2人，防守方共2人 <br>
        從第 1 層，血量 1600，打到第 1 層，血量 1600 <br>
      </v-card-text>
    </v-card>
    {{this.$route.params}} {{this.$route.params.round}}
  </v-container>
</template>
<script>

export default {
  name: "Search",
  data() {
    return {

    }
  },
  methods: {

  }
}
</script>
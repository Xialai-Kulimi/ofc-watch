<template>
  <v-app id="inspire">
    <v-app-bar
        app
        flat
    >
      <v-container class="py-0 fill-height">

        <v-btn
            v-for="link in links"
            :key="link"
            @click="goto_page(link.path)"
            text
        >
          {{ link.label }}
        </v-btn>

        <v-spacer></v-spacer>

        <v-responsive max-width="260">
          <v-select
              dense
              flat
              hide-details
              rounded
              solo-inverted
              v-model="round"
              @change="change_round"
              :items="round_options"
          >
          </v-select>
        </v-responsive>
      </v-container>
    </v-app-bar>

    <v-main class="fill-height" app>
      <v-container>


        <router-view></router-view>

      </v-container>



    </v-main>
    <v-footer
        app
        dense
        padless
    >
      <v-card-text
          class="text-center"

      >Copyright © {{ new Date().getFullYear() }}  ofc-watch.kulimi.tw All rights reserved.</v-card-text>
    </v-footer>
    <v-snackbar
        v-model="snackbar"
        timeout="5000"
    >
      {{ text }}

      <template v-slot:action="{ attrs }">
        <v-btn
            color="pink"
            text
            v-bind="attrs"
            @click="snackbar = false"
        >
          關閉
        </v-btn>
      </template>
    </v-snackbar>
  </v-app>
</template>

<script>
import router from "./router";
import api from "./api";

export default {
  data() {
    return {
      search_text: "",
      snackbar: false,
      text: '',
      round: {},
      round_options: [
        {text: '第四輪', value: '4'},
        {text: '第五輪', value: '5'},
        {text: '幕間劇場', value: '5.5'},
        {text: '第六輪', value: '6'},
        {text: '第七輪 端午亂鬥', value: '7'},
        {text: '第八輪 疫苗亂鬥', value: '8'},
        {text: '第九輪 吳剛', value: '9'},
        {text: '第十輪 bang利商店大亂鬥', value: '10'},
        {text: '第十二輪 年夜飯', value: '11'},
        {text: '第十三輪 真正的艾恩葛朗特', value: '12'}
      ],
      links: [
        {label: 'OFC WATCH', path: ""},
        {label: '玩家', path: "player"},
        // {label: '會戰', path: "match"},
        // {label: '搜尋', path: "search"},
        // {label: '武具大賞', path: "weapon"},
        {label: '關於', path: "about"},
      ],
    }
  },
  methods: {
    goto_page(path) {
      if (localStorage.round !== 'undefined'){
        if (path === "about" || path === "weapon") {
          router.replace("/" + path)
        }
        else{
          router.replace("/" + localStorage.round + "/" + path)
        }
      }
      else {
        this.text = '請選擇輪數'
        this.snackbar = true
      }


    },

    change_round() {
      // alert(this.round)
      localStorage.round = this.round
      router.replace('/')
      router.replace("/" + this.round)

    },
  },
  mounted: async function () {

    if (localStorage.round) {
      this.round = localStorage.round
      await router.replace("/" + this.round)
    }
    else {
      localStorage.round = this.round_options[this.round_options.length - 1].value
      this.round = this.round_options[this.round_options.length - 1]
      await router.replace("/" + this.round)
    }

    setInterval(() => {
      if (this.$route.params.round === 'undefined'){
        this.router.replace('/')
      }
    }, 1000)
    this.round_options = await api.getData("round_options")
    // this.change_round()

  }

}
</script>
<style>
html {
  height: 100%;
  font-family: "微軟正黑體", "黑體-繁", "Helvetica", "Arial","LiHei Pro", sans-serif;
}
body {
  height: 100%;
}

</style>
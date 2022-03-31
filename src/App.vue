<template>
  <v-app id="inspire">
    <v-container
        style="display: flex;flex-flow: column"
        row
        fluid
        class="align-center justify-center text-center ma-0"
    >
      <Login v-if="!login"></Login>
    </v-container>
    <v-container v-if="login"
    >
      <v-speed-dial
          v-model="fab"
          fixed
          top
          left

          direction="bottom"
          transition="slide-y-transition"
      >
        <template v-slot:activator>

          <v-btn
              v-model="fab"
              color="black"
              dark
              fab
          >
            <v-icon v-if="fab">
              mdi-close
            </v-icon>
            <v-icon v-else>
              mdi-eye
            </v-icon>
          </v-btn>

        </template>

        <v-btn
            fab
            dark
            small
            color="gray"
            @click="round_dialog=true"
        >
          <v-icon>mdi-eye-settings</v-icon>
        </v-btn>
        <v-btn
            fab
            small
            v-for="b in links"
            :key="b"
            @click="goto_page(b.path)"
            color="gray"
        >
          <v-icon>{{b.icon}}</v-icon>

        </v-btn>

      </v-speed-dial>
      <v-dialog
          v-model="round_dialog"
          width="500"
      >

        <v-card class="pa-5">
          <v-card-title>
            選擇輪數
          </v-card-title>

          <v-divider></v-divider>

          <v-card-actions>
            <v-select
                shaped
                v-model="round"
                @change="change_round"
                :items="round_options"
            >
            </v-select>
          </v-card-actions>
        </v-card>
      </v-dialog>
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
    </v-container>

  </v-app>
</template>

<script>
import router from "./plugins/router";
import api from "./api";
import Login from "@/components/Login";

export default {
  data() {
    return {
      login: false,
      round_dialog: false,
      fab: false,
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
        // {'path': '', 'icon': 'mdi-monitor-eye'},
        // {'path': 'player', 'icon': 'mdi-account-eye'},
        // {'path': 'search', 'icon': 'mdi-magnify'},
        // {'path': 'about', 'icon': 'mdi-file-eye-outline'},
      ],
      // links: [
      //   // {label: 'OFC WATCH', path: ""},
      //   {label: '玩家', icon: 'mdi-account-eye', path: "player"},
      //   // {label: '會戰', path: "match"},
      //   // {label: '搜尋', path: "search"},
      //   // {label: '武具大賞', path: "weapon"},
      //   {label: 'mdi', icon: 'mdi-file-eye-outline', path: "about"},
      // ],
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
      this.round_dialog = false
    },
  },
  mounted: async function () {

    if (window.location.pathname === '/'){
      if (localStorage.round) {
        this.round = localStorage.round
        await router.replace("/" + this.round)
      }
      else {
        localStorage.round = this.round_options[this.round_options.length - 1].value
        this.round = this.round_options[this.round_options.length - 1]
        await router.replace("/" + this.round)
      }
    }
    this.links = await api.getData("links")
    this.round_options = await api.getData("round_options")
    this.login = await api.getData("check_login")

  },
  components: {
    Login
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
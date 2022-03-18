<template>
  <v-app id="inspire">
    <v-speed-dial
        v-model="fab"
        fixed
        top
        left

        direction="bottom"
        open-on-hover
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
                  v-for="link in links"
                  :key="link"
                  small
                  @click="goto_page(link.path)"
                  color="gray"
              >
                <v-icon>{{ link.icon }}</v-icon>

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
<!--    <v-app-bar-->
<!--        app-->
<!--        flat-->
<!--    >-->
<!--      <v-container class="py-0 fill-height">-->

<!--        <v-btn-->
<!--            v-for="link in links"-->
<!--            :key="link"-->
<!--            @click="goto_page(link.path)"-->
<!--            text-->
<!--        >-->
<!--          {{ link.label }}-->
<!--        </v-btn>-->

<!--        <v-spacer></v-spacer>-->

<!--        <v-responsive max-width="260">-->

<!--        </v-responsive>-->
<!--      </v-container>-->
<!--    </v-app-bar>-->

    <v-main class="fill-height" app>
      <v-container>


        <router-view></router-view>

      </v-container>



    </v-main>

<!--    <v-bottom-navigation-->
<!--        app-->
<!--    >-->
<!--      <v-list>-->
<!--        <v-list-item class="px-2">-->
<!--          <v-list-item-avatar>-->
<!--            <v-img src="https://randomuser.me/api/portraits/women/85.jpg"></v-img>-->
<!--          </v-list-item-avatar>-->
<!--        </v-list-item>-->

<!--        <v-list-item link>-->
<!--          <v-list-item-content>-->
<!--            <v-list-item-title class="text-h6">-->
<!--              Sandra Adams-->
<!--            </v-list-item-title>-->
<!--            <v-list-item-subtitle>sandra_a88@gmail.com</v-list-item-subtitle>-->
<!--          </v-list-item-content>-->
<!--        </v-list-item>-->
<!--      </v-list>-->

<!--      <v-divider></v-divider>-->
<!--      <v-btn-->
<!--          v-for="link in links"-->
<!--          :key="link"-->
<!--          @click="goto_page(link.path)"-->
<!--          text-->
<!--      >-->
<!--        {{ link.label }}-->
<!--      </v-btn>-->
<!--      <v-list-->
<!--          nav-->
<!--          dense-->
<!--      >-->
<!--        <v-list-item link-->
<!--                     v-for="link in links"-->
<!--                     :key="link"-->
<!--                     @click="goto_page(link.path)"-->
<!--        >-->
<!--          <v-list-item-title>{{ link.label }}</v-list-item-title>-->
<!--        </v-list-item>-->

<!--      </v-list>-->
<!--    </v-bottom-navigation>-->

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
        // {label: 'OFC WATCH', path: ""},
        {label: '玩家', icon: 'mdi-account-eye', path: "player"},
        // {label: '會戰', path: "match"},
        // {label: '搜尋', path: "search"},
        // {label: '武具大賞', path: "weapon"},
        {label: 'mdi', icon: 'mdi-file-eye-outline', path: "about"},
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

    this.round_options = await api.getData("round_options")
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
<template>
  <v-container
      style="display: flex;flex-flow: column"
      row
      fluid
      class="align-center justify-center text-center"
  >
    <v-card width="800" class="pa-5">
      <v-row class="text-center">
        <v-col cols="12">
          <Big_Eye></Big_Eye>
        </v-col>

        <v-col class="mb-4">
          <h1>Our Floating Castle Watcher</h1>
          <h1>我們的浮游城 觀察者</h1>
          <v-dialog
              v-model="dialog"
              width="500"
              persistent
              overlay-opacity="0.8"
          >
            <template v-slot:activator="{ on, attrs }">

              <v-btn
                  block
                  outlined

                  v-bind="attrs"
                  v-on="on"

              >點此登入</v-btn>
            </template>

            <v-card class="pa-5">
              <v-card-title class="text-h5">
                《隱私權政策》
              </v-card-title>

              <v-card-text>
                非常歡迎您光臨「OFC WATCH」（以下簡稱本網站），為了讓您能夠安心的使用本網站的各項服務與資訊，特此向您說明本網站的隱私權保護政策，以保障您的權益，請您詳閱下列內容： <br>
                <br>
                <strong>一、隱私權保護政策的適用範圍</strong> <br>
                隱私權保護政策內容，包括本網站如何處理在您使用網站服務時收集到的個人識別資料。隱私權保護政策不適用於本網站以外的相關連結網站，也不適用於非本網站所委託或參與管理的人員。 <br>
                <br>
                <strong>二、個人資料的蒐集、處理及利用方式</strong> <br>
                本網站不保證使用者的任何權利。 <br>
              </v-card-text>

              <v-divider></v-divider>


                          <v-alert

                              outlined
                              type="error"
                          >
                            Abandon hope, all ye who enter here.
                          </v-alert>

                <v-btn

                    block
                    @click="dialog = false"
                    href="https://discord.com/api/oauth2/authorize?client_id=894818033254674442&redirect_uri=https%3A%2F%2Fyourdream.kulimi.tw&response_type=code&scope=identify"
                >
                  <v-icon>
                    mdi-discord
                  </v-icon>
                  接受並使用Discord登入
                </v-btn>

            </v-card>
          </v-dialog>

        </v-col>

      </v-row>
    </v-card>

  </v-container>
</template>

<script>
import Big_Eye from "@/components/Big-Eye";
  export default {
    name: 'HelloWorld',

    data: () => ({
      ecosystem: [
        {
          text: 'vuetify-loader',
          href: 'https://github.com/vuetifyjs/vuetify-loader',
        },
        {
          text: 'github',
          href: 'https://github.com/vuetifyjs/vuetify',
        },
        {
          text: 'awesome-vuetify',
          href: 'https://github.com/vuetifyjs/awesome-vuetify',
        },
      ],
      importantLinks: [
        {
          text: 'Documentation',
          href: 'https://vuetifyjs.com',
        },
        {
          text: 'Chat',
          href: 'https://community.vuetifyjs.com',
        },
        {
          text: 'Made with Vuetify',
          href: 'https://madewithvuejs.com/vuetify',
        },
        {
          text: 'Twitter',
          href: 'https://twitter.com/vuetifyjs',
        },
        {
          text: 'Articles',
          href: 'https://medium.com/vuetify',
        },
      ],
      whatsNext: [
        {
          text: 'Explore components',
          href: 'https://vuetifyjs.com/components/api-explorer',
        },
        {
          text: 'Select a layout',
          href: 'https://vuetifyjs.com/getting-started/pre-made-layouts',
        },
        {
          text: 'Frequently Asked Questions',
          href: 'https://vuetifyjs.com/getting-started/frequently-asked-questions',
        },
      ],
    }),
    components: {
      Big_Eye
    },
  }
</script>

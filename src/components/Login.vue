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
          <v-row style="display: flex;flex-flow: row" class="align-center justify-center text-center pa-5">
            <v-spacer></v-spacer>
            <v-dialog
                v-model="dialog"
                width="500"
                overlay-opacity="0.8"
            >
              <template v-slot:activator="{ on, attrs }">

                <v-btn
                    outlined
                    v-bind="attrs"
                    v-on="on"
                >《隱私權政策》&《社群守則》</v-btn>
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
                <v-card-title class="text-h5">
                  《社群守則》
                </v-card-title>

                <v-card-text>
                  我們將「OFC WATCH」（以下簡稱本網站）打造為一個可以輕鬆進行真誠交流、建立關係及閒逛的地方。我們的社群準則確保每個人都能找到歸屬感，同時以犧牲其他人為代價。這些準則規定用戶如何使用從本網站獲得的資訊。本網站的每個使用者都必須遵守這些規則，它們適用於我們平台的所有部分，包括您的內容、行為。在評估是否違反特定社群準則時，我們可能會考量相關的平台外行為。我們的信任暨安全團隊審查使用者和版主提交的報告或可信報告。當有人違反這些準則時，我們可能會對他們採取一些強制措施，包括：發出警告；移除使用者權限；公布使用者私人資料；暫停或移除相關帳戶。如果您發現看起來違反這些準則的使用者、行為，請向我們通報。 <br>
                  <br>
                  <strong>OFC WATCH決策團隊擁有任何情況下的最終裁量權</strong> <br>
                </v-card-text>

                <v-alert

                    outlined
                    type="error"
                >
                  Abandon hope, all ye who enter here.
                </v-alert>
                <v-card-actions><v-checkbox
                    v-model="agree"
                    label="我已詳閱並同意其內容"
                    color="red darken-3"
                    value="true"
                    hide-details
                ></v-checkbox></v-card-actions>


              </v-card>
            </v-dialog>

            <v-spacer></v-spacer>
            <v-btn
                v-bind:disabled="!agree"

                color="red darken-3"
                href="/api/login"
            >
              <v-icon>
                mdi-discord
              </v-icon>
              授權並登入
            </v-btn>
            <v-spacer></v-spacer>
          </v-row>



        </v-col>

      </v-row>
    </v-card>

  </v-container>
</template>

<script>
import Big_Eye from "@/components/Big-Eye";
import api from "@/api.js"

export default {
    name: 'Login',

    data: () => ({
      agree: false,
      dialog: false

    }),
    components: {
      Big_Eye
    },
    mounted: async function() {
      let params = new URLSearchParams(location.search)
      let code = (params.get("code"))
      if (code){
        let token = await api.getData('login/'+code)
        alert(token)
        this.$store.commit('update_token', token)
      }


    }
  }
</script>

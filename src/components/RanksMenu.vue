<template>
  <div class="row-div2">
    <div id="ranks">
      <router-link class="ranks-link" to="kill">擊殺排行</router-link>
      <router-link class="ranks-link" to="killed">被擊殺排行</router-link>
      <router-link class="ranks-link" to="damage">對人傷害排行</router-link>
      <router-link class="ranks-link" to="castleDamage">對牆傷害排行</router-link>
      <router-link class="ranks-link" to="damaged">承受傷害排行</router-link>
      <router-link class="ranks-link" to="xp">戰鬥經驗排行</router-link>
      <router-link class="ranks-link" to="times">出戰次數排行</router-link>
      <router-link class="ranks-link" to="loot">樓層獎勵排行</router-link>
    </div>
    <div class="navbar-toggler" style="border: none" v-bind:class="{'m-menu-btn-a': sidebar}" >
      <i @click="SideBarOn" class="fa fa-bars fa-lg m-dots" style="cursor: pointer"></i>
    </div>
    <div v-if="sidebar" @click="SideBarOn" class="black-layout"></div>
    <transition>
      <div v-if="sidebar" id="sidebar-nav" :class="{'nav-show':sidebar}">
        <router-link class="ranks-link m-ranks-link" to="kill">擊殺排行</router-link>
        <router-link class="ranks-link m-ranks-link" to="killed">被擊殺排行</router-link>
        <router-link class="ranks-link m-ranks-link" to="damage">對人傷害排行</router-link>
        <router-link class="ranks-link m-ranks-link" to="castleDamage">對牆傷害排行</router-link>
        <router-link class="ranks-link m-ranks-link" to="damaged">承受傷害排行</router-link>
        <router-link class="ranks-link m-ranks-link" to="xp">戰鬥經驗排行</router-link>
        <router-link class="ranks-link m-ranks-link" to="times">出戰次數排行</router-link>
        <router-link class="ranks-link m-ranks-link" to="loot">樓層獎勵排行</router-link>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: "RanksMenu",
  data() {
    return {
      sidebar: false
    }
  },
  methods: {
    SideBarOn() {
      this.sidebar = (!this.sidebar);
    }
  }
}
</script>

<style scoped lang="scss">

@keyframes m-move {
  0%{
    right: 0;
  }
  100%{
    right: 45%;
  }
}


.ranks-link {
  font-weight: bold;
  color: #2c3e50;
  margin-right: 20px;
  margin-left: 20px;
}

.ranks-link:hover {
  text-decoration: underline;
}

#ranks {
  text-align: center;
  width: 100%;
  margin-bottom: 50px;
  display: flex;
  justify-content: center;
  @include phone-width{
    display: none;
  }
  @include small-pad-width{
    display: none;
  }

}

.m-ranks-link{
  margin-bottom: 10%;
}

.navbar-toggler {
  height: 50px;
  width: 30px;
  border-radius: 15px 0 0 15px;
  background-color: white;
  box-shadow:3px 3px 5px 6px #cccccc;
  display: none;
  justify-content: left;
  align-content: center;
  position: fixed;
  right: 0px;
  top: 95px;
  z-index: 3;
  @include phone-width{
    display: flex;
  }
  @include small-pad-width{
    display: flex;
  }
}

.m-dots {
  display: flex;
  justify-content: center;
  align-content: center;
  line-height: 50px;
  margin-left: 10px;

}



.m-menu-btn-a {
  animation-duration: 0.4s;
  animation-name: m-move;
  right: 45%;
  box-shadow:none;
}

.sidebar-link {
  font-size: x-large;
  font-weight: bold;
  color: #2c3e50;
  display: flex;
  width: 85%;
  margin: auto;
  align-items: center;
  justify-content: left;
  @include pad-width{
    font-size: 35px;
  }
  @include small-pad-width{
    font-size: 35px;
  }
  @include phone-width{
    font-size: 20px;
  }
}

#sidebar-nav {
  animation-name: m-move !important;
  animation-duration: 0.4s !important;
  position: fixed;
  top: 0;
  background: white;
  z-index: 3;
  width: 45%;
  height: 100%;
  text-align: center;
  padding-top: 5%;
  left: 55%;
}


.nav-show{
  right: 0;
  display: flex;
  flex-wrap: wrap;
  flex-flow: column;

}




</style>
<template>
  <div class="home">
    <div class="box block" @click="navZone('dining')">Dining Room</div>
    <div class="box block" @click="navZone('living')">Living Room</div>
    <div class="box block" @click="navZone('bathrooms')">Bathrooms</div>
    <div class="box block" @click="navZone('master')">Master</div>
    <div class="box block" @click="navZone('outside')">Outside</div>
    <div class="box block empty">&nbsp;</div>
    <div class="bottom">
      <div class="box block" @click="makeRequest('on')">All On</div>
      <div class="box block" @click="makeRequest('off')">All Off</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'home',
  methods: {
    navZone (zone) {
      this.$router.push({ path: `/zone/${zone}` })
    },
    makeRequest (command) {
      this.$http.get(`http://192.168.1.12:5000/api/zone/global/${command}`)
        .then(res => console.log(res))
    }
  }
}
</script>

<style lang="scss" scoped>
.home {
  margin-top: 10px;
}

.block {
  margin: 0 10px 10px 10px !important;
  font-size: 32pt !important;
  text-align: center;
  background-color: rgb(53, 63, 109);
}

@media (max-width: 500px) {
  .block {
    font-size: 24pt !important;
  }
}

.empty {
  background-color: #1f2424 !important;
  color: #1f2424;
}

.bottom {
  width: 100%;
  position: fixed;
  bottom:0%;
}
</style>

<template>
  <div class="zone">
    <div class="box block" @click="makeRequest('on')">On</div>
    <div class="box block" @click="makeRequest('off')">Off</div>
    <div class="box block" @click="makeRequest('up')">Volume Up</div>
    <div class="box block" @click="makeRequest('down')">Volume Down</div>
    <div class="box block empty">&nbsp;</div>
    <div class="bottom">
      <div class="box block" @click="navHome()">Home</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'zone',
  props: ['id'],
  methods: {
    navHome () {
      this.$router.push({ path: '/' })
    },
    makeRequest (command) {
      this.$http.get(`http://192.168.1.12:5000/api/zone/${this.id}/${command}`)
        .then(res => console.log(res))
    }
  }
}
</script>

<style lang="scss" scoped>
.zone {
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

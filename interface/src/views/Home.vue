<template>
  <div class="home">
    <div class="box block">Dining Room</div>
    <div class="box block">Living Room</div>
    <div class="box block">Bathrooms</div>
    <div class="box block">Master</div>
    <div class="box block">Outside</div>
    <div class="box block empty">&nbsp;</div>
    <div class="bottom">
      <div class="box block">All On</div>
      <div class="box block">All Off</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'home'
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

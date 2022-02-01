<template>
  <div>
    <topbar/>
    <FooterComponent/>
  </div>
</template>

<script>
import FooterComponent from "@/components/shared/Footer"
import Topbar from "@/components/shared/TopBar"
export default {
  name: "home",
  components: {
    Topbar,
    FooterComponent
  }
};
</script>

<style scoped lang="scss">

</style>

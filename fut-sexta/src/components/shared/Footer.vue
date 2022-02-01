<template>
  <footer class="footer_shared">
    <div class="footer_shared--menu">
      <icon-shared icon="icon-menu"
      />
      <icon-shared icon="icon-credit"
      />
      <icon-shared icon="icon-user-add"
      />
    </div>
  </footer>
</template>

<script>
import { UserMixin } from "@/modules/User/UserMixin.js"
import IconShared from "@/components/shared/IconShared"
export default {
    name: "topbar-shared",
    mixins: [UserMixin],
    components: {
      IconShared
    }
}
</script>

<style scoped lang="scss">
  .footer_shared {
    
    display: flex;
    align-items: center;  
    justify-content: center;
    background-color: white;
    position: fixed;
    bottom: 0px;
    padding: .5em 0em;
    width: 100vw;
    color: black;
    font-size: 1.2em;

    .footer_shared--menu {
      display: flex;
      width: 70%;
      color: darken(map-get($colors, 'content'), 40);
      justify-content: space-between;
    }
  }
</style>
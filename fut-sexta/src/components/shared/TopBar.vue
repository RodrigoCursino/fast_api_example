<template>
  <nav class="topbar_shared">
    <div class="topbar_shared--user">
      <icon-shared icon="icon-person"/>
      <span>{{user.user}}</span>
    </div>
    <icon-shared icon="icon-menu"
                 class="topbar_shared--menu"
    />
  </nav>
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
  .topbar_shared {
    
    display: flex;
    align-items: center;  
    justify-content: space-between;
    background-color: map-get($colors, 'dark');
    
    padding: .8em 1em;
    color: white;

    box-shadow: rgba(33, 35, 38, .2) 0px 5px 0px 0px;
    
    .topbar_shared--menu {
      cursor: pointer;
      padding: 5px;
      border-radius: 50%;
      background-color: darken(map-get($colors, 'dark'),8);
    }
    .topbar_shared--user {
      display: flex;
      align-items: flex-end;
      
      .icon {
        font-size: 1.3em;
      }
      span {
        margin-left: 5px;
        font-weight: bold;
      }
    }
  }
</style>
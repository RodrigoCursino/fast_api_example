<template>
  <div class="home">
    <principal/>
  </div>
</template>

<script>
// @ is an alias to /src

import Principal from "@/components/home/Home.vue";

export default {
  name: "Home",
  components: {
    Principal,
  },
};
</script>

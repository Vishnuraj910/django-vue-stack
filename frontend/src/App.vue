<template>
  <v-app>
    <v-main>
      <Welcome />
    </v-main>
  </v-app>
</template>

<script>
import Welcome from './components/Welcome.vue'

export default {
  name: 'App',

  components: {
    Welcome,
  },

  data: () => ({
    //
  }),
  mounted() {
    document.title = process.env.VUE_APP_NAME
  }
}
</script>

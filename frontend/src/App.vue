<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <button @click="fetchMessage">Get Message from Django</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      message: 'Welcome to Vue.js!'
    };
  },
  methods: {
    async fetchMessage() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/hello/');
        this.message = response.data.message;
      } catch (error) {
        console.error('Error fetching message:', error);
      }
    }
  }
};
</script>

<style>
#app {
  text-align: center;
  margin-top: 60px;
}
</style>
<template>
  <div id="app">
    <h1>HotmartGPT</h1>
    <input type="text" v-model="textInput" placeholder="Enter text" />
    <button @click="sendText">Send</button>
    <div>{{ response }}</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      textInput: '',
      response: ''
    };
  },
  methods: {
    async sendText() {
      try {
        const res = await axios.post(`${process.env.VUE_APP_FRONTEND_URL}/sendText`, {
          text: this.textInput
        });
        this.response = res.data.response;
      } catch (error) {
        console.error('Error:', error);
      }
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

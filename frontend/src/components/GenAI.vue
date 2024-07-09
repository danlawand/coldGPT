<template>
  <div id="app">
    <h1>Chat with HotmartGPT</h1>
    <input type="text" v-model="textInput" placeholder="Enter text" />
    <button @click="sendText">Send</button>
    <p>{{response}}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'GenAI',
  data () {
    return {
      textInput: '',
      response: ''  
    }
  },
  methods: { 
    async sendText() {
      try {
        const res = await axios.post("http://localhost:5000/genai",
        {
          "text": this.textInput
        });
        this.response = res.data;
      }
      catch (error){
        this.response = error.message;
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #FF0000;
}
</style>

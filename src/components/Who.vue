<template>
    <div>
        <h1>You're new!</h1>
        <h3>Who are you?</h3>
        <button v-for="name in names" v-bind:key="name">{{ name }}</button>
    </div>
</template>

<script>

export default {
  name: 'who',
  props: [],
  data: function() {
    return {
      names: process.env.VUE_APP_NAMES.split(" ")
    }
  },
  methods: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

button {
  outline: none;
  border: none;
  margin: 10px;
  padding: 5px 10px 5px 10px;
  background: rgba(0, 0, 0, 0.1);
  border-radius: 7px;

  font: 'Avenir', Helvetica, Arial, sans-serif;
  font-size: 14px;
  font-style: bold;

  transition: 300ms;
}

button:hover {
  transform: scale(1.5);
}

div { 
  text-align: center;
  margin-top: 30%;
}

</style>

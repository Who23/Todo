<template>
    <div>
        <h1>You're new!</h1>
        <h3>Who are you?</h3>
        <button v-for="name in names" v-bind:key="name" @click="sendIAm(name)">{{ name }}</button>
    </div>
</template>

<script>

import exportBus from '../bus.js'

export default {
  name: 'who',
  props: [],
  data: function() {
    return {
      names: process.env.VUE_APP_NAMES.split(" ")
    }
  },
  methods: {
    sendIAm: function(name) {
      exportBus.$emit('iam', name)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

div { 
  text-align: center;
  margin-top: 30%;
}

</style>

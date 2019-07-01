<template>
<div>
  <div @click="delTodo" id="button"><img :src="icon" @mouseenter="toggleIcon" @mouseleave="toggleIcon"></div>
  <p>{{ todoItem }}</p>
</div>
</template>

<script>
import exportBus from '../bus.js'
const icon = require('../assets/check.png')
const hoverIcon = require('../assets/filled_check.png')

export default {
  name: 'todo',
  props: ['todoItem', 'listPos'],
  data: function() {
    return {
      icon: icon
    }
  },
  methods: {
    delTodo: function() {
      exportBus.$emit('delTodo', this.listPos)
    },
    toggleIcon: function() {
      if (this.icon === icon) {
        this.icon = hoverIcon
      } else {
        this.icon = icon
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
img {
  display: inline-block;
  width: 20px;
  height: 20px;
  margin-right: 10px;
}

p {
  display: inline;
  word-break: break-all;
  vertical-align: top;
  width: 90%;
}

#button {
  display: inline-block;
}

</style>

<template>
<div>
  <button @click="delTodo">x</button>
  <p>{{ todoItem }}</p>
</div>
</template>

<script>
import exportBus from '../bus.js'

export default {
  name: 'todo',
  props: ['todoItem', 'listPos'],
  methods: {
    delTodo: function() {
      exportBus.$emit('delTodo', this.listPos)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
button {
  display: inline;
  margin-right: 10px;
}
p {
  display: inline;
}
</style>

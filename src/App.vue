<template>
  <div id="app">
    <div id="todoBox">
    <todo v-for="[todoIndex, todoItem] in todos.entries()"
          :key="todoIndex"
          :todoItem="todoItem"
          :listPos="todoIndex"
          ></todo>
    <input v-model="newTodo" @keyup.enter="addTodo">
    </div>
  </div>
</template>

<script>
import todo from './components/todo.vue'
import exportBus from './bus.js'

export default {
  name: 'app',
  components: {
    todo
  },
  data: function () {
    return {
      todos: [],
      newTodo: ""
    }
  },
  created: function () {
    exportBus.$on('delTodo', (event) => {
      this.todos.splice(event, 1)
    })
  },
  methods: {
    addTodo: function() {
      this.todos.push(this.newTodo)
      this.newTodo = ""
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  justify-content: center;
  display: flex;
  color: #2c3e50;
}

input {
  margin-top: 20px;
  display: block;
  width: 100%;
}

#todoBox {
  width: 75%;
}
</style>

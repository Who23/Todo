<template>
  <div id="app">
    <who v-if="!inApp"></who>
    <div v-if="inApp">
      <input v-model="newTodo" @keyup.enter="addTodo" placeholder="I need to...">
      <div id="todoBox">
      <todo v-for="[todoIndex, todoItem] in todos.entries()"
            :key="todoIndex"
            :todoItem="todoItem"
            :listPos="todoIndex"
            ></todo>
      </div>
    </div>
  </div>
</template>

<script>
import todo from './components/todo.vue'
import who from './components/Who.vue'
import exportBus from './bus.js'

export default {
  name: 'app',
  components: {
    todo,
    who
  },
  data: function () {
    return {
      todos: [],
      newTodo: "",
      inApp: false
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
  font-size: 15px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  justify-content: center;
  color: #2c3e50;
  width: 50%;
  margin-left: 25%;
  margin-top: 40px;
}

input {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  margin-bottom: 20px;
  padding: 6px;
  padding-left: 10px;
  padding-right: 10px;
  font-size: 15px;
  display: block;
  outline: none;
  width: 90%;
  border-radius: 15px;
  border: none;
  background-color: rgba(0, 0, 0, 0.05);
  color: #2c3e50;
}

#todoBox {
  width: 75%;
  display: block;
}
</style>

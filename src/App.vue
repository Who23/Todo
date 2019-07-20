<template>
  <div id="app">
    <who v-if="!inApp"></who>
    <div v-if="inApp">
      <input v-model="newTodo" @keyup.enter="addTodo" placeholder="I need to...">
      <div id="todoBox">
      <todo v-for="[todoIndex, todoItem] in todos.entries()"
            :key="todoIndex"
            :todoItem="todoItem.todo"
            :addedBy="todoItem.author"
            :listPos="todoIndex"
            ></todo>
      </div>
      <button @click="inApp = false">{{ person }}</button>
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
      inApp: false,
      person: "",
    }
  },
  created: function () {
    exportBus.$on('delTodo', (event) => {
      this.todos.splice(event, 1)
    })

    exportBus.$on('iam', (event) => {
      this.inApp = true
      this.person = event
    })
  },
  methods: {
    addTodo: function() {
      this.todos.push({ "todo" : this.newTodo, "author" : this.person })
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
  width: calc(100% - 20px);
  border-radius: 15px;
  border: none;
  background-color: rgba(0, 0, 0, 0.05);
  color: #2c3e50;
}

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

#todoBox {
  display: block;
}
</style>

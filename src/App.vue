<template>
  <div id="app">
    <who v-if="!inApp"></who>
    <div v-if="inApp">
      <div class="inputDiv">
        <input id="todoInput" v-model="newTodo" @keyup.enter="addTodo" placeholder="I need to...">
        <taglist class="taglist" :taglist="tags"></taglist>
      </div>
      <div id="todoBox">
      <todo v-for="[todoIndex, todoItem] in Object.entries(todos)"
            :key="todoIndex"
            :todoItem="todoItem.todo"
            :addedBy="todoItem.author"
            :tags="todoItem.tags"
            :listPos="todoIndex"
            ></todo>
      </div>
      <button @click="inApp = false">{{ person }}</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import todo from './components/todo.vue'
import who from './components/Who.vue'
import taglist from './components/taglist.vue'
import exportBus from './bus.js'

export default {
  name: 'app',
  components: {
    todo,
    who,
    taglist
  },
  data: function () {
    return {
      todos: [],
      tags: [],
      newTodo: "",
      inApp: false,
      person: "",
    }
  },
  created: function () {
    exportBus.$on('delTodo', (event) => {
      this.todos.splice(event, 1)
      this.delTodoPost(event)
    })

    exportBus.$on('iam', (event) => {
      this.inApp = true
      this.person = event
      localStorage.who = event
    })

    exportBus.$on('tagUpdate', (event) => {
      this.updateTagPost(...event)
    })

    exportBus.$on('todoEdit', (event) => {
      this.todos[event[1]]['todo'] = event[0]
      this.editTodoPost(event[1], this.todos[event[1]])
    })
  },
  mounted: function () {
    if (localStorage.who) {
      this.inApp = true
      this.person = localStorage.who
    }

    axios.get("/todos")
    // arrow functions for keeping `this` reference
    .then(response => {
      console.log(response)
      this.todos = response.data
    })
    .catch(error => {console.log(error)})
  },
  methods: {
    addTodo: function() {
      let todoObj = { "todo" : this.newTodo, "author" : this.person, "tags": this.tags }

      this.addTodoPost(todoObj)
      this.todos.push(todoObj)
      this.newTodo = ""
      this.tags = []
    },
    addTodoPost: function(todoObj) {
      axios.post('/todos/add', { todo: todoObj })
      .then(response => {console.log(response)})
      .catch(error => {console.log(error)});
    },
    delTodoPost: function(todoIndex) {
      axios.post('/todos/remove', { todoIndex: todoIndex})
      .then(response => {console.log(response)})
      .catch(error => {console.log(error)})
    },
    editTodoPost: function(todoIndex, todoObj) {
      axios.post('/todos/edit', { todo: todoObj, todoIndex: todoIndex})
      .then(response => {console.log(response)})
      .catch(error => {console.log(error)})
    },
    updateTagPost: function(todoIndex, tags) {
      axios.post('/todos/tags/update', { tags: tags, todoIndex: todoIndex})
      .then(response => {console.log(response)})
      .catch(error => {console.log(error)})
      
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

.inputDiv {
  margin-bottom: 20px;
}

.taglist {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}

#todoInput {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  padding: 6px;
  margin-bottom: 5px;
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

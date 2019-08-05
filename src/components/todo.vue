<template>
<div>
  <div class="itemDiv">
    <div @click="delTodo" id="button"><img :src="icon" @mouseenter="toggleIcon" @mouseleave="toggleIcon"></div>
    <p>{{ todoItem }}</p>
    <taglist :taglist="tags" style="margin-top: 0px;"></taglist>
  </div>
  <div class="addedByDiv">
    <p class="addedBy"> - {{ addedBy }}</p>
  </div>
</div>
</template>

<script>
import exportBus from '../bus.js'
import taglist from './taglist.vue'


const icon = require('../assets/check.png')
const hoverIcon = require('../assets/filled_check.png')

export default {
  name: 'todo',
  props: ['todoItem', 'listPos', 'addedBy'],
  components: {
    taglist
  },
  data: function() {
    return {
      icon: icon,
      tags: []
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
}

.itemDiv {
  display: inline-block;
  width: 90%;
}

.addedByDiv {
  display: inline-block;
  width: 10%;
  margin-bottom: 8px;
}

.addedBy {
  color: #2c3e5033;
  align-content: right;
  transition: 300ms;
  word-break: none;
  white-space: nowrap;
}

.addedBy:hover {
  color: #2c3e50aa;
}

#button {
  display: inline-block;
}

</style>

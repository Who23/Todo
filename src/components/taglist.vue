<template>
  <div class="taglistContainer">
    <div v-for="[index, tag] in Object.entries(taglist)" 
        :key="index" 
        :class="{ editing: editing == index, tagItem: true}" 
        @dblclick="setEdit(index)">

      <span v-if="editing == index">
        <input v-model="edit" 
               v-autowidth="{minWidth: '20px'}" 
               @keyup.enter="stopEdit"
               @keydown="onKeyDown"
               ref="tagInputField"
               class="tagEdit">
      </span>

      <span v-else class="tagDisplay">
        {{ tag }}
      </span>

      <span @click="rmTag(index)" class="removeTag">x</span>
    </div>
    <div @click="addTag" class="addTag">+</div>
  </div>
</template>

<script>
import exportBus from '../bus';

export default {
  name: 'taglist',
  props: ['taglist'],
  data: function() {
    return {
      edit: "",
      editing: -1
    }
  },
  created: function() {
    exportBus.$on('clickedOff', () => {
      if (this.editing) {
        this.stopEdit()
      }
    })
  },
  methods: {
    rmTag: function(index) {
      if (this.editing) {
        this.editing = -1
      }
      this.taglist.splice(index, 1)
      exportBus.$emit('tagUpdateTodo')
    },
    addTag: function() {
      this.taglist.push("")
    },
    setEdit: function(index) {
      if (this.editing == -1) {
        this.edit = this.taglist[index]
        this.editing = index
      }
    },
    stopEdit: function() {
      this.taglist[this.editing] = this.edit
      this.editing = -1
      exportBus.$emit('tagUpdateTodo')
    },
    onKeyDown(evt){
      if (this.edit.length >= 40) {
        if (evt.keyCode >= 48 && evt.keyCode <= 90) {
          evt.preventDefault()
          return
        }
      }
    }
  },
}

</script>

<style scoped>

.tagItem {
  border-radius: 5px;
  height: 15px;
  white-space: nowrap;
  max-width: 100%;
  display: inline-block;

  font-size: 12px;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  word-wrap: break-word;
  background-color: aquamarine;

  margin: 2px 3px;
  padding: 2px 5px;

  transition: 200ms;
 }

 .editing {
   background-color: deeppink;
 }

 .tagDisplay {
   display: inline-block;
   margin-right: 2px;
   min-width: 20px;
 }

 .tagEdit {
  font-size: 12px;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  white-space: nowrap;
  background-color: rgba(127, 255, 212, 0);
  color: #2c3e50;

  padding: 0px;
  margin: 0px 3px 0px 0px;
  border: none;
  outline: none;
 }

 .addTag {
   font-size: 14px;

   text-align: center;
   display: inline-block;
   border-radius: 5px;
   width: 20px;
   background-color: darkcyan;

   margin: 2px 0px;

   transition: 400ms;
 }

 .addTag:hover {
   background-color: cornflowerblue;
 }

</style>
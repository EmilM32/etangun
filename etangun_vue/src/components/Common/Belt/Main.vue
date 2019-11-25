<template>
  <div
    :class='levelClass'
    :style="{ width: `${width}px`, height: `${height}px`, margin: '0 1rem' }">
    <div v-if='levelT==="kup" && levelN%2!=0'
      :class='beltColor'>
    </div>
    <v-icon v-if='levelT!=="kup"' color='amber accent-2'>{{`mdi-numeric-${levelN}`}}</v-icon>
  </div>
</template>
<script>
export default {
  props: ['width', 'height', 'levelN', 'levelT'],
  data: () => ({

  }),
  computed: {
    levelClass () {
      let _str = ''
      this.levelT==='kup'
        ? _str = (`${this.levelT}-${this.levelN}`)
        : _str = (`${this.levelT}`)
      return _str
    },
    beltColor () {
      return `belt-${this.levelN}`
    }
  }
}
</script>
<style lang="sass">
   @import 'styles/style.sass'
</style>
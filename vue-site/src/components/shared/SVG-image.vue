<template>
    <img class="responsive-img" alt="JS logo" :src="path">
</template>

<script>
export default {
  name: 'SVG-image',
  props: {
    SVGFile: String
  },
  computed: {
    path(){
      return require( `@/assets/svg/${this.SVGFile}`)
    }
  }
}
</script>

<style scoped>

.responsive-img{
  max-width: 100%;
  height: auto;
}

</style>
<template>
  <img class="responsive-img" alt="JS logo" :src="path" @mouseover="onMouseover" @mouseleave="onMouseleave" />
</template>

<script>
export default {
  name: "SVG-Hoverable",
  props: {
    SVGFile: String
  },
  computed: {
    path() {
      return require(`@/assets/svg/${this.SVGFile}.svg`);
    },
    pathHover() {
      return require(`@/assets/svg/${this.SVGFile}-hover.svg`);
    }
  },
  methods: {
    onMouseover(e) {
      e.target.src = this.pathHover;
    },
    onMouseleave(e) {
      e.target.src = this.path;
    }
  }
};
</script>

<style scoped>
.responsive-img {
  max-width: 100%;
  height: auto;
}
</style>
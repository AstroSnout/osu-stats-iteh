<template>
  <button type="button" class="button" id="imageButton" @click="detailedClick">
    <transition name="fade">
      <SVGHover class="fixed-position" SVGFile="icon-detailed-off" v-if="!detailedRowView" />
    </transition>
    <transition name="fade">
      <SVGHover class="fixed-position" SVGFile="icon-detailed-on" v-if="detailedRowView" />
    </transition>
  </button>
</template>

<script>
import SVGHover from "../shared/SVG-hoverable";

export default {
  name: "DetailedButton",
  components: {
    SVGHover
  },
  computed: {
    detailedRowView: {
      get() {
        return this.$store.state.detailedRowView;
      }
    }
  },
  methods: {
    detailedClick() {
      this.$store.dispatch("detailedRowViewToggle");
      console.log("Clicked");
    }
  }
};
</script>

<style scoped>
button {
  position: relative;
  background-color: #00000000;
  height: 30px;
  padding: 0;
  margin: 30px 0;
  vertical-align: top;
  width: 30px;
  outline: none;
  border: none;
}

.fixed-position {
  position: absolute;
  top: 0;
  left: 0;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
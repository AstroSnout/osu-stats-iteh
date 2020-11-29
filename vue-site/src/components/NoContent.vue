<template>
  <div class="no-content">

      <div id="arrow">
      <SVGImage SVGFile="no-content-arrow.svg"/>
      </div>
      <div id="splash">
          <SVGImage SVGFile="no-content-splash.svg"/>
      </div>
      <div id="text">
          Tell us your rank to begin
      </div>
  </div>
</template>

<script>
import SVGImage from "./shared/SVG-image.vue";

export default {
  name: "NoContent",
  components: {
      SVGImage
  }
};
</script>

<style scoped>
.no-content {
  position: absolute;
  margin: auto;
  margin-top: 50px;
  height: 640px;
  width: 1252px;
  border-radius: 0 0 20px 20px;
  padding-bottom: 15px;
  overflow: hidden;
}

.no-content #arrow {
    position: relative;
    left: 675px;
    width: 102px;
}

.no-content #splash {
    position: relative;
    left: 433px;
    width: 433px;
}

.no-content #text {
    position: relative;
	color: #D9D9D9;
	font-size: 37px;
	line-height: 45px;
	text-align: center;
    margin-top: 50px;
    bottom: 0px;
}
</style>
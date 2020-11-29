<template>
  <div
    class="table-content-row"
    :class="{ 'mouseover': mouseover}"
    :style="{'height': `${componentHeight}px`}"
    @mouseover="mouseover=true"
    @mouseleave="mouseover=false"
  >
    <div
      class="jumbo-image"
      v-if="expanded"
      :style="{'background-image': `url(${mapData.thumb_url})`, 'background-size': `cover`}"
    >
      <div class="gradient">
        <ul class="jumbo">
          <li id="map-occ">
            <span>{{ mapData.count }} ({{ mapData.occurrence }}%)</span>
          </li>
          <li id="map-name">
            <span>{{ mapData.beatmap_name }}</span>
          </li>
          <li id="dl-link">
            <a :href="mapData.dl_link" target="_blank">
              <SVGImage SVGFile="dl-button-white-nohover.svg" />
            </a>
          </li>
        </ul>
      </div>
    </div>
    <ul class="detailed" v-if="!expanded">
      <li id="map-occ">
        <span>{{ mapData.count }} ({{ mapData.ccurrence }}%)</span>
      </li>
      <li id="map-diff-icon">
        <SVGImage SVGFile="icon-speed-white.svg" v-if="mapData.diff_aim_pct <= 50" />
        <SVGImage SVGFile="icon-aim-white.svg" v-if="mapData.diff_aim_pct > 50" />
      </li>
      <li id="map-thumb">
        <img :src="mapData.thumb_url" alt @error="defaultPicture" />
      </li>
      <li id="map-name">
        <span>{{ mapData.beatmap_name }}</span>
      </li>
      <li id="expand-button">
        <button type="button" class="button" id="imageButton" @click="onExpandClick">
          <SVGImage SVGFile="icon-expand-white.svg" />
        </button>
      </li>
      <li id="map-pp-avg">
        <span>{{ mapData.pp_avg }}pp</span>
      </li>
    </ul>
    <ul class="expand" v-if="expanded">
      <li id="map-diff-speed">
        <div>
          <ul class="inner-list">
            <li class="icon">
              <SVGImage SVGFile="icon-speed-white.svg" />
            </li>
            <li>
              <span>{{ 100 - mapData.diff_aim_pct }}%</span>
              <br />
              <span id="small">Speed</span>
            </li>
          </ul>
        </div>
      </li>
      <li id="map-diff-aim">
        <div>
          <ul class="inner-list">
            <li class="icon">
              <SVGImage SVGFile="icon-aim-white.svg" />
            </li>
            <li>
              <span>{{ mapData.diff_aim_pct }}%</span>
              <br />
              <span id="small">Aim</span>
            </li>
          </ul>
        </div>
      </li>
      <li id="map-length">
        <div>
          <ul class="inner-list">
            <li class="icon">
              <SVGImage SVGFile="icon-aim-white.svg" />
            </li>
            <li>
              <span>{{ mapData.play_time}} ({{ mapData.total_time }}) min</span>
              <br />
              <span id="small">Map duration</span>
            </li>
          </ul>
        </div>
      </li>
      <li id="map-mods">
        <span id="big">{{ modString }}</span>
        <br />
        <span id="small">Mods</span>
      </li>
      <li id="collapse-button">
        <button type="button" class="button" id="imageButton" @click="onExpandClick">
          <SVGImage SVGFile="icon-collapse-white.svg" />
        </button>
      </li>
    </ul>
  </div>
</template>

<script>
import SVGImage from "./shared/SVG-image.vue";
import defImage from "../assets/background-main.png";
export default {
  name: "ContentRowDetailed",
  components: {
    SVGImage
  },
  props: {
    mapData: Object
  },
  data() {
    return {
      mouseover: false,
      expanded: false
    };
  },
  computed: {
    componentHeight() {
      var tmp;
      if (this.expanded) {
        tmp = 367;
      } else {
        tmp = 90;
      }
      return tmp;
    },
    modString() {
      console.log(this.mapData.enabled_mods)
      if (this.mapData.enabled_mods != "") {
        return this.mapData.enabled_mods.match(/.{1,2}/g).join(", ")
      } else {
        return "NoMod"
      }
    }
  },
  methods: {
    defaultPicture: function(event) {
      console.log(event);
      event.target.src = defImage;
    },
    onExpandClick() {
      this.expanded = !this.expanded;
    }
  }
};
</script>

<style scoped>
.table-content-row {
  height: 90px;
  border: thin solid #00000000;
  border-bottom: thin solid rgba(96, 96, 96, 0.4);
  font-size: 14px;
  line-height: 17px;
}

.mouseover {
  height: 89px;
  transition: 0.2s;
  box-shadow: 0 6px 8px 0 #161b28;
  border: 1px solid rgba(255, 255, 255, 0.4);
}

ul {
  width: 100%;
  height: 90px;
  list-style-type: none;
  display: table;
  margin: 0;
  padding: 0;
}

ul li {
  padding: 0 14px;
  display: table-cell;
  color: #fff;
  word-wrap: break-word;
  vertical-align: middle;
  /* line-height: 90px; */
}

li img {
  height: 50px;
  /* padding: 20px 36px; */
}

.detailed #map-occ {
  width: 12%;
}

.detailed #map-diff-icon {
  width: 30px;
  padding: 0 0;
}

.detailed #map-thumb {
  width: 10%;
  padding: 0 0;
}

.detailed #map-thumb img {
  height: 40px;
  width: 93px;
  object-fit: cover;
  border-radius: 10px;
  box-shadow: 0 2px 6px 0 rgba(0, 0, 0, 0.3);
}

.detailed #map-name {
  text-align: left;
  width: 47%;
}

.detailed #expand-button {
  line-height: 90px;
  width: 15%;
  float: right;
}

.detailed #map-pp-avg {
  line-height: 90px;
  text-align: left;
  float: right;
  width: 25%;
  color: #a1ff67;
}

div.jumbo-image {
  position: relative;
  height: 277px;
  width: 100%;
}

.gradient {
  height: 277px;
  width: 100%;
  background: linear-gradient(180deg, rgba(0, 0, 0, 0.2) 0%, #000000 110%);
}

ul.jumbo {
  position: absolute;
  bottom: 0;
}

ul.jumbo li {
  height: 90px;
  width: 100%;
  vertical-align: bottom;
  margin: 25px 32px;
  padding-bottom: 20px;
  font-weight: 600;
  font-size: 18px;
  color: #ffffff;
}

.jumbo #map-occ {
  width: 14%;
}

.jumbo #map-name {
  text-align: left;
  width: 80%;
}

.expand {
  text-align: left;
  background-color: #1d1f24;
  height: 90px;
  width: 100%;
}
.expand li {
  padding: 0 32px;
}

.expand #map-diff-speed,
.expand #map-diff-aim {
  width: 12%;
}

#map-length .inner-list {
  padding: 0 110px;
}

#map-mods {
  width: 25%;
}

.inner-list {
  width: inherit;
}

.inner-list li {
  font-weight: 600;
  font-size: 18px;
  padding: 0;
}

#big {
  font-weight: 600;
  font-size: 18px;
}

.inner-list .icon {
  width: 30px;
  padding: 0 10px;
}

.inner-list li span#small {
  font-weight: 100;
  font-size: 14px;
  padding: 10px 0;
}

#collapse-button {
  padding: 0 26px;
  line-height: 90px;
  width: 30px;
  float: right;
}

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
</style>
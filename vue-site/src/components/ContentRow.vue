<template>
  <div
    class="table-content-row"
    :class="{ 'mouseover': mouseover}"
    @mouseover="mouseover=true"
    @mouseleave="mouseover=false"
  >
    <ul class="override ">
      <li id="map-occ">
        <span>{{ mapData.occurrence }}% ({{ mapData.count }})</span>
      </li>
      <li id="map-thumb">
        <img :src="mapData.thumb_url" alt @error="defaultPicture" />
      </li>
      <li id="map-name">
        <span>{{ mapData.beatmap_name }}</span>
      </li>
      <li id="map-length">
        <span>{{ mapData.play_time}} ({{ mapData.total_time }})</span>
      </li>
      <li id="map-pp-avg">
        <span>{{ mapData.pp_avg }}pp</span>
      </li>
      <li id="map-acc-avg">
        <span>{{ mapData.acc_avg }}%</span>
      </li>
      <li id="map-diff-icon">
        <SVGImage SVGFile="icon-aim-white.svg" />
      </li>
      <li id="map-diff">
        <div id="diff-aim">
          <div id="diff-speed" v-bind:style="{ width: (mapData.diff_aim_pct) + '%'}"></div>
        </div>
      </li>
      <li id="map-diff-icon">
        <SVGImage SVGFile="icon-speed-white.svg" />
      </li>
      <li id="dl-link">
        <a :href="mapData.dl_link" target="_blank">
          <SVGImage SVGFile="dl-button-white-nohover.svg" />
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
import SVGImage from "./shared/SVG-image.vue";
import defImage from "../assets/background-main.png";
export default {
  name: "ContentRow",
  components: {
    SVGImage
  },
  props: {
    mapData: Object
  },
  data() {
    return {
      mouseover: false
    };
  },
  methods: {
    defaultPicture: function(event) {
      console.log(event);
      event.target.src = defImage;
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
  transition: 0.2s;
  box-shadow: 0 6px 8px 0 #161B28;
  border: 1px solid rgba(255,255,255,0.4);
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

#map-occ {
  width: 11%;
}

#map-thumb {
  width: 10%;
}

#map-thumb img {
  height: 40px;
  width: 93px;
  object-fit: cover;
  border-radius: 10px;
  box-shadow: 0 2px 6px 0 rgba(0, 0, 0, 0.3);
}

#map-name {
  width: 25%;
  text-align: left;
}

#map-length {
  width: 10%;
}

#map-pp-avg {
  width: 10%;
  color: #A1FF67;
}

#map-acc-avg {
  width: 10%;
}

#map-diff-icon {
  width: 30px;
}

#map-diff {
  width: 10%;
  padding: 0;
}

#map-diff #diff-aim {
  background-color: #5ae4ff;
  width: 100%;
  height: 3px;
  border-radius: 3px;
}

#map-diff #diff-speed {
  background-color: #ff3434;
  height: 3px;
  border-radius: 3px;
}

#dl-link {
  width: 5%;
}
</style>
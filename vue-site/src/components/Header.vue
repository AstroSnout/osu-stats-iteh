<template>
  <div class="table-header">
    <ul>
      <li id="osu-logo">
        <div>
          <a href="https://osu.ppy.sh/" target="_blank">
            <SVGHover SVGFile="osu-logo-white" />
          </a>
        </div>
      </li>
      <li>
        <HeaderButton ButtonName="HD" v-on:modClick="onModClick" />
      </li>
      <li>
        <HeaderButton ButtonName="HR" v-on:modClick="onModClick" />
      </li>
      <li>
        <HeaderButton ButtonName="DT" v-on:modClick="onModClick" />
      </li>
      <li>
        <StrictButton ButtonName="Strict" v-on:strictClick="onStrictClick" />
      </li>
      <li id="input-fields">
        <span>
          Enter your rank:
          <input
            id="user-rank"
            type="number"
            name="user-rank"
            :class="{ animate: viewNoContent }"
            placeholder="e.g. 9000"
            v-model.number.lazy="urank"
          />
        </span>
      </li>
      <li id="burger">
        <DetailedButton fileName="icon-detailed-off" />
      </li>
      <li id="faq">
        <button
          :class="{'faq-mo': faqMouseover}"
          @mouseover="faqMouseover=true"
          @mouseleave="faqMouseover=false"
          @click="onFaqClick"
        >FAQ</button>
      </li>
    </ul>
  </div>
</template>

<script>
import SVGHover from "./shared/SVG-hoverable.vue";
import HeaderButton from "./header/HeaderButton.vue";
import StrictButton from "./header/StrictButton.vue";
import DetailedButton from "./header/DetailedButton.vue";
// import { mapState } from "vuex";

export default {
  name: "Header",
  components: {
    // SVGImage,
    HeaderButton,
    StrictButton,
    SVGHover,
    DetailedButton
  },
  data() {
    return {
      faqMouseover: false
    };
  },
  mounted() {
    this.$store.dispatch("loadMapData");
  },
  computed: {
    urank: {
      get() {
        return this.$store.state.urank;
      },
      set(value) {
        this.$store.commit("SET_URANK", value);
      }
    },
    urange: {
      get() {
        return this.$store.state.urange;
      },
      set(value) {
        this.$store.commit("SET_URANGE", value);
      }
    },
    viewNoContent: {
      get() {
        return this.$store.state.viewStates.noContent;
      }
    }
  },
  methods: {
    onModClick(value) {
      this.$store.dispatch("contentIsLoading", true);
      this.$store.dispatch("modToggleClick", value);
      this.$store.dispatch("loadMapData", value);
    },
    onStrictClick(value){
      this.$store.dispatch("contentIsLoading", true);
      this.$store.dispatch("strictToggleClick", value);
      this.$store.dispatch("loadMapData", value);
    },
    onFaqClick() {
      this.$store.dispatch("faqSectionToggle");
    }
  },
  watch: {
    urank: function() {
      if (this.urank != "") {
        this.$store.dispatch("contentIsShowing", false);
      } else {
        this.$store.dispatch("contentIsShowing", true);
      }
      this.$store.dispatch("loadMapData");
    },
    urange: function() {
      this.$store.dispatch("loadMapData");
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 90px;
}

li {
  float: left;
  height: 90px;
  line-height: 90px;
}

li#osu-logo img {
  height: 50px;
  margin: 20px 36px;
}

.table-header {
  height: 90px;
  width: 100%;
  background-color: #2c353c;
  border-radius: 20px 20px 0 0;
}

.button#mod-other {
  background: #ffffff00;
  border: 1px solid #d9d9d9;
  box-sizing: border-box;
  color: #ffffff;
  font-weight: 100;
}

#other {
  width: 9%;
  text-align: center;
}

#button-other {
  padding: 10px;
}

#input-fields {
  /* background-color: #00ccff; */
  left: 55px;
  color: #ffffff;
  width: auto;
  font-weight: 600;
}

#input-fields {
  padding-left: 135px; /* Centers it a bit more properly */
}

#input-fields #user-rank {
  margin: 0 15px;
  color: #ffffff;
  width: 188px;
  height: 38px;
  background-color: #ffffff00;
  border: 1px solid #d9d9d9;
  border-radius: 12px;
  text-align: center;
  font-size: 16px;
  outline: none;
}

#input-fields #user-range {
  color: #ffffff;
  width: 100px;
  height: 38px;
  background-color: #ffffff00;
  border: 1px solid #d9d9d9;
  border-radius: 12px;
  text-align: center;
  font-size: 16px;
  outline: none;
}
#input-fields span {
  padding: 0 18px;
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0px;
}

#burger {
  float: right;
  width: 5%;
  padding: 0 16px;
}

#burger img {
  padding: 30px 0;
}

#dark-mode {
  float: right;
  width: 5%;
  padding-right: 4px;
  padding-left: 16px;
}

#dark-mode img {
  padding: 30px 0;
}

#faq {
  padding: 0 16px;
  float: right;
  color: #d9d9d9;
  font-size: 16px;
  width: 5%;
}

#faq button {
  transition: 0.1s;
  background: #ffffff00;
  border: 0 solid #d9d9d9;
  box-sizing: border-box;
  color: #d9d9d9;
  font-size: 16px;
  font-weight: 100;
  cursor: pointer;
  outline: none;
}

button.faq-mo {
  transition: 0.1s;
  color: #ffffff !important;
  font-weight: 600 !important;
}

a:link,
a:visited,
a:hover,
a:active {
  color: inherit;
  text-decoration: none;
}

a {
  width: 0;
}

.animate {
  animation: shadow-pulse 1.5s infinite;
}

@keyframes shadow-pulse {
  0% {
    box-shadow: inset 0 0 14px 0px rgba(136, 69, 180, 0.1),
      inset 0 0 14px 0px rgba(136, 69, 180, 0.1),
      0 0 14px 0px rgba(136, 69, 180, 0.1);
  }
  50% {
    box-shadow: inset 0 0 14px 0px rgba(136, 69, 180, 0.7),
      inset 0 0 14px 0px rgba(136, 69, 180, 0.5),
      0 0 14px 0px rgba(136, 69, 180, 0.5);
  }
  100% {
    box-shadow: inset 0 0 14px 0px rgba(136, 69, 180, 0.1),
      inset 0 0 14px 0px rgba(136, 69, 180, 0.1),
      0 0 14px 0px rgba(136, 69, 180, 0.1);
  }
}
</style>

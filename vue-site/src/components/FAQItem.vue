<template>
  <div
    class="faq-content-row"
    :class="{ 'mouseover': mouseover, 'click': clickedAnimation}"
    @mouseover="mouseover=true"
    @mouseleave="mouseover=false"
    @click="onClick"
  >
    <div>
      <ul>
        <li id="title">
          <div>{{ content.id }}. {{ content.question }}</div>
        </li>
        <li id="arrow">
          <SVGImage SVGFile="icon-dropdown-white.svg" />
        </li>
      </ul>
    </div>
    <div v-if="clicked" id="answer">
      <p>{{content.answer}}</p>
    </div>
  </div>
</template>

<script>
import SVGImage from "./shared/SVG-image.vue";
import defImage from "../assets/background-main.png";
export default {
  name: "FAQItem",
  components: {
    SVGImage
  },
  props: {
    content: Object
  },
  data() {
    return {
      mouseover: false,
      clicked: false,
      clickedAnimation: false
    };
  },
  methods: {
    defaultPicture: function(event) {
      console.log(event);
      event.target.src = defImage;
    },
    onClick() {
      this.clickedAnimation = !this.clickedAnimation;
      if (this.clicked) {
        this.clicked = !this.clicked;
      } else {
        setTimeout(() => {
          this.clicked = !this.clicked;
        }, 250);
      }
    }
  }
};
</script>

<style scoped>
.faq-content-row {
  height: 90px;
  border: thin solid #00000000;
  border-bottom: thin solid rgba(96, 96, 96, 0.4);
  font-size: 14px;
  line-height: 17px;
}

.mouseover {
  transition: 0.3s;
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
  text-align: center;
  padding: 0 14px;
  display: table-cell;
  color: #fff;
  word-wrap: break-word;
  vertical-align: middle;
  /* line-height: 90px; */
}

li img {
  height: 50px;
}

#title {
  font-size: 16px;
  font-weight: 400;
  /* line-height: 20px; */
  padding: 0 36px;
  text-align: left;
  width: 91%;
  float: inline-start;
}

.click {
  height: 230px;
}

#answer {
  text-align: left;
  font-size: 16px;
  font-weight: 400;
  /* line-height: 20px; */
  padding: 0 36px;
  text-align: justify;
  justify-content: center;
  width: auto;
  float: inline-start;
  color: #d9d9d9;
  word-wrap: break-word;
}
</style>
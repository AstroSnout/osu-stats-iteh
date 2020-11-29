<template>
  <div class="table-content">
    <transition name="fade">
      <NoContent v-if="viewNoContent" :key="2" />
    </transition>
    <transition name="fade">
      <Loading v-show="viewLoading" :key="3" />
    </transition>
    <div
      class="scrollable-content"
      :class="{ shadow: !scrollTopMost }"
      v-if="!viewNoContent"
      @scroll.passive="scrolled"
    >
      <transition name="fade">
        <FAQSection v-if="viewFaq" :key="1" />
      </transition>

      <div v-for="mapData in allMapData" :key="mapData.beatmap_id">
        <ContentRowDetailed :mapData="mapData" v-if="detailedRowView" />
        <ContentRow :mapData="mapData" v-if="!detailedRowView" />
      </div>
    </div>
  </div>
</template>

<script>
import ContentRow from "./ContentRow.vue";
import ContentRowDetailed from "./ContentRowDetailed.vue";
import Loading from "./Loading.vue";
import NoContent from "./NoContent.vue";
import FAQSection from "./FAQSection.vue";

export default {
  name: "Content",
  components: {
    ContentRow,
    ContentRowDetailed,
    Loading,
    NoContent,
    FAQSection
  },
  data() {
    return {
      scrollTopMost: true
    };
  },
  computed: {
    allMapData: {
      get() {
        return this.$store.state.allMapData.slice(0, 100);
      }
    },
    viewLoading: {
      get() {
        return this.$store.state.viewStates.loading;
      }
    },
    viewNoContent: {
      get() {
        return this.$store.state.viewStates.noContent;
      }
    },
    viewFaq: {
      get() {
        return this.$store.state.viewStates.faq;
      }
    },
    detailedRowView: {
      get() {
        return this.$store.state.detailedRowView;
      }
    }
  },
  methods: {
    scrolled(e) {
      if (e.target.scrollTop > 10) {
        this.scrollTopMost = false;
      } else {
        this.scrollTopMost = true;
      }
    }
  },
  watch: {
    allMapData() {
      console.log("Var allMapData changed");
    },
    detailedRowView() {
      console.log("Should scroll to top");
    }
  },
  mounted() {
    window.addEventListener("scroll", this.updateScroll);
  },
  destroy() {
    window.removeEventListener("scroll", this.updateScroll);
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

.table-content {
  height: 690px;
  margin: 0 auto;
  /* background-color: #299bf3; */
  border-radius: 0 0 20px 20px;
}

.scrollable-content {
  padding-left: 4px;
  scroll-behavior: smooth;
  height: 685px;
  overflow: auto;
  overflow-x: hidden;
  background-color: #272f35;
  scroll-behavior: smooth;
}

.scrollable-content::-webkit-scrollbar {
  width: 4px;
  margin: 0;
}
.scrollable-content::-webkit-scrollbar-track {
  background: #cccccc00;
  margin: 0;
}
.scrollable-content::-webkit-scrollbar-thumb {
  background: #5ae4ff;
  border-radius: 2px;
  margin: 0;
}

.content-row-enter-active,
.content-row-leave-active {
  transition: opacity 0.1s ease;
}
.content-row-enter,
.content-row-leave-to {
  opacity: 0;
}

.content-row-move {
  transition: transform 0.1s ease;
}

.shadow {
  -moz-box-shadow: inset 0 108px 64px -114px;
  -webkit-box-shadow: inset 0 108px 64px -114px;
  box-shadow: inset 0 108px 64px -114px;
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

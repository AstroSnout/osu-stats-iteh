<template>
  <button
    type="button"
    class="button"
    :id="buttonID"
    :class="{ 'active': isActive, 'not-active': isNotActive, 'mouseover': mouseover}"
    @mouseover="mouseover=true"
    @mouseleave="mouseover=false"
    @click="isActive = !isActive, isNotActive = !isNotActive"
    v-on:click="$emit('modClick', buttonID)"
  >{{ ButtonName }}</button>
</template>

<script>
export default {
  name: "HeaderButton",
  props: {
    ButtonName: String
  },
  data() {
    return {
      isActive: false,
      isNotActive: true,
      mouseover: false,
      buttonID: this.ButtonName
    };
  },
  methods: {}
};
</script>

<style scoped>
.button {
  transition: 0.3s;
  padding: 10px 19px;
  border-radius: 20px;
  color: #000000;
  font-family: "Roboto", sans-serif;
  font-size: 16px;
  font-weight: 600;
  line-height: 20px;
  text-align: center;
  vertical-align: middle;
  text-decoration: none;
  display: inline;
  margin: 0 5px;
  cursor: pointer;
  outline: none;
}

.not-active {
  background: #ffffff00;
  border: 1px solid #d9d9d9;
  box-sizing: border-box;
  color: #ffffff;
  font-weight: 100;
}

.active {
  box-shadow: 0 2px 6px 0 rgba(71, 0, 110, 0.4);
  box-sizing: border-box;
  border: 1px solid #d9d9d900;
  border-collapse: collapse;
  color: #ffffff;
}

.button.active#HD {
  background: linear-gradient(135deg, #dea1ff 0%, #ad4aff 100%);
}

.button.active#HR {
  background: linear-gradient(135deg, #00ccff 0%, #009dff 100%);
}

.button.active#DT {
  background: linear-gradient(135deg, #ff7bfd 0%, #ff45fa 100%);
}

.button.active#Strict {
  background: linear-gradient(135deg, #b2b200 0%, #b2b200 100%);
}

.mouseover {
  background-color: rgba(17,18,19,0.4);
}
</style>
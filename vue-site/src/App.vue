<template>
  <div class="container">
    <Header />
    <Content />
  </div>
</template>
<script>
import Header from "./components/Header.vue";
import Content from "./components/Content.vue";

export default {
  name: "App",
  components: {
    Header,
    Content
  }
};
</script>

<style>
body {
  font-family: "Avenir", "Arial Narrow", Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: #111213;
  margin: 0;
  padding: 0;
  background-image: url("./assets/background-main.png");
  background-repeat: no-repeat;
  background-position: 0 150px;
  text-align: center;
}

.container {
  margin: 0 auto;
  margin-top: 60px;
  height: 780px;
  width: 1252px;
  background-color: #272f35;
  border-radius: 20px;
  padding: 0;
  padding-bottom: 15px;
}
</style>

<template>
  <div class="loader">
    <img src="../assets/loading-alt.png" alt="loading" />
  </div>
</template>

<script>
export default {
  name: "Loading",
};
</script>

<style scoped>
.loader {
  position: absolute;
  margin: auto;
  height: 690px;
  width: 1252px;
  background-color: #0000009d;
  border-radius: 0 0 20px 20px;
  padding-bottom: 15px;
  overflow: hidden;
}

.loader img {
  margin-top: 18%;
}
</style>
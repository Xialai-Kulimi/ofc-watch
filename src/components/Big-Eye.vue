<template>
  <img alt="Vue logo" src="../assets/big-eye.png" class="eye">
</template>

<script>
export default {
name: "Big-Eye"
}
</script>

<style scoped>
@keyframes eye-open {
  0% {
    transform: matrix(1, 0, 0, 0, 0, 0);
  }
  50% {
    transform: matrix(1, 0, 0, 0.0001, 0, 0);
  }
  60% {
    transform: matrix(1, 0, 0, 0.3, 0, 0);
  }
  70% {
    transform: matrix(1, 0, 0, 0.3, 0, 0);
  }
  80% {
    transform: matrix(1.01, 0, 0, 0.01, 0, 0);
  }

  100% {
    transform: matrix(1, 0, 0, 1, 0, 0);
  }
}

.eye {
  max-width: 100%;

  animation-name: eye-open;
  animation-duration: 2.5s;

}
</style>
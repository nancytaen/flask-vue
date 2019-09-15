<template>
  <div>
    <button type="button" class="btn btn-primary" @click="getMessage()">ABC</button>
    {{msg}}
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping.vue',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/api/random';
      axios.get(path)
        .then((res) => {
          this.msg = res.data.data;
          /* eslint-disable no-console */
          console.log(res);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>

</style>

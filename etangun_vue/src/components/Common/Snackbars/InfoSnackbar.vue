<template>
  <v-snackbar v-model="show"
    color="blue"
    :multi-line="mode === 'multi-line'"
    :timeout="timeout"
    :vertical="mode === 'vertical'">
    {{ message }}
    <v-btn icon fab
      @click="show = false">
      <v-icon>mdi-close</v-icon>
    </v-btn>
  </v-snackbar>
</template>

<script>
export default {
  data() {
    return {
      message: "",
      show: false,
      mode: "",
      timeout: 6000,
      text: "Test"
    };
  },
  created: function() {
    this.$store.watch(
      state => state.snackbar.snackInfo,
      () => {
        const msg = this.$store.state.snackbar.snackInfo;
        if (msg !== "") {
          this.show = true;
          this.message = this.$store.state.snackbar.snackInfo;
          this.$store.commit("snackbar/setSnackInfo", "");
        }
      }
    );
  }
};
</script>
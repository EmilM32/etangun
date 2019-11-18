<template>
  <v-snackbar v-model="show"
    color="green"
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
      message: "Test",
      show: false,
      mode: "",
      timeout: 3000,
      text: "Test"
    };
  },
  created: function() {
    this.$store.watch(state => state.snackbar.snackSuccess,() => {
        const msg = this.$store.state.snackbar.snackSuccess
        if (msg !== "") {
          this.show = true
          this.message = this.$store.state.snackbar.snackSuccess
          this.$store.commit("snackbar/setSnackSuccess", "")
        }
      }
    );
  }
};
</script>
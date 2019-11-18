<template>
  <v-snackbar v-model="show"
    color="red"
    :multi-line="mode === 'multi-line'"
    :right="x === 'right'"
    :bottom="y === 'bottom'"
    :left="x === 'left'"
    :timeout="timeout"
    :vertical="mode === 'vertical'">
    {{ message }}
    <v-btn text
      @click="show = false">
      <!-- {{ $t('snackbars.common.closeButton') }} -->
    </v-btn>
  </v-snackbar>
</template>

<script>
export default {
  data() {
    return {
      show: false,
      message: "Test",
      y: "top",
      x: null,
      mode: "",
      timeout: 6000,
      text: "Test"
    };
  },
  created: function() {
    this.$store.watch(state => state.snackbar.snackError, () => {
        const msg = this.$store.state.snackbar.snackError
        if (msg !== "") {
          this.show = true
          this.message = this.$store.state.snackbar.snackError
          this.$store.commit("snackbar/setSnackError", "")
        }
      }
    );
  }
};
</script>
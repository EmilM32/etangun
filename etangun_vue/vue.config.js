module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],

  devServer: {
    proxy: {
      "/api": {
        target: "http://127.0.0.1:8000",
        changeOrigin: true,
        pathRewrite: {
          "^/api": ""
        }
      }
    }
  },

  pluginOptions: {
    i18n: {
      locale: 'pl',
      fallbackLocale: 'pl',
      localeDir: 'locales',
      enableInSFC: true
    }
  }
}

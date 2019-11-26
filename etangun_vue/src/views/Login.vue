<template>
  <v-app id="inspire">
    <v-content>
      <v-container
        class="fill-height"
        fluid>
        <v-row
          align="center"
          justify="center">
          <v-col
            cols="12"
            sm="8"
            md="4">
            <v-card class="elevation-12">
              <v-toolbar
                color="primary"
                dark
                flat>
                <v-toolbar-title>{{ $t('login.loginForm') }}</v-toolbar-title>
                <v-spacer />
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                    v-model='username'
                    :label=" $t('login.login')"
                    prepend-icon="mdi-account"/>
                  <v-text-field
                    :label=" $t('login.pass')"
                    v-model='password'
                    prepend-icon="mdi-lock"
                    type="password"/>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn
                  icon
                  x-large
                  @click='login'
                  color="success">
                  <v-icon>mdi-check</v-icon>
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>
<script>
import axios from "axios"
export default {
  props: {
    source: String,
  },
  data: () => ({
    username: null,
    password: null
  }),
  methods: {
    login () {
      axios
        .post('/api/tangun/login_user/', { username: this.username, password:  this.password })
        .then(response => {
          this.$store.commit("auth/setLoggedState", { logged: response.data.data, userLogin: this.username})
          this.$router.push('Home')
        })
        .catch(error => console.error(error))
    }
  }
}
</script>

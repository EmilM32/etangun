<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
    >
      <v-list dense>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-home</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{ $t('menu.home') }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-contact-mail</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Contact</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      color="light-blue darken-2"
      dark
      clipped-left
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Tangun</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-menu offset-x>
      <template v-slot:activator="{ on }">
        <v-btn icon v-on="on">
          <v-icon>mdi-earth</v-icon>
        </v-btn> 
      </template>
      <v-list>
        <v-list-item>
          <img src="../public/pl.svg" alt="pl" style='width:20px'
            @click='$i18n.locale = "pl"'>
        </v-list-item>
        <v-list-item>
          <img src="../public/en.svg" alt="en" style='width:20px'
            @click='$i18n.locale = "en"'>
        </v-list-item>
      </v-list>
    </v-menu>
      <!-- <div v-if='showLangMenu' class='mr-3'>
        <img src="../public/pl.svg" alt="pl" style='width:20px'
          @click='$i18n.locale = "pl"'>
        
        <img src="../public/en.svg" alt="en" style='width:20px'
          @click='$i18n.locale = "en"'>
      </div>
      <v-btn icon
        @click='showLangMenu = !showLangMenu'>
        <v-icon>mdi-earth</v-icon>
      </v-btn> -->
    </v-app-bar>

    <v-content>
      <v-container
        class="fill-height"
        fluid
      >
      </v-container>
    </v-content>
    <v-footer
      color="light-blue darken-2"
      app
    >
      <span class="white--text">&copy; 2019 UKS Tangun</span>
    </v-footer>
  </v-app>
</template>

<script>
import axios from "axios"
export default {
  props: { source: String, },
  data: () => ({
    drawer: null
  }),
  mounted () {
    axios.get('/api/tangun/test_function/').then(response =>{
      console.log(response)
    })
  }
}
</script>
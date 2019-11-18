<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped>
      <v-list dense
        v-for='(item, i) in getSideBarItems'
        :key='i'>
        <v-list-item link :to='item.link'>
          <v-list-item-action>
            <v-icon>
              {{ item.icon }}
            </v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>
              {{ item.text }}
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      app
      color="light-blue darken-2"
      dark
      clipped-left>
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
    </v-app-bar>
    <v-content>
      <v-container fluid>
        <router-view/>
      </v-container>
    </v-content>
    <v-footer
      color="light-blue darken-2"
      app>
      <span class="white--text">&copy; 2019 UKS Tangun</span>
    </v-footer>
    <t-success-snackbar></t-success-snackbar>
    <t-info-snackbar></t-info-snackbar>
    <t-error-snackbar></t-error-snackbar>
  </v-app>
</template>
<script>
export default {
  data: () => ({
    drawer: null
  }),
  computed: {
    getSideBarItems () {
      return [
        {
          icon: 'mdi-home',
          text: this.$t('menu.home'),
          link: '/'
        },
        {
          icon: 'mdi-view-list',
          text: this.$t('menu.list'),
          link: '/MemberList'
        }
      ]
    }
  }
}
</script>


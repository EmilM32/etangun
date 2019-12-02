<template>
  <div>
    <v-card>
      <v-card-title>
        <v-spacer></v-spacer>
          <v-toolbar-title>{{ $t('menu.places') }}</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-text-field
          v-model="searchAddress"
          append-icon="mdi-magnify"
          :label="$t('common.search')"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-card-text>
        <v-data-table
        :headers="addressHeaders"
        :items="addressItems"
        :search="searchAddress"
        :no-data-text="$t('table.noData')"
        :no-results-text="$t('table.noResult')"
        hide-default-footer
        @page-count="pageCount = $event"
        :page.sync="page"
        :items-per-page="itemsPerPage">
        <template v-slot:item.actions="{ item }">
          <v-btn
            small
            icon
            color='teal darken-3'
            @click='editAddress(item)'>
            <v-icon>mdi-pencil</v-icon>
          </v-btn>
          <v-btn
            small
            icon
            color='red darken-3'
            @click='deleteAddress(item)'>
            <v-icon>mdi-delete</v-icon>
          </v-btn>
        </template>
      </v-data-table>
      <div class="text-center pt-2">
        <v-pagination v-model="page" :length="pageCount"></v-pagination>
        <v-row>
          <v-spacer></v-spacer>
          <v-col cols='2'>
            <v-text-field
              :value="itemsPerPage"
              :label="$t('table.itemsPerPage')"
              type="number"
              min="-1"
              max="15"
              @input="itemsPerPage = parseInt($event, 10)"
            ></v-text-field>
          </v-col>
        </v-row>
      </div>
      </v-card-text>
    </v-card>
    <v-fab-transition>
      <v-tooltip left>
        <template v-slot:activator="{ on }">
          <v-btn
            v-on="on"
            large
            fixed
            bottom
            right
            fab
            color='success'
            @click='addNewAddress'>
            <v-icon>mdi-plus</v-icon>
          </v-btn>
        </template>
        <span>{{ $t('common.add') }}</span>
      </v-tooltip>
    </v-fab-transition>
    <AddressHandler
      v-model='addressDialog'
      v-if='addressDialog'
      @reloadData='getItems'
      :case='addressCase'
      :editedData='editedData'/>
  </div>
</template>
<script>
import axios from "axios"
import AddressHandler from "@/views/dialogs/AddressHandler.vue"
export default {
  components: { AddressHandler },
  data: () => ({
    page: 1,
    pageCount: 0,
    itemsPerPage: 10,
    searchAddress: '',
    addressItems: [],
    fabButton: false,
    transition: 'slide-y-reverse-transition',
    addressDialog: false,
    addressCase: '',
    editedData: {}
  }),
  methods: {
    getItems () {
      axios
        .get('/api/tangun/get_all_addresses/')
        .then(response => { this.addressItems = response.data.data })
        .catch(error => console.error(error))
    },
    addNewAddress () {
      this.addressCase = 'add'
      this.addressDialog = true
    },
    editAddress (item) {
      this.addressCase = 'edit'
      this.editedData = item
      this.addressDialog = true
    },
    deleteAddress (item) {
      this.addressCase = 'del'
      this.editedData = item
      this.addressDialog = true
    }
  },
  computed: {
    addressHeaders () {
      return [
        { text: this.$t('addresses.city'), value: 'city', align: 'center' },
        { text: this.$t('addresses.streetAddress'), value: 'streetAddress', align: 'center' },
        { text: this.$t('addresses.postCode'), value: 'postCode', align: 'center' },
        { text: this.$t('addresses.descr'), value: 'descr', align: 'center' },
        { text: this.$t('addresses.country'), value: 'country', align: 'center' },
        { text: this.$t('common.actions'), value: 'actions', align: 'center' }
      ]
    }
  },
  mounted () {
    this.getItems()
  }
}
</script>
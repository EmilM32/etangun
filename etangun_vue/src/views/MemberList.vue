<template>
  <div>
    <v-card>
      <v-card-title>
        <v-tooltip right>
          <template v-slot:activator="{ on }">
            <v-btn
              v-on="on"
              icon
              x-large
              color='success'
              @click='addNewMember'>
              <v-icon>mdi-plus-circle</v-icon>
            </v-btn>
          </template>
          <span>{{ $t('common.add') }}</span>
        </v-tooltip>
        <v-spacer></v-spacer>
        <v-text-field
          v-model="searchModel"
          append-icon="mdi-magnify"
          :label="$t('common.search')"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-card-text>
        <t-data-table
          :headers="tableHeaders"
          :items="memberlist"
          :search="searchModel"
        ></t-data-table>
      </v-card-text>
    </v-card>
    <MemberHandler 
      v-if='memberHandler.dialog'
      v-model='memberHandler.dialog'
      :addCase='memberHandler.addCase'
      :beltLevels='beltLevels'
      @reloadData='getAllMembers'>
    </MemberHandler>
  </div>
</template>
<script>
import axios from "axios"
import MemberHandler from "@/views/dialogs/MemberHandler.vue"
export default {
  components: { MemberHandler },
  data: () => ({
    memberHandler: {
      dialog: false,
      addCase: true,
      beltLevels: []
    },
    searchModel: '',
    memberlist: [],
  }),
  methods: {
    getAllMembers () {
      axios
        .get('/api/tangun/get_all_members/')
        .then(response => { if (response.status === 200) this.memberlist = response.data.data })
        .catch(error => console.error(error))
    },
    addNewMember () {
      if (this.beltLevels.length > 0) {
        this.memberHandler.addCase = true
        this.memberHandler.dialog = true
      }
    },
    getLevelDict () {
      axios
        .get('/api/tangun/get_belt_level/')
        .then(response => { if (response.status === 200) this.beltLevels = response.data.data })
        .catch(error => console.error(error))
    }
  },
  computed: {
    tableHeaders () {
      return [
        { text: this.$t('memberList.firstName'), value: 'firstName', align: 'center' },
        { text: this.$t('memberList.lastName'), value: 'lastName', align: 'center' },
        { text: this.$t('memberList.birthDate'), value: 'birthDate', align: 'center' },
        { text: this.$t('memberList.level'), value: 'level', align: 'center' },
        { text: this.$t('memberList.group'), value: 'group', align: 'center' }
      ]
    }
  },
  mounted () {
    this.getAllMembers()
    this.getLevelDict()
  }
}
</script>
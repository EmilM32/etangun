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
      :addCase='memberHandler.addCase'>
    </MemberHandler>
  </div>
</template>
<script>
import MemberHandler from "@/views/dialogs/MemberHandler.vue"
export default {
  components: { MemberHandler },
  data: () => ({
    memberHandler: {
      dialog: false,
      addCase: true,
    },
    searchModel: '',
    memberlist: [
      {
        firstName: "firstName1",
        lastName: "lastName",
        birthDate: "birthDate",
        level: "level"
      },
      {
        firstName: "firstName2",
        lastName: "lastName",
        birthDate: "birthDate",
        level: "level"
      },
      {
        firstName: "firstName3",
        lastName: "lastName",
        birthDate: "birthDate",
        level: "level"
      },
      {
        firstName: "firstName4",
        lastName: "lastName",
        birthDate: "birthDate",
        level: "level"
      },
      {
        firstName: "firstName5",
        lastName: "lastName",
        birthDate: "birthDate",
        level: "level"
      },
      {
        firstName: "firstName6",
        lastName: "lastName",
        birthDate: "birthDate",
        level: "level"
      }
    ],
  }),
  methods: {
    addNewMember () {
      this.memberHandler.addCase = true
      this.memberHandler.dialog = true
    }
  },
  computed: {
    tableHeaders () {
      return [
        { text: this.$t('memberList.firstName'), value: 'firstName', align: 'center' },
        { text: this.$t('memberList.lastName'), value: 'lastName', align: 'center' },
        { text: this.$t('memberList.birthDate'), value: 'birthDate', align: 'center' },
        { text: this.$t('memberList.level'), value: 'level', align: 'center' }
      ]
    }
  }
}
</script>
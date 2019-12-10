<template>
  <v-dialog
    v-model='value'
    persistent
    width='800'>
    <v-card>
      <v-card-title>
        <span v-if='addCase'>{{ $t('memberList.add') }}</span>
        <span v-else>{{ $t('memberList.edit') }}</span>
      </v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols='6'>
            <v-text-field
              v-model='memberData.firstName'
              :label="$t('memberList.firstName')">
            </v-text-field>
          </v-col>
          <v-col cols='6'>
            <v-text-field
              v-model='memberData.lastName'
              :label="$t('memberList.lastName')">
            </v-text-field>
          </v-col>
          <v-col cols='4'>
            <v-menu
              v-model="dateMenu"
              :close-on-content-click="false"
              transition="scale-transition"
              offset-y
              min-width="290px">
              <template v-slot:activator="{ on }">
                <v-text-field
                  v-model="memberData.birthDate"
                  :label="$t('memberList.birthDate')"
                  prepend-icon="mdi-calendar"
                  readonly
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="memberData.birthDate"
                @input="dateMenu = false"
                locale='pl'>
              </v-date-picker>
            </v-menu>
          </v-col>
          <v-col cols='3'>
            <v-autocomplete
              :items='groupItems'
              v-model='memberData.group'
              :label="$t('memberList.group')">
            </v-autocomplete>
          </v-col>
          <v-col cols='3'>
            <v-autocomplete
              v-model='memberData.level'
              :items='beltLevels'
              item-text='belt_level'
              item-value='id'
              :label="$t('memberList.level')">
            </v-autocomplete>
          </v-col>
          <v-col cols='2'>
            <v-autocomplete
              v-model='memberData.gender'
              :items='gender'
              :label="$t('memberList.gender')">
            </v-autocomplete>
          </v-col>
          <v-col cols='12' class='pt-5'>
            <v-textarea
              height='0'
              v-model='memberData.comment'
              :label="$t('memberList.comment')"
            ></v-textarea>
          </v-col>
        </v-row>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          icon
          x-large
          color='grey'
          @click='closeDialog'>
          <v-icon>mdi-close</v-icon>
        </v-btn>
        <v-btn
          icon
          x-large
          color='success'
          @click='saveData'>
          <v-icon>mdi-content-save</v-icon>
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
import axios from 'axios'
export default {
  props: ['value', 'addCase', 'beltLevels'],
  data: () => ({
    memberData: {
      firstName: '',
      lastName: '',
      birthDate: new Date().toISOString().substr(0, 10),
      group: '',
      level: '',
      comment: ''
    },
    groupItems: [1, 2],
    dateMenu: false,
    gender: ['M', 'K']
  }),
  methods: {
    saveData () {
      axios
        .post('/api/tangun/save_new_member/', this.memberData)
        .then(response => {
          this.$emit('reloadData', true)
          this.$store.commit('snackbar/setSnackSuccess', this.$t('snackbar.success.save'))
          this.closeDialog()
        })
        .catch(error => {
          console.error(error)
          this.$store.commit('snackbar/setSnackError', this.$t('snackbar.error.save'))
        })
    },
    closeDialog () {
      this.$emit('input', false)
    }
  }
}
</script>

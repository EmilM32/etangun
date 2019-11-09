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
          <v-col cols='6'>
            <v-text-field
              v-model='memberData.birthDate'
              :label="$t('memberList.birthDate')">
            </v-text-field>
          </v-col>
          <v-col cols='6'>
            <v-text-field
              v-model='memberData.level'
              :label="$t('memberList.level')">
            </v-text-field>
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
          @click='$emit("input", false)'>
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
export default {
  props: ['value', 'addCase'],
  data: () => ({
    memberData: {
      firstName: '',
      lastName: '',
      birthDate: '',
      level: '',
      comment: ''
    }
  }),
  methods: {
    saveData () {
      console.log(this.memberData)
    }
  }
}
</script>
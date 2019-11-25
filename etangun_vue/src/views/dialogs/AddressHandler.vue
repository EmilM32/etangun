<template>
  <v-dialog
    v-model='value'
    persistent
    width='800'>
    <v-card>
      <v-card-title>
        <span v-if='addFlg'>{{ $t('addresses.add') }}</span>
        <span v-else-if='editFlg'>{{ $t('addresses.edit') }}</span>
        <span v-else-if='delFlg'>{{ $t('addresses.delete') }}</span>
      </v-card-title>
      <v-card-text>
        <v-form ref='addressForm' lazy-validation v-model="valid">
          <v-row>
            <v-col cols='2'>
              <v-text-field
                v-model='address.city'
                required
                :rules='notNull'
                :label="$t('addresses.city')">
              </v-text-field>
            </v-col>
            <v-col cols='2'>
              <v-text-field
                required
                v-model='address.postCode'
                v-mask="mask"
                :rules='notNull'
                :label="$t('addresses.postCode')">
              </v-text-field>
            </v-col>
            <v-col cols='8'>
              <v-text-field
                required
                :rules='notNull'
                v-model='address.streetAddress'
                :label="$t('addresses.streetAddress')">
              </v-text-field>
            </v-col>
            <v-col cols='12'>
              <v-text-field
                v-model='address.descr'
                :label="$t('addresses.descr')">
              </v-text-field>
            </v-col>
          </v-row>
        </v-form>
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
  props: ['value', 'case', 'editedData'],
  data: () => ({
    addFlg: false,
    editFlg: false,
    delFlg: false,
    address: {
      city: null,
      postCode: null,
      streetAddress: null,
      descr: null
    },
    mask: '##-###',
    valid: true,
    notNull: [v => !!v || ''],
  }),
  methods: {
    closeDialog () {
      this.$emit("input", false)
    },
    saveData () {
      if (this.$refs.addressForm.validate()) {
        if (this.case === 'add') {
          axios
            .post('/api/tangun/add_new_address/', this.address)
            .then(response => { console.log(response) })
            .catch(error => console.error(error))
        } else if (this.case === 'edit') {
          axios
            .post('/api/tangun/edit_address/', this.address)
            .then(response => { console.log(response) })
            .catch(error => console.error(error))
        }
      }
    }
  },
  mounted () {
    if (this.case === 'add') {
      this.addFlg = true
    } else if (this.case === 'edit') {
      this.editFlg = true
      this.address = this.editedData
    } else if (this.case === 'del') {
      this.delFlg = true
    }
  }
}
</script>
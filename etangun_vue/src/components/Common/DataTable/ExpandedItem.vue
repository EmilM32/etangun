<template>
  <v-data-table
    dense
    hide-default-footer
    :headers="paidMonths"
    :items="monthsCheckBox">
    <template v-slot:item.ix="props">
      <v-edit-dialog
        :return-value.sync="props.item.ix">
        {{ props.item.ix }}
        <template v-slot:input>
          <v-text-field
            v-model="props.item.ix"
            label="Edit"
            single-line
            counter
          ></v-text-field>
        </template>
      </v-edit-dialog>
    </template>
  </v-data-table>
</template>
<script>
export default {
  props: ['item'],
  data: () => ({
    paidMonths: [
      {text: 'IX', value: 'ix'},
      {text: 'X', value: 'x'},
      {text: 'XI', value: 'xi'},
      {text: 'XII', value: 'xii'},
      {text: 'I', value: 'i'},
      {text: 'II', value: 'ii'},
      {text: 'III', value: 'iii'},
      {text: 'IV', value: 'iv'},
      {text: 'V', value: 'v'},
      {text: 'VI', value: 'vi'}
    ],
    monthsCheckBox: [{i:0,ii:0,iii:0,iv:0,v:0,vi:0,ix:0,x:0,xi:0,xii:0}]
  }),
  mounted () {
    console.log('item', this.item)
  }

}
</script>
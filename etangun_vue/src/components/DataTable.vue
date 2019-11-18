<template>
<div>
  <v-data-table
    :headers="headers"
    :items="items"
    :search="search"
    :no-data-text="$t('table.noData')"
    :no-results-text="$t('table.noResult')"
    hide-default-footer
    @page-count="pageCount = $event"
    :page.sync="page"
    :items-per-page="itemsPerPage"
    :show-expand='expandShow'
    :single-expand="singleExpand"
    :expanded.sync="expanded"
    class="elevation-1">
    <template v-slot:expanded-item="{ headers }">
      <td :style='{"background-color": "white"}' :colspan="headers.length">
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
      </td>
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
</div>
</template>
<script>
export default {
  props: ['headers', 'items', 'search', 'showExpand'],
  data: () => ({
    page: 1,
    pageCount: 0,
    itemsPerPage: 10,

    //expand feature
    expandShow: false,
    expanded: [],
    singleExpand: false,
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
  created () {
    this.showExpand
      ? this.expandShow = true
      : this.expandShow = false
    
  }
}
</script>
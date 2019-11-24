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
    show-expand
    :single-expand="singleExpand"
    :expanded.sync="expanded"
    class="elevation-1">
    <template v-slot:expanded-item="{ headers, item }">
      <td :style='{"background-color": "white"}' :colspan="headers.length">
        <ExpandedItem :item='item'></ExpandedItem>
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
import ExpandedItem from "@/components/Common/DataTable/ExpandedItem.vue"
export default {
  props: ['headers', 'items', 'search'],
  components: {ExpandedItem},
  data: () => ({
    page: 1,
    pageCount: 0,
    itemsPerPage: 10,

    //expand feature
    expandShow: false,
    expanded: [],
    singleExpand: false,
  })
}
</script>
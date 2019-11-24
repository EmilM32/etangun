<template>
  <v-card class='my-4'>
    <v-card-title>
      <v-icon v-if='item.gender === "M"' color='indigo darken-1'>mdi-face</v-icon>
      <v-icon v-else color='cyan lighten-1'>mdi-face-woman</v-icon>
      <span class='pl-3'>
        {{ item.firstName }} {{ item.lastName }} {{ memberAge }}
      </span>
      <t-belt
        :width='100'
        :height='15'
        :levelN='levelNum'
        :levelT='levelType'
      />
    </v-card-title>
    <v-card-text>
      <v-row>
        <v-col cols='3'>
            <v-card outlined color='blue-grey lighten-5'>
              <v-row class='overline pa-3'>
                <v-col cols='6'>
                  {{ $t('memberList.firstName') }}
                </v-col>
                <v-col cols='6'>
                  {{ item.firstName }}
                </v-col>
                <v-col cols='6'>
                  {{ $t('memberList.lastName') }}
                </v-col>
                <v-col cols='6'>
                  {{ item.lastName }}
                </v-col>
                <v-col cols='6'>
                  {{ $t('memberList.birthDate') }}
                </v-col>
                <v-col cols='6'>
                  {{ item.birthDate }} <kbd>{{ memberAge }} {{ $t('memberList.yearsOld') }}</kbd>
                </v-col>
                <v-col cols='6'>
                  {{ $t('memberList.group') }}
                </v-col>
                <v-col cols='6'>
                  {{ item.group }}
                </v-col>
                <v-col cols='6'>
                  {{ $t('memberList.level') }}
                </v-col>
                <v-col cols='6'>
                  {{ item.level }}
                </v-col>
              </v-row>
            </v-card>
        </v-col>
        <v-col cols='4'>
          <v-card outlined>
            <v-card-subtitle class='overline font-weight-bold' style='font-family: Verdana'>osiągnięcia</v-card-subtitle>
            <v-card-text class='text-right'>
              <div class='d-block'>
                <img src="@/assets/medals/gold.png" alt="gold" class='medal-style'>
                <img src="@/assets/medals/gold.png" alt="gold" class='medal-style'>
                <img src="@/assets/medals/gold.png" alt="gold" class='medal-style'>
              </div>
              <div class='d-block'>
                <img src="@/assets/medals/silver.png" alt="silver" class='medal-style'>
              </div>
              <div class='d-block'>
                <img src="@/assets/medals/brown.png" alt="brown" class='medal-style'>
              </div>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
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
    </v-card-text>
  </v-card>
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
  methods: {
    getAge(dateString) {
        let today = new Date()
        let birthDate = new Date(dateString)
        let age = today.getFullYear() - birthDate.getFullYear()
        let m = today.getMonth() - birthDate.getMonth()
        if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) age--
        return age
    }
  },
  computed: {
    memberAge () {
      return this.getAge(this.item.birthDate)
    },
    levelNum () {
      return this.item['level'].split(" ")[0]
    },
    levelType () {
      return this.item['level'].split(" ")[1]
    }
  },
  mounted () {}

}
</script>
<style lang="sass">
.medal-style
  width: 40px
</style>
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
        <v-col lg="3" md="5" sm="12">
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
                <v-col cols='6'>
                  {{ $t('memberList.id') }}
                </v-col>
                <v-col cols='6'>
                  {{ item.login }}
                </v-col>
              </v-row>
            </v-card>
        </v-col>
        <v-col lg="4" md="7" sm="12">
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
        <v-col lg="5" md="6" sm="12">
          <v-card outlined>
            <v-card-subtitle class='overline font-weight-bold' style='font-family: Verdana'>aktywności</v-card-subtitle>
          </v-card>
        </v-col>
      </v-row>
      <v-row align='center' class='text-right'>
        <v-col cols='1'>
          {{ $t('memberList.year') }}
        </v-col>
        <v-col cols='2'>
          <v-autocomplete
            v-model='yearModel'
            :items='yearsList'
          >
          </v-autocomplete>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols='11'>
          <v-data-table
            dense
            hide-default-footer
            :headers="paidMonths"
            :items="monthsPayments">
            <template v-slot:item.ix="props">
              <v-edit-dialog
                :return-value.sync="props.item.ix">
                {{ props.item.ix }}
                <template v-slot:input>
                  <v-text-field
                    v-model="props.item.ix"
                    single-line
                    counter
                  ></v-text-field>
                </template>
              </v-edit-dialog>
            </template>
            <template v-slot:item.x="props">
              <v-edit-dialog
                :return-value.sync="props.item.x">
                {{ props.item.x }}
                <template v-slot:input>
                  <v-text-field
                    v-model="props.item.x"
                    single-line
                    counter
                  ></v-text-field>
                </template>
              </v-edit-dialog>
            </template>
            <template v-slot:item.xi="props">
              <v-edit-dialog
                :return-value.sync="props.item.xi">
                {{ props.item.xi }}
                <template v-slot:input>
                  <v-text-field
                    v-model="props.item.xi"
                    single-line
                    counter
                  ></v-text-field>
                </template>
              </v-edit-dialog>
            </template>
            <template v-slot:item.xii="props">
              <v-edit-dialog
                :return-value.sync="props.item.xii">
                {{ props.item.xii }}
                <template v-slot:input>
                  <v-text-field
                    v-model="props.item.xii"
                    single-line
                    counter
                  ></v-text-field>
                </template>
              </v-edit-dialog>
            </template>
            <template v-slot:item.i="props">
              <v-edit-dialog
                :return-value.sync="props.item.i">
                {{ props.item.i }}
                <template v-slot:input>
                  <v-text-field
                    v-model="props.item.i"
                    single-line
                    counter
                  ></v-text-field>
                </template>
              </v-edit-dialog>
            </template>
            <template v-slot:item.ii="props">
              <v-edit-dialog
                :return-value.sync="props.item.ii">
                {{ props.item.ii }}
                <template v-slot:input>
                  <v-text-field
                    v-model="props.item.ii"
                    single-line
                    counter
                  ></v-text-field>
                </template>
              </v-edit-dialog>
            </template>
            <template v-slot:item.iii="props">
              <v-edit-dialog
                :return-value.sync="props.item.iii">
                {{ props.item.iii }}
                <template v-slot:input>
                  <v-text-field
                    v-model="props.item.iii"
                    single-line
                    counter
                  ></v-text-field>
                </template>
              </v-edit-dialog>
            </template>
            <template v-slot:item.iv="props">
              <v-edit-dialog
                :return-value.sync="props.item.iv">
                {{ props.item.iv }}
                <template v-slot:input>
                  <v-text-field
                    v-model="props.item.iv"
                    single-line
                    counter
                  ></v-text-field>
                </template>
              </v-edit-dialog>
            </template>
            <template v-slot:item.v="props">
              <v-edit-dialog
                :return-value.sync="props.item.v">
                {{ props.item.v }}
                <template v-slot:input>
                  <v-text-field
                    v-model="props.item.v"
                    single-line
                    counter
                  ></v-text-field>
                </template>
              </v-edit-dialog>
            </template>
            <template v-slot:item.vi="props">
              <v-edit-dialog
                :return-value.sync="props.item.vi">
                {{ props.item.vi }}
                <template v-slot:input>
                  <v-text-field
                    v-model="props.item.vi"
                    single-line
                    counter
                  ></v-text-field>
                </template>
              </v-edit-dialog>
            </template>
          </v-data-table>
        </v-col>
        <v-col cols='1'>
          <v-btn
            icon
            fab
            large
            color='success'
            @click='savePaymentData'>
            <v-icon>mdi-content-save</v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>
<script>
import axios from "axios"
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
    monthsPayments: [{i:0,ii:0,iii:0,iv:0,v:0,vi:0,ix:0,x:0,xi:0,xii:0}],
    yearsList: ['2019/2020'],
    yearModel: '2019/2020'
  }),
  methods: {
    getAge(dateString) {
        let today = new Date()
        let birthDate = new Date(dateString)
        let age = today.getFullYear() - birthDate.getFullYear()
        let m = today.getMonth() - birthDate.getMonth()
        if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) age--
        return age
    },
    savePaymentData () {
      const dataToSend = {
        years: this.yearModel,
        payments: this.monthsPayments
      }
      axios
        .post('/api/tangun/save_member_payments/', dataToSend)
        .then(response => this.$store.commit('snackbar/setSnackSuccess', this.$t('snackbar.success.save')))
        .catch(error => console.error(error))
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
<style lang="sass" scoped>
.medal-style
  width: 40px
</style>
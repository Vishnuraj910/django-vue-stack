<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img :src="require('../assets/kema-logo.png')" class="my-3" contain height="200" />
      </v-col>

      <v-col cols="12">
        <h3>
          Welcome to</h3>
        <h1 class="display-2 font-weight-bold mb-3">
          Kema Merchant Payment System
        </h1>
      </v-col>
      <v-row align="center" justify="center">
        <v-col cols="8" sm="8" md="6" lg="4">
          <v-card>
            <v-card-title class="headline font-weight-bold">
              Scan to Pay
            </v-card-title>

            <v-card-item justify="center">
              <qrcode-vue :value="paymentLink" :size="200" level="H"></qrcode-vue>
            </v-card-item>
            <v-card-subtitle class="merchant-name">
              {{ merchantDetails.merchantName }}<br>
            </v-card-subtitle>
          </v-card>
        </v-col>
      </v-row>
    </v-row>
  </v-container>
</template>

<script>
import QrcodeVue from 'qrcode.vue';
export default {
  name: 'App',
  data() {
    const merchantDetails = {
      merchantName: 'Kema Merchant 1',
      merchantUUID: 'HASHED_MERCHAT_ID_0001',
      amount: 100,
      currency: 'AED'
    }
    return {
      merchantDetails,
      paymentLink: `https://kema-payment.com/api/process?merchantUUID=${merchantDetails.merchantUUID}&amount=${merchantDetails.amount}&currency=${merchantDetails.currency}`
    };
  },
  methods: {
  },
  components: {
    QrcodeVue
  }
};

</script>

<style>
.merchant-name {
  font-size: 20px;
  font-weight: bold;
  color: rgb(78, 77, 76);
  text-align: center;
  font-family: 'Courier New', Courier, monospace;
}
</style>
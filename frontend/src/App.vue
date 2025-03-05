<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <!-- <button @click="fetchMessage">Get Message from Django</button> -->
  </div>
  <qrcode-vue :value="paymentLink" :size="200" level="H"></qrcode-vue>
</template>

<script>
import axios from 'axios';
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
      message: `Payment Kiosk for ${merchantDetails.merchantName}`,
      paymentLink: `https://kema-payment.com/merchantUUID=${merchantDetails.merchantUUID}&amount=${merchantDetails.amount}&currency=${merchantDetails.currency}`
    };
  },
  methods: {
    // async fetchMessage() {
    //   try {
    //     const response = await axios.get('http://127.0.0.1:8000/api/test/');
    //     this.message = response.data.message;
    //   } catch (error) {
    //     console.error('Error fetching message:', error);
    //   }
    // }
    async showQRCode() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/test/');
        this.message = response.data.message;
      } catch (error) {
        console.error('Error fetching message:', error);
      }
    }
  },
  components: {
    QrcodeVue
  }
};
</script>

<style>
#app {
  text-align: center;
  margin-top: 60px;
}
</style>
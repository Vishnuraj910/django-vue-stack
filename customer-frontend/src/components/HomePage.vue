<template>

  <v-container class="fill-height">
    <v-responsive class="align-centerfill-height mx-auto" max-width="900">

      <v-img class="mb-4" height="150" src="@/assets/kema-logo.png" />

      <div class="text-center">
        <div class="text-body-2 font-weight-light mb-5">Welcome</div>

        <h1 class="text-h4 font-weight-bold"> {{ customerDetails.customerName }}!</h1>
      </div>

      <div class="text-center mt-5 mb-10">

        <v-btn @click="cameraOn = !cameraOn" class="mb-5">
          {{ !cameraOn ? "Scan QR Code" : "Cancel" }}
        </v-btn>
        <!-- <camera v-if="cameraOn" :resolution="{ width: 375, height: 812 }" autoplay></camera> -->
        <StreamBarcodeReader v-if="cameraOn" @decode="onDecode" @loaded="onLoaded"></StreamBarcodeReader>
      </div>
      <div class="text-center mt-5 mb-16" v-show="isLoading">
        <v-progress-circular color="primary" indeterminate><span class="mt-18">Processing
            Payment</span></v-progress-circular>
      </div>

    </v-responsive>

  </v-container>
  <v-banner v-if="showAlert" class="bottom" color="primary" lines="one">
    <template v-slot:text>
      {{ alertMessage }}
    </template>

    <template v-slot:actions>
      <v-btn @click="showAlert = false">
        Dismiss
      </v-btn>
    </template>
  </v-banner>
</template>

<script>
//
import axios from 'axios';
// import { dummyUser } from '@/services/dummyData.js';
import { StreamBarcodeReader } from "vue-barcode-reader";
navigator.permissions.query({ name: 'camera' })
  .then((permissionObj) => {
    console.log(permissionObj.state);
  })
  .catch((error) => {
    console.log('Got error :', error);
  })
export default {
  name: 'App',
  data() {
    const customerDetails = { // This is a mock data. Will fetch from backend on JWT validation from cookie or after login
      customerName: 'Vishnuraj Rajagopal',
      device_metadata: { device: 'device1', os: 'android', browser: 'chrome' },
      balance: 100000,
      currency: 'AED'
    };
    return {
      customerDetails,
      cameraOn: false,
      isLoading: false,
      showAlert: false,
      alertMessage: ''
    };
  },
  methods: {
    onDecode(text) {
      // console.log(`Decode text from QR code is ${text}`)
      this.cameraOn = false
      this.isLoading = true
      const searchParams = new URLSearchParams(text);

      const paymentPayload = {
        customerName: this.customerDetails.customerName,
        device_metadata: JSON.stringify(this.customerDetails.device_metadata),
        balance: this.customerDetails.balance,
        currency: this.customerDetails.currency,
        merchantUUID: searchParams.get('merchantUUID') || 'HASHED_MERCHAT_ID_0001', // TODO Fix the issue with merchantUUID
        amount: searchParams.get('amount'),
        currency: searchParams.get('currency'),
        qrCode: text
      }
      if (this.customerDetails.currency !== paymentPayload.currency) {
        this.showAlert = true
        this.alertMessage = `Currency mismatch. Expected ${this.customerDetails.currency} but got ${paymentPayload.currency}`
        this.isLoading = false
        return
      }
      this.processPayment(paymentPayload);
      // setTimeout(() => {
      //   this.isLoading = false
      // }, 2000)
    },
    onLoaded() {
      console.log(`Ready to start scanning barcodes`)
    },
    processPayment(paymentPayload) {
      try {
        console.log("Data to process", paymentPayload);
        axios.post('http://127.0.0.1:8000/api/process/', paymentPayload).then(response => {
          console.log(response.data);
          this.showAlert = true
          this.alertMessage = "Payment processed successfully!"
        }).catch(error => {
          this.showAlert = true
          this.alertMessage = error.message
          console.error('Error fetching message:', error);
        }).finally(() => {
          this.isLoading = false
        });
      } catch (error) {
        console.error('Error fetching message:', error);
      }
    }
  },
  components: {
    StreamBarcodeReader
  }
};
</script>
<style scoped>
.v-progress-circular span {
  font-size: 20px;
  margin-top: 100px;
}

.bottom {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
}
</style>

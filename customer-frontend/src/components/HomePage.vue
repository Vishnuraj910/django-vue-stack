<template>
  <v-container class="fill-height">
    <v-responsive class="align-centerfill-height mx-auto" max-width="900">
      <v-img class="mb-4" height="150" src="@/assets/kema-logo.png" />

      <div class="text-center">
        <div class="text-body-2 font-weight-light mb-5">Welcome</div>

        <h1 class="text-h3 font-weight-bold"> {{ customerDetails.customerName }}!</h1>
      </div>

      <div class="text-center mt-5 mb-10">

        <v-btn>
          Scan QR Code
        </v-btn>

      </div>


    </v-responsive>
  </v-container>
</template>

<script>
//
import axios from 'axios';

export default {
  name: 'App',
  data() {
    const customerDetails = { // This is a mock data. Will fetch from backend on JWT validation from cookie or after login
      customerName: 'Vishnuraj Rajagopal',
      device_metadata: { device: 'device1', os: 'android', browser: 'chrome' },
      balance: 100000,
      currency: 'AED'
    }
    return {
      customerDetails,
    };
  },
  methods: {
    async showQRCode() {

    }
  },
  components: {

  }
};
</script>

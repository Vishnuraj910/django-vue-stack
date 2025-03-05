// This file contains dummy data for testing purpose. Will be replaced with actual data from backend
export default {
  dummyUser: { // This is a mock data. Will fetch from backend on JWT validation from cookie or after login
    customerName: 'Vishnuraj Rajagopal',
    device_metadata: { device: 'device1', os: 'android', browser: 'chrome' },
    balance: 100000,
    currency: 'USD'
  }
}

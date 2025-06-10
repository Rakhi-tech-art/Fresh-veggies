// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyD97ghiZWbbKdlXYQXViTGm0PV2kKv6jOQ",
  authDomain: "fresh-veggies-b5f72.firebaseapp.com",
  projectId: "fresh-veggies-b5f72",
  storageBucket: "fresh-veggies-b5f72.firebasestorage.app",
  messagingSenderId: "793804774564",
  appId: "1:793804774564:web:213c1bf4745b06d8f3da31",
  measurementId: "G-E1FTE4H698"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
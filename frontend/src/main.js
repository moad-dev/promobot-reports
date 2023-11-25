import './app.css'
import App from './App.svelte'

const app = new App({
  target: document.getElementById('app'),
})

export default app

window.API_URL = 'http://'+import.meta.env.VITE_API_HOST+':'+import.meta.env.VITE_API_PORT

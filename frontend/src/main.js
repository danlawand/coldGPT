import { createApp } from 'vue'
import { createRouter, createWebHistory} from 'vue-router'
import HomePage from './components/HomePage.vue'
import GenAI from './components/GenAI.vue'
import App from './App.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {path: '/', component: HomePage},
        {path: '/genai', component: GenAI}
    ]
});

const app = createApp(App)
app.use(router)
app.mount('#app')

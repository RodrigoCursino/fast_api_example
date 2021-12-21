import axios         from 'axios'
import config        from '@/config'
import { UserMixin } from "@/modules/User/UserMixin.js"

export const AjaxMixin = {
    mixins: [UserMixin],
    computed: {
        headers() {
            const self = this
            return {
                headers: {
                    Authorization: `Bearer ${self.get_token()}`
                }
            }
        }
    },
    methods: {
        get(url, param=null) {
           
            let response = null
            
            if(param) {
                response = axios.get(`${config.URL_BASE}${url}`, param, this.headers)
            } else {
                response = axios.get(`${config.URL_BASE}${url}`, param, this.headers)
            }

            return response
        },
        post(url, data) {
            console.info("this.get_token()", this.get_token())
            let response = axios.post(`${config.URL_BASE}${url}`, data, this.headers)
            return response
        },
        put(url, data) {
            let response = axios.put(`${config.URL_BASE}${url}`, data, this.headers)
            return response
        },
        delete(url, data) {
            let response = axios.delete(`${config.URL_BASE}${url}`, data, this.headers)
            return response
        },
    },
}
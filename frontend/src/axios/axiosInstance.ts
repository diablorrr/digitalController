import type {AxiosInstance} from 'axios'
import axios from 'axios'

const axiosInstance: AxiosInstance = axios.create({
    baseURL: 'http://localhost:5000',
    timeout: 120000
})

export default axiosInstance
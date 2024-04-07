import axios from 'axios'

const service = axios.create({
    baseURL: 'http://127.0.0.1:8000/', // Replace with your API base URL
    timeout: 40000, // Set the request timeout in milliseconds
    headers: {
        'Content-Type': 'application/json', // Set the default content type
    },
});

export default service
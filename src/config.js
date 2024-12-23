const config = {
    backendUrl: "https://recipe-makers.onrender.com", // Replace with your backend URL
};

export default config;
import config from './config';

fetch(`${config.backendUrl}/api/endpoint`, {
    method: 'GET',
});

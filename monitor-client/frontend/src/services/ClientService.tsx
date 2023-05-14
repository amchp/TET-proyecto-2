import axios from "axios";

const SERVER_URL = process.env.REACT_APP_SERVER_URL;

export async function setLoadToClient(load: number): Promise<void> {
    try {
        await axios.post(SERVER_URL + 'load/', {
            load: load
        });
    } catch (error: any) {
        throw error.response.data;
    }
}
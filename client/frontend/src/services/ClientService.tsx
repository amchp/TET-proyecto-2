import axios from "axios";

const SERVER_URL = process.env.PUBLIC_IP;

export async function setLoadToClient(load: number): Promise<void> {
    try {
        await axios.post(SERVER_URL + ':8000/load/', {
            load: load
        });
    } catch (error: any) {
        throw error.response.data;
    }
}
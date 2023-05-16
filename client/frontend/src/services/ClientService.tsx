import axios from "axios";

axios.defaults.baseURL = window.location.href.substring(0, window.location.href.length-1) + ":8000/";

export async function setLoadToClient(load: number): Promise<void> {
    try {
        console.log(axios.defaults.baseURL);
        await axios.post("load/", {
            load: load
        });
    } catch (error: any) {
        throw error.response.data;
    }
}
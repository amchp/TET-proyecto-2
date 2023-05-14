//import axios from "axios";
import { Client } from "../models/Client";

//const SERVER_URL = process.env.REACT_APP_SERVER_URL;


export async function getClients(): Promise<(Client)[]> {
    try {
        //const response = await axios.get(BACKEND_URL + '/api/developer/organization/');
        //const users: Developer[] = response.data.map((json: any) => {
        //    return JsonToUser(json);
        //});
        const client1 = new Client("1.1.1.1", "Client 1", 0.1, true);
        const client2 = new Client("2.2.2.2", "Client 2", 0.2, true);
        const client3 = new Client("3.3.3.3", "Client 3", 0.3, true);
        const client4 = new Client("4.4.4.4", "Client 4", 0.4, true);
        const client5 = new Client("5.5.5.5", "Client 5", 0.5, true);
        const client6 = new Client("6.6.6.6", "Client 6", 0.6, true);
        const client7 = new Client("7.7.7.7", "Client 7", 0.7, true);
        const client8 = new Client("8.8.8.8", "Client 8", 0.8, true);
        const client9 = new Client("9.9.9.9", "Client 9", 0.9, true);

        return [client1, client2, client3, client4, client5, client6, client7, client8, client9];
    } catch (error: any) {
        throw error.response.data;
    }
}

export async function createClient(): Promise<void> {

}

export async function deleteClient(): Promise<void> {

}

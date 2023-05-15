import axios from "axios";
import { Client } from "../models/Client";

const SERVER_URL = process.env.REACT_APP_SERVER_URL;


export async function getClients(): Promise<(Client)[]> {
    try {
        const response = await axios.get(SERVER_URL + '/servers/');
        const clients: Client[] = [];
        Object.keys(response.data).forEach((key) => {
            const clientObj = response.data[key];
            const client = new Client(key, clientObj.instance_id, clientObj.load, true);
            clients.push(client);
        });

        return clients;
    } catch (error: any) {
        throw error.response.data;
    }
}


export async function deleteClient(client: Client): Promise<void> {
    try {
        await axios.delete(SERVER_URL + '/servers/' + client.getIpAddress() + '/');
    } catch (error: any) {
        throw error.response.data;
    }
}


export async function createClient(): Promise<void> {
    try {
        await axios.post(SERVER_URL + '/servers/create/');
    } catch (error: any) {
        throw error.response.data;
    }
}


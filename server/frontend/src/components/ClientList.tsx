import { useEffect, useState } from 'react';
import { Client } from '../models/Client';
import ClientCard from './ClientCard';
import ModalCreateClient from './ModalCreateClient';
import { getClients } from '../services/ClientService';


function ClientList() {
    const [clients, setClients] = useState<Client[]>([]);

    const [modalIsOpen, setModalIsOpen] = useState(false);

    function openModal() {
        setModalIsOpen(true);
    }

    function closeModal() {
        setModalIsOpen(false);
    }

    useEffect(() => { 
        const interval = setInterval(() => {
            getClients().then((clients) => setClients(clients));
        }, 1000);
        return () => clearInterval(interval);
    });

    return (
        <div className='py-8  mx-auto w-full'>
            {modalIsOpen && (<ModalCreateClient closeModal={closeModal} />)}
            <div className='rounded-lg p-8 bg-gradient-to-r from-gray-800 to-dark-blue-800 shadow-2xl space-y-8'>
                <div className='flex items-center justify-between'>
                    <h2 className="text-2xl sm:text-5xl font-extrabold dark:text-white">Clientes</h2>

                    <button onClick={openModal} className="inline-block rounded-full bg-gradient-to-r from-fuchsia-700 to-blue-600 p-[4px] text-white focus:outline-none focus:ring active:text-opacity-75">
                        <span className="block rounded-full bg-dark-blue-800/60 px-8 py-2 text-sm font-medium hover:bg-dark-blue-800/40">
                            Crear cliente
                        </span>
                    </button>

                </div>

                <hr className="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700" />

                <ul className="grid sm:grid-cols-2 lg:grid-cols-3 grid-cols-1 gap-4">
                    {clients.map((client, index) =>
                        <li>
                            <ClientCard key={index} client={client}></ClientCard>
                        </li>
                    )}
                </ul>
            </div>
        </div>
    );
}

export default ClientList;
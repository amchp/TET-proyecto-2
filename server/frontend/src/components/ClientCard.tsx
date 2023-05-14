import { useState } from "react";
import { Client } from "../models/Client";
import ModalClient from "./ModalClient";

interface ClientCardProps {
    client: Client;
}

function ClientCard({ client }: ClientCardProps) {
    const loadColor = client.getLoad() < 0.4 ? "text-green-500" : client.getLoad() < 0.7 ? "text-yellow-500" : "text-red-500";

    const [modalIsOpen, setModalIsOpen] = useState(false);

    function openModal() {
        setModalIsOpen(true);
    }

    function closeModal() {
        setModalIsOpen(false);
    }

    return (
        <div className="w-full">
            {modalIsOpen && <ModalClient client={client} closeModal={closeModal} />}
            <button onClick={openModal} className="w-full transition ease-in-out hover:scale-105 hover:bg-indigo-500 duration-150 rounded-2xl max-w-md bg-gradient-to-r from-fuchsia-700 to-blue-600 p-1 shadow-2xl">
                <div className="transition block rounded-xl hover:bg-gray-800/50 duration-150 bg-gray-800/80 p-4 sm:p-6 lg:p-8" >
                    <div className="space-y-2 my-8 text-center">
                        <h3 className="text-3xl font-bold text-gray-200 ">
                            {client.getName()}
                        </h3>

                        <p className="text-xl text-white">
                            {client.getIpAddress()}
                        </p>

                        <p className={"text-7xl pt-8 " + loadColor}>
                            {client.getLoad() * 100}%
                        </p>
                    </div>
                </div>
            </button>
            
        </div>

    );
}

export default ClientCard;
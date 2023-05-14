import { ChangeEvent, useState } from 'react';
import { setLoadToClient } from '../services/ClientService';


function LoadCard() {
    const [load, setLoad] = useState(0.1);

    const loadColor = load < 0.4 ? "text-green-500" : load < 0.7 ? "text-yellow-500" : "text-red-500";
    const handleChange = (event: ChangeEvent<HTMLInputElement>) => {
        const rawValue: string = event.target.value;
        const parsedValue: number = parseFloat(rawValue);
        const roundedValue: number = parseFloat(parsedValue.toFixed(3));
        setLoad(roundedValue);
    };

    const handleRelease = () => {
        setLoadToClient(load).catch((error) => {
            console.log(error)
        });
    };

    return (
        <div className='py-8  mx-auto w-full'>
            <div className='rounded-lg p-8 bg-gradient-to-r from-gray-800 to-dark-blue-800 shadow-2xl space-y-8'>
                <div className='flex items-center justify-between'>
                    <h2 className="text-2xl sm:text-5xl font-extrabold dark:text-white">Simula tu propia carga</h2>
                </div>

                <hr className="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700" />

                <p className={"text-9xl text-center pt-8 " + loadColor}>
                    {(load * 100).toFixed(0)}%
                </p>

                <input
                    id="default-range"
                    type="range"
                    min={0}
                    max={1}
                    step={0.01}
                    value={load}
                    onChange={handleChange}
                    onMouseUp={handleRelease}
                    className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700"
                />


                <ul className="grid sm:grid-cols-2 lg:grid-cols-3 grid-cols-1 gap-4">

                </ul>
            </div>
        </div>
    );
}

export default LoadCard;
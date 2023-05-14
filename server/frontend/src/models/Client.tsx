export class Client {
    private _ip_address: string;
    private _name: string;
    private _load: number;
    private _is_alive: boolean;

    constructor(ip_address: string, name: string, load: number, is_alive: boolean) {
        this._ip_address = ip_address;
        this._name = name;
        this._load = load;
        this._is_alive = is_alive;
    }

    public getIpAddress(): string {
        return this._ip_address;
    }

    public getName(): string {
        return this._name;
    }

    public getLoad(): number {
        return this._load;
    }

    public getIsAlive(): boolean {
        return this._is_alive;
    }
}
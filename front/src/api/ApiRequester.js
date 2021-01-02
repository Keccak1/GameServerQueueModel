import axios from "axios";
import constants from "./apiConstants";

class ApiRequester {
    constructor(setStatus) {
        this.setStatus = setStatus;
        this.counter = 0;
    }

    async dummy() {
        console.log(this.counter);
        this.setStatus({ counter: this.counter });
        this.counter += 1;
        console.log(this.counter);
    }
    async addPlayer(playerName, regions) {
        const result = await axios.post(constants.addPlayerUrl, {
            name: playerName,
            regions: regions
        });
        if (result.status === 200) {
            this.setStatus(JSON.stringify(result.data));
            return true;
        }
    }

    async removePlayer(playerName) {
        const result = await axios.delete(
            `${constants.removePlayerUrl}/${playerName}`,
            {
                name: playerName
            }
        );

        if (result.status === 200) {
            this.setStatus(JSON.stringify(result.data));
            return true;
        }
    }

    async addRoom(playerName, roomName, regions) {
        const result = await axios.post(constants.removePlayerUrl, {
            player_name: playerName,
            room_name: roomName,
            regions: regions
        });

        if (result.status === 200) {
            this.setState(JSON.stringify(result.data));
            return true;
        }
    }
}

export default ApiRequester;

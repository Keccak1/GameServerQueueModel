import InputDialog from "../components/InputDialog";
import Queue from "../components/Queue";
import { UseGameStatus } from "../contexts/GameStatusContext";

import "./../style/lobby.css";

const Lobby = () => {
    const gameStatus = UseGameStatus();
    return (
        <div className={"lobbyContainer"}>
            <InputDialog />
            <span className={"queueSpan"}>Queue</span>
            {gameStatus && <Queue elements={gameStatus.queue} />}
        </div>
    );
};

export default Lobby;

import InputDialog from "../components/InputDialog";
import Queue from "../components/Queue";
import { UseGameStatus } from "../contexts/GameStatusContext";

import "./../style/lobby.css";

const Lobby = () => {
    const gameStatus = UseGameStatus();
    const elements = gameStatus.queue;
    return (
        <div className={"lobbyContainer"}>
            <InputDialog />
            <span className={"queueSpan"}>Queue</span>
            {elements && <Queue elements={elements} />}
        </div>
    );
};

export default Lobby;

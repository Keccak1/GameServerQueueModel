import InputDialog from "../components/InputDialog";
import Queue from "../components/Queue";

import "./../style/lobby.css";

const Lobby = () => {
    return(<div className={"lobbyContainer"}>
        <InputDialog />
        <span className={"queueSpan"}>Queue</span>
        <Queue parentName='Global' />
    </div>)
};

export default Lobby;

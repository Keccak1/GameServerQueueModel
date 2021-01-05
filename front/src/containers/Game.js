import Lobby from "./Lobby";
import Regions from "./Regions";
import { GameStatusProvider } from "../contexts/GameStatusContext";

import "../style/game.css";

const Game = () => {
    return (
        <div className={"gameContainer"}>
            <GameStatusProvider>
                <Lobby />
                <Regions />
            </GameStatusProvider>
        </div>
    );
};

export default Game;

import  { useEffect } from "react";
import Lobby from "./Lobby";
import Regions from "./Regions";

import "../style/game.css";

const Game = () => {
    
    return (
        <div className={"gameContainer"}>
            <Lobby />
            <Regions/>
        </div>
    );
};

export default Game;

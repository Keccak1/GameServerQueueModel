import React from "react";
import Lobby from "./containers/Lobby";
import Game from "./containers/Game";
import { GameStatusProvider } from "./contexts/GameStatusContext";

import "./style/app.css";

const App = () => {
    return (
        <main>
            <GameStatusProvider>
                <Lobby />
                <Game />
            </GameStatusProvider>
        </main>
    );
};

export default App;

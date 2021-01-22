import React from "react";
import Game from "./containers/Game";
import { GameStatusProvider } from "./contexts/GameStatusContext";
import "./style/app.css";

const App = () => {
    return (
        <GameStatusProvider>
            <Game />
        </GameStatusProvider>
    );
};

export default App;

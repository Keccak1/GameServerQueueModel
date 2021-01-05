import React from "react";
import Lobby from "./containers/Lobby";
import Regions from "./containers/Regions";
import { GameStatusProvider } from "./contexts/GameStatusContext";

import "./style/app.css";

const App = () => {
    return (
        <main>
            <GameStatusProvider>
                <Lobby />
                <Regions />
            </GameStatusProvider>
        </main>
    );
};

export default App;

import React, { useState } from "react";
import Player from "./Player";

import "../style/queue.css";

const dummyPlayers = ["Marcin", "Tomek", "Artur", "X", "A"];

const Queue = () => {
    const [players, setPlayers] = useState(dummyPlayers);
    const handleOnClicked = (toRemoveName) => {
        const newPlayers = players.filter((name) => name !== toRemoveName);
        setPlayers(newPlayers);
    };
    return (
        <div className={"queue"}>
            <ul>
                {players.map((player) => (
                    <Player
                        name={player}
                        key={player}
                        handleOnClicked={handleOnClicked}
                    />
                ))}
            </ul>
        </div>
    );
};

export default Queue;

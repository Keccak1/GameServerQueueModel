import React from "react";
import Player from "./Player";
import { UseSetGameStatus, UseGameStatus } from "../contexts/GameStatusContext";

import "../style/queue.css";

const Queue = ({ parrent }) => {
    const setGameStatus = UseSetGameStatus();
    const gameStatus = UseGameStatus();

    const getPlayers = (parrentName) => {
        if (parrentName === 'global') {
            return gameStatus.queue
        } else {
            const region = gameStatus.regions.find(region => region.name === parrent)
            if (region) {
                return region.queue
            }
        }
    }

    const players = getPlayers(parrent)
    return (
        <div className={"queue"}>
            {players && <ul>
                {
                    players.map((player) => {
                        return (
                            <Player
                                name={player.name}
                                key={player.name}
                                handleOnClick={() => setGameStatus.removePlayer(player.name)}
                            />
                        );
                    })}
            </ul>}
        </div>
    );
};

export default Queue;

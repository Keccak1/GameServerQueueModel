import React from "react";
import Player from "./Player";
import { UseSetGameStatus, UseGameStatus } from "../contexts/GameStatusContext";

import "../style/room.css";
import "../style/queue.css";

const Room = ({ roomName, regionName }) => {
    const gameStatus = UseGameStatus();
    const setGameStatus = UseSetGameStatus();
    const region = gameStatus.regions.find(region => region.name === regionName)
    const room = region.rooms.find(room => room.name === roomName)
    return (
        <div className={"room"}>
            <p className={"name"}>{roomName}</p>
            <div className={"queueWrapperRoom"}>
                <div className={"queue"}>
                    {room && <ul>
                        {
                            room.players.map((player) => {
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
            </div>
        </div>
    );
};

export default Room;

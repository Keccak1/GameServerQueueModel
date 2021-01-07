import React from "react";
import Queue from "./Queue";
import Room from "./Room";
import { UseGameStatus } from "../contexts/GameStatusContext";

import "../style/region.css";

const Region = ({ name }) => {
    const { regions } = UseGameStatus();
    const { queue, rooms } = regions.find((region) => region.name === name);
    const queuePlayers = queue.map(player => player.name)
    return (
        <div className={"regionWrapper"}>
            <h2>{name}</h2>
            <div className={"region"}>
                <div className={"queueWrapper"}>
                    <span className={"queueSpan"}>Queue</span>
                    {queuePlayers && <Queue elements={queuePlayers} />}
                </div>
                <div className={"roomsWrapper"}>
                    {rooms && rooms.map((room) => <Room roomName={room.name} elements={room.players.map(player=>player.name)}/>)}
                </div>
            </div>
        </div>
    );
};

export default Region;

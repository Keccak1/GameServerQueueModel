import React from "react";
import Queue from "./Queue";
import Room from "./Room";
import { UseGameStatus } from "../contexts/GameStatusContext";

import "../style/region.css";

const Region = ({ name }) => {
    const { regions } = UseGameStatus();
    const region = regions.find(region => region.name === name)
    return (
        <div className={"regionWrapper"}>
            <h2>{name}</h2>
            { region &&
                <div className={"region"}>
                    <div className={"queueWrapper"}>
                        <span className={"queueSpan"}>Queue</span>
                        <Queue parrent={region.name} />
                    </div>
                    <div className={"roomsWrapper"}>
                        {region && region.rooms.map((room) => <Room roomName={room.name} regionName={region.name} />)}
                    </div>
                </div>
            }
        </div>
    );
};

export default Region;

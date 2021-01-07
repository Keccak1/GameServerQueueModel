import React from "react";
import Queue from "./Queue";
import { UseGameStatus } from "../contexts/GameStatusContext";
import "../style/room.css";

const Room = ({ roomName, players }) => {
    return (
        <div className={"room"}>
            <p className={"name"}>{roomName}</p>
            <div className={"queueWrapperRoom"}>
                <Queue elements={players} />
            </div>
        </div>
    );
};

export default Room;

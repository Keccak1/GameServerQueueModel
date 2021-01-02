import React from "react";
import Queue from "./Queue";

import "../style/room.css";

const Room = ({ name }) => {
    return (
        <div className={"room"}>
            <p className={"name"}> name</p>
            <div className={"queueWrapperRoom"}>
                <Queue />
            </div>
        </div>
    );
};

export default Room;

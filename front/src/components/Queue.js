import React, { useState } from "react";
import Player from "./Player";
import { UseGameStatus } from "../contexts/GameStatusContext";

import "../style/queue.css";

const Queue = ({ elements }) => {
    return (
        <div className={"queue"}>
            <ul>
                {elements &&
                    elements.map((player) => {
                        return (
                            <Player
                                name={player.name}
                                key={player.name}
                                handleOnClick={() => console.log("XD")}
                            />
                        );
                    })}
            </ul>
        </div>
    );
};

export default Queue;

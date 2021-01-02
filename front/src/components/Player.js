import React from "react";
import "../style/player.css";

const Player = ({ name, handleOnClicked }) => {
    return (
        <li>
            <span>{name}</span>
            <button type='button' onClick={() => handleOnClicked(name)}>
                Remove
            </button>
        </li>
    );
};

export default Player;

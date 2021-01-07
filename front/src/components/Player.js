import React from "react";
import "../style/player.css";


const Player = ({ name, handleOnClick }) => {
    return (
        <li>
            <span>{name}</span>
            <button type='button' onClick={() => handleOnClick(name)}>
                Remove
            </button>
        </li>
    );
};

export default Player;

import React from "react";
import Region from "../components/Region";
import { UseGameStatus } from "../contexts/GameStatusContext";

import "./../style/regions.css";

const Regions = () => {
    const gameStatus = UseGameStatus();
    return (
        <div className={"regionsContainer"}>
            {gameStatus &&
                gameStatus.regions.map((region) => {
                    return <Region key={region.name} name={region.name} />;
                })}
        </div>
    );
};

export default Regions;

import React from "react";
import Region from "../components/Region";
import {UseGameStatus } from "../contexts/GameStatusContext";

import "./../style/regions.css";

const Regions = () => {
    const status = UseGameStatus();
    const regions = status.regions;
    console.log("regions", regions);
    return (
        <div className={"regionsContainer"}>
            {regions &&
                regions.map((region) => {
                    return <Region key={region.name} name={region.name} />;
                })}
        </div>
    );
};

export default Regions;

import React from "react";
import Region from "../components/Region";

import "./../style/regions.css";

const Regions = () => {
    return (
        <div className={"regionsContainer"}>
            <Region />
            <Region />
        </div>
    );
};

export default Regions;

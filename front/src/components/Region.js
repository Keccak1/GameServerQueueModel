import React from "react";
import Queue from "./Queue";
import Room from "./Room";
import "../style/region.css";

const Region = ({ name }) => {
    return (
        <div className={"regionWrapper"}>
            <h2>name</h2>
            <div className={"region"}>
                <div className={"queueWrapper"}>
                    <span className={"queueSpan"}>Queue</span>
                    <Queue />
                </div>
                <div className={"roomsWrapper"}>
                    <Room />
                    <Room />
                    <Room />
                    <Room />
                    <Room />
                    <Room />
                    <Room />
                    <Room />
                    <Room />
                    <Room />
                    <Room />
                    <Room />
                    <Room />
                    <Room />
                    <Room />
                    <Room />
                    <Room />
                    <Room />
                    <Room />
                </div>
            </div>
        </div>
    );
};

export default Region;

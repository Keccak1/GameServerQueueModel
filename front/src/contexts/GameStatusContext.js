import React, { useContext, useState, createContext } from "react";
import ApiRequester from "../api/ApiRequester";

const GameStatusRequesterContext = createContext();
const GameStatusContext = createContext();

export function UseGameStatus() {
    return useContext(GameStatusContext);
}

export function SetGameStatus() {
    return useContext(GameStatusRequesterContext);
}

export function GameStatusProvider({ children }) {
    const [status, setStatus] = useState({});
    const requester = new ApiRequester(setStatus);
    return (
        <GameStatusContext.Provider value={status}>
            <GameStatusRequesterContext.Provider value={requester}>
                {children}
            </GameStatusRequesterContext.Provider>
        </GameStatusContext.Provider>
    );
}

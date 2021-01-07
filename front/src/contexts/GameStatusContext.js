import React, { useContext, useState, useEffect, createContext } from "react";
import ApiRequester from "../api/ApiRequester";

const GameStatusRequesterContext = createContext();
const GameStatusContext = createContext();

export async function UseGameStatus() {
    return useContext(GameStatusContext);
}

export async function SetGameStatus() {
    return useContext(GameStatusRequesterContext);
}

export function GameStatusProvider({ children }) {
    const [gameStatus, setGameStatus] = useState({});
    const apiRequester = new ApiRequester(setGameStatus);

    const init = async () => {
        await apiRequester.fetchData();
    };

    useEffect(async () => {
        await init();
    }, []);

    return (
        gameStatus && (
            <GameStatusContext.Provider value={gameStatus}>
                <GameStatusRequesterContext.Provider value={apiRequester}>
                    {children}
                </GameStatusRequesterContext.Provider>
            </GameStatusContext.Provider>
        )
    );
}

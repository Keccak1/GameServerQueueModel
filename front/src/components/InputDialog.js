import React, { useState } from "react";
import InputDialogElement from "./InputDialogElement";
import { useForm } from "react-hook-form";
import { UseGameStatus, UseSetGameStatus } from "../contexts/GameStatusContext";

import "./../style/inputDialog.css";

const InputDialog = () => {
    const operations = ["Add Player", "Add Room", "Remove Player"];
    const [currentOption, setCurrentOperation] = useState(operations[0]);
    const { register, handleSubmit} = useForm();
    const gameStatus = UseGameStatus();
    const useGameStatus = UseSetGameStatus();

    const onSubmit = data => {
        const getRegions = data => {
            const regions = [];
            for (let i in data) {
                if (data[i] === true) {
                    regions.push(i)
                }
            }
            return regions.join(',')
        }
        const { operation, playerName, roomName } = data
        const regions = getRegions(data)
        switch (operation) {
            case "Add Player":
                useGameStatus.addPlayer(playerName, regions)
                break;
            case "Remove Player":
                useGameStatus.removePlayer(playerName)
                break;
            case "Add Room":
                useGameStatus.addRoom(playerName, roomName, regions)
                break;
            default:

        }
    }
    return (
        <div className={"inputDialogWrapper"}>
            <h1>{currentOption}</h1>
            {gameStatus && <form onSubmit={handleSubmit(onSubmit)} >

                <InputDialogElement labelName="Operation" key="operation" inputElement={<select name="operation" ref={register} onChange={(event) =>
                    setCurrentOperation(event.target.value)
                }>
                    {operations.map(operation => <option value={operation}>{operation}</option>)}
                </select>} />

                {currentOption === "Add Room" && (
                    <InputDialogElement labelName="Room Name"
                        key="roomName"
                        inputElement={<input name="roomName" placeholder="Room Name" ref={register({ required: true })} />} />

                )}
                <InputDialogElement
                    labelName='Player Name'
                    key='Player Name'
                    inputElement={
                        <input type='text' name="playerName" placeholder='Player Name' ref={register({ required: true })} />
                    }
                />
                {currentOption !== "Remove Player" && (
                    <InputDialogElement
                        labelName='Regions'
                        key='regions'
                        inputElement={
                            <div>
                                {
                                    gameStatus.regions.map((region) => (
                                        <div
                                            key={region.name}
                                            className={"inputDialogElement"}
                                        >
                                            <label>{region.name}</label>
                                            <input type='checkbox' name={region.name} ref={register} />
                                        </div>
                                    )
                                    )
                                }

                            </div>
                        }
                    />
                )}
                <button className={"submitButton"}>
                    {currentOption === "Remove Player" ? (
                        <span>Remove</span>
                    ) : (
                            <span>Add</span>
                        )}
                </button>
            </form>}

        </div>
    );
};

export default InputDialog;

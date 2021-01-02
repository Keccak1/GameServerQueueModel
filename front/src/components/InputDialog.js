import React, { useState } from "react";
import InputDialogElement from "./InputDialogElement";

import { useForm } from "react-hook-form";

import "./../style/inputDialog.css";
// TODO: useEffect fetch all regions
const InputDialog = () => {
    const operations = ["Add Player", "Add Room", "Remove Player"];
    const regions = ["Asia", "Europe"];
    const [currentOption, setCurrentOperation] = useState(operations[0]);
    const { register, handleSubmit, erorrs } = useForm();

    const onSubmit = (data) => console.log(currentOption);
    return (
        <div className={"inputDialogWrapper"}>
            <h1>{currentOption}</h1>
            <form onSubmit={handleSubmit(onSubmit)}>
                <InputDialogElement
                    labelName='Operation'
                    key='Operation'
                    inputElement={
                        <select
                            htmlFor='operation'
                            name='opearation'
                            onChange={(event) =>
                                setCurrentOperation(event.target.value)
                            }
                            ref={register}
                        >
                            {operations.map((operation) => (
                                <option key={operation}>{operation}</option>
                            ))}
                        </select>
                    }
                />
                {currentOption === "Add Room" && (
                    <InputDialogElement
                        labelName='Room Name'
                        key='Room Name'
                        inputElement={
                            <input type='text' placeholder='Room Name' />
                        }
                    />
                )}
                <InputDialogElement
                    labelName='Player Name'
                    key='Player Name'
                    inputElement={
                        <input type='text' placeholder='Player Name' />
                    }
                />
                {currentOption !== "Remove Player" && (
                    <InputDialogElement
                        labelName='Regions'
                        inputElement={
                            <div>
                                {regions.map((region) => (
                                    <div
                                        key={region}
                                        className={"inputDialogElement"}
                                    >
                                        <label>{region}</label>
                                        <input type='checkbox' />
                                    </div>
                                ))}
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
            </form>
        </div>
    );
};

export default InputDialog;

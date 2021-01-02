import React from "react";
import "./../style/inputDialogElement.css";

const InputDialogElement = ({labelName, inputElement}) => {
    return <div className="inputDialogElement">
        <label style={{padding: 10}}>{labelName}</label>
        {inputElement}
    </div>
}

export default InputDialogElement
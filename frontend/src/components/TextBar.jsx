import { useState, useEffect } from "react";

const TextBar = ({ message, setMessage, sendMessage }) => {
    const handleKeyPress = (event) => {
        if (event.key === "Enter") sendMessage();
    };

    return (
        <div className="flex items-center w-1/3">
            <input
                className="w-full h-10 bg-gray-200 indent-3 outline-none rounded-xl mr-2"
                onChange={(e) => setMessage(e.target.value)}
                value={message}
                onKeyDown={handleKeyPress}
            />
            <button
                className="w-20 h-10 bg-blue-500 text-white rounded-xl"
                onClick={() => sendMessage()}
            >
                Send
            </button>
        </div>
    );
};

export default TextBar;

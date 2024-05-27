import { TextBar, Message } from ".";
import { useState, useEffect, useRef } from "react";
import axios from "axios";

const ChatUI = () => {
    const [message, setMessage] = useState("");
    const [conversation, setConversation] = useState([]);
    const [isStart, setIsStart] = useState(true);

    const messagesEndRef = useRef(null);

    const sendMessage = () => {
        if (message !== "") {
            addConversation("user", message);
            setMessage("");
            getMessageResponse(message);
        }
    };

    const getMessageResponse = async (message) => {
        try {
            const response = await axios.post("http://localhost:5000/chat", {
                message: { role: "user", content: message },
                start: isStart,
            });
            console.log(response.data);
            const aiReply = response.data.reply;
            addConversation("system", aiReply);
            setIsStart(false);
        } catch (error) {
            console.error("Error sending message:", error);
        }
    };

    const addConversation = (role, content) => {
        const messages = content
            .split("\n")
            .map((line) => ({ role, content: line }));
        setConversation((prevConversation) => [
            ...prevConversation,
            ...messages,
        ]);
    };

    // Scroll to the bottom of the messages
    useEffect(() => {
        if (messagesEndRef.current) {
            messagesEndRef.current.scrollIntoView({ behavior: "smooth" });
        }
    }, [conversation]);

    return (
        <div className="flex flex-col justify-center items-center h-full">
            <div className="h-3/4 w-1/3 bg-gray-200 border flex justify-center mb-2 rounded-xl">
                <div className="w-full p-5 overflow-y-auto hide-scrollbar">
                    {conversation.map((message, idx) => (
                        <Message key={idx} message={message} />
                    ))}
                    {conversation.length === 0 && (
                        <span className="text-center">Start Chatting...</span>
                    )}
                    <div ref={messagesEndRef} />
                </div>
            </div>
            <TextBar
                message={message}
                setMessage={setMessage}
                sendMessage={sendMessage}
            />
        </div>
    );
};

export default ChatUI;

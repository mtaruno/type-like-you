const Message = ({ message }) => {
    return (
        <>
            {message.content !== "" && (
                <div
                    className={`mb-2 flex ${
                        message.role === "user"
                            ? "justify-end"
                            : "justify-start"
                    }`}
                >
                    <div
                        className={`p-3 rounded-lg max-w-xs 
        ${
            message.role === "user"
                ? "bg-blue-500 text-white"
                : "bg-gray-300 text-black"
        }`}
                    >
                        <p>{message.content}</p>
                    </div>
                </div>
            )}
        </>
    );
};

export default Message;

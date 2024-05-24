const Message = ({ message }) => {
    return (
        <>
            {message.message !== "" && (
                <div
                    className={`mb-2 flex ${
                        message.person === "user"
                            ? "justify-end"
                            : "justify-start"
                    }`}
                >
                    <div
                        className={`p-3 rounded-lg max-w-xs 
        ${
            message.person === "user"
                ? "bg-blue-500 text-white"
                : "bg-gray-300 text-black"
        }`}
                    >
                        <p>{message.message}</p>
                    </div>
                </div>
            )}
        </>
    );
};

export default Message;

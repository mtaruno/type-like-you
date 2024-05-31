import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

const Home = ({ profilePic, setProfilePic }) => {
    const [chatHistory, setChatHistory] = useState(null);
    const navigate = useNavigate();

    const handleProfilePicChange = (event) => {
        const file = event.target.files[0];
        setProfilePic(file ? URL.createObjectURL(file) : null);
    };

    const handleChatHistoryChange = (event) => {
        const file = event.target.files[0];
        setChatHistory(file ? file.name : null);
    };

    useEffect(() => {
        console.log(profilePic);
    }, [profilePic]);

    return (
        <div className="w-screen h-screen bg-gray-400 justify-center items-center flex flex-col">
            <div className="h-3/4 w-1/3 bg-gray-200 border flex flex-col justify-around items-center rounded-xl">
                <div className="flex flex-col justify-center items-center">
                    {profilePic ? (
                        <img
                            src={profilePic}
                            className="w-24 h-24 rounded-full"
                            alt="profile picture"
                        />
                    ) : (
                        <div className="w-24 h-24 rounded-full bg-gray-500"></div>
                    )}

                    <div className="flex flex-col justify-center items-center space-x-4 mt-2">
                        <label
                            htmlFor="file-upload"
                            className="cursor-pointer bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
                        >
                            Profile Picture
                        </label>
                        <input
                            id="file-upload"
                            type="file"
                            className="hidden"
                            onChange={handleProfilePicChange}
                        />
                    </div>
                </div>

                <div className="flex flex-col justify-center items-center space-x-4">
                    <label
                        htmlFor="file-upload2"
                        className="cursor-pointer bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
                    >
                        Chat History
                    </label>
                    <span className="text-gray-700 ml-0">{chatHistory}</span>
                    <input
                        id="file-upload2"
                        type="file"
                        className="hidden"
                        onChange={handleChatHistoryChange}
                    />
                </div>

                <button
                    className="w-20 h-10 bg-blue-500 text-white rounded-xl"
                    onClick={() => navigate("/chat")}
                >
                    Continue
                </button>
            </div>
        </div>
    );
};

export default Home;

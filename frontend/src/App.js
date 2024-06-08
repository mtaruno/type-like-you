import "./App.css";
import "./tailwind.css";
import { Home, ChatUI } from "./pages";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useState } from "react";

function App() {
    const [profilePic, setProfilePic] = useState(null);

    return (
        <BrowserRouter>
            <Routes>
                <Route
                    path="/"
                    exact
                    element={
                        <Home
                            profilePic={profilePic}
                            setProfilePic={setProfilePic}
                        />
                    }
                />
                <Route
                    path="/chat"
                    element={<ChatUI profilePic={profilePic} />}
                />
            </Routes>
        </BrowserRouter>
    );
}

export default App;

import "./App.css";
import "./tailwind.css";
import { ChatUI } from "./components";

function App() {
    return (
        <div className="w-screen h-screen bg-gray-500 justify-center items-center">
            <ChatUI />
        </div>
    );
}

export default App;

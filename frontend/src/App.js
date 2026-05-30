import React, { useEffect } from "react";
import SolveQuestion from "./components/SolveQuestion";
import "./App.css";

function App() {
    useEffect(() => {
        document.title = "Abstract: LeetCode AI Assistant"; // ✅ Set tab name
    }, []);
  return (
      <div className="App">
        <SolveQuestion />
      </div>
  );
}

export default App;

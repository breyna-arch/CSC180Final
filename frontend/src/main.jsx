import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import App from "./App";
import Loading from "./loadingPage"; 
import MermaidDiagram from "./flowchartPage";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/loadingPage" element={<Loading />} />
        <Route path="/flowchartPage" element={<MermaidDiagram />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

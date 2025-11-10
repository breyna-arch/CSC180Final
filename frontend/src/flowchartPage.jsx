import React, { useEffect, useRef } from "react";
import mermaid from "mermaid";
import { useLocation } from "react-router-dom";

export default function MermaidDiagram() {
  const mermaidRef = useRef(null);
  const location = useLocation();
  const response = location.state?.response || "";

  console.log("🧠 Raw response:\n", response);

  useEffect(() => {
    if (!mermaidRef.current || !response) return;

    // Clean and normalize Mermaid text
    const definition = response
      .replace(/^flowchart/, "graph") // fix old syntax
      .trim();

    console.log("📜 Final Mermaid definition:\n", definition);

    // Reinitialize Mermaid on each render
    mermaid.initialize({
      startOnLoad: false,
      theme: "default",
      securityLevel: "loose",
      logLevel: 1,
    });

    // Create a unique ID each time
    const id = `mermaid-${Math.floor(Math.random() * 100000)}`;

    // Actually render
    mermaid
      .render(id, definition)
      .then(({ svg }) => {
        console.log("✅ Mermaid render success");
        mermaidRef.current.innerHTML = svg;
      })
      .catch((err) => {
        console.error("❌ Mermaid render failed:", err);
        mermaidRef.current.innerHTML = `
          <div style="color:red;white-space:pre-wrap">
            <b>Mermaid Render Error:</b>\n${err.message || err}
          </div>
          <pre>${definition}</pre>
        `;
      });
  }, [response]);

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div
        ref={mermaidRef}
        className="mermaid-container bg-white p-4 rounded-xl shadow-md w-full max-w-5xl overflow-auto"
      >
        <p>Rendering flowchart...</p>
      </div>
    </div>
  );
}


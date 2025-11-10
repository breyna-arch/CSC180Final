import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function App() {
  const [text, setText] = useState("");
  const [response, setResponse] = useState("");
  const navigate = useNavigate();

  async function handleSubmit() {
    navigate("/loadingPage");

    try {
      const res = await fetch("http://localhost:5000/api/respond", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input: text })
      });

      const data = await res.text();
      setResponse(data);
      navigate("/flowchartPage", { state: { response: data } });
    } catch (e) {
      setResponse("Error: " + e.message);
    }
  }

  return (
    <div 
      className="app" 
      style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'top center',
        background: '#bf1be4ff',
        width: '100vw',
        height: '100vh',
        color: 'white'
      }}
    >
      <main 
        className="main"
        style={{
          alignItems: 'center',
          textAlign: 'center',
          background: 'transparent',
          maxWidth: '800px'
        }}
      >
        <section className="content">
          <p>
            This is a tool that leverages AI<br />
            to create a flowchart to help you visualize and solve problems.
          </p>

          <div 
            className="card"
            style={{
              background: 'transparent',
              textAlign: 'center',
              marginTop: '1em'
            }}
          >
            <textarea
              style={{ resize: "none" }}
              value={text}
              onChange={(e) => setText(e.target.value)}
              placeholder="Enter a problem..."
              className="border rounded-lg p-3 w-full h-48 focus:outline-none focus:ring focus:ring-blue-300"
              rows={10}
              cols={50}
            />

            <br />

            <button
              onClick={handleSubmit}
              style={{
                marginTop: '1em',
                background: 'white',
                color: '#bf1be4ff',
                border: 'none',
                borderRadius: '8px',
                padding: '10px 20px',
                cursor: 'pointer'
              }}
            >
              Submit
            </button>

            {response && (
              <div style={{ marginTop: '1em', background: 'white', color: 'black', padding: '1em', borderRadius: '8px' }}>
                <strong>Response:</strong>
                <p>{response}</p>
              </div>
            )}
          </div>
        </section>
      </main>
    </div>
  );
}

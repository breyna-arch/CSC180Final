# Final Project — CSC180

## Overview
This project is my **CSC180 Final Project** at **Sacramento State**. 
It is a full-stack web app with a **Python (Flash)** backend and a **React (Vite)** frontend.
The backend communicates with the **Google Docs API** and, combined with user input, generates **AI-created Mermaid flowcharts**, which can be visualized in the frontend.

The system flow:
1. User enters a prompt in the web app.
2. Backend (Python) fetches and processes a master prompt from Google Docs.
3. The OpenAI API (if configured) generates a Mermaid flowchart (uses LLM as a judge to correct its code).
4. The flowchart code is sent back to the frontend, which renders it visually.

---

Frontend (Vite + React):
- Location: `frontend/`
- Dev server: runs on port 5173 (default)

### Key Files
| File | Description |
|------|--------------|
| `src/App.jsx` | Main app logic and API integration |
| `src/main.jsx` | React app entry point |
| `src/styles.css` | Custom CSS styling |
| `src/loadingPage.jsx` | Presents loading screen while AI generates mermaid code |
| `src/flowchartPage.jsx` | Visualizes the AI generated Mermaid code in the form of a flowchart |
| `index.html` | Base HTML template for Vite |
| `package.json` | Node dependencies and scripts |

Backend (Flask):
- File: `backend_server.py`
- Endpoints:
  - `GET /api/ping` — returns {status: "ok"}
  - `POST /api/respond` — accepts JSON {"input": "..."}; if your OpenAI client is configured this will proxy to it.
- File: `config.py`
- File: `insert_prompt.py`
- File: `main.py`
- File: `mermaid_code_judge.py`
- File: `retrieve_master_prompt.py`

Quick start (Linux / bash):

1) Run backend

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# ensure OPENAI_API_KEY is set if you want to use /api/respond
export OPENAI_API_KEY="your_key_here"
python backend_server.py
```

2) Run frontend

```bash
cd frontend
npm install
npm run dev
```

Then open the Vite dev URL (usually http://localhost:5173). The "Ping Backend" button in the UI will call `http://localhost:5000/api/ping`.
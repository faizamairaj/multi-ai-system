uv setup:
uv init .
uv venv
.venv\Scripts\activate
uv run main.py
uv add openai-agents
uv add dotenv
uv add chainlit
create file .env
uv run chainlit run main.py -w (for terminal)


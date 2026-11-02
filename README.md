# PersonaAI

Personal AI companion MVP with configurable personality, persistent conversations and user-managed memories.

## Quick start

1. Install Docker Desktop with Docker Compose.
2. Copy `.env.example` to `.env`.
3. Optionally set `OPENAI_API_KEY` for real model responses (without it, demo mode stores chat messages).
4. Run `docker compose up --build`.
5. Open http://localhost:8000.

The app persists data in a Docker volume. Use the Personality tab to edit Sophia, the Memories tab to create explicit memories, and Chat to converse.

## Testing

`pip install -r requirements.txt && pytest -q`

## Security and scope

**Development use only.** The MVP has no authentication or multi-user support and intentionally binds to localhost. Do not deploy it publicly. Memory must be manually supplied; automated extraction and long-term semantic search are future milestones.

See [Architecture and roadmap](docs/ARCHITECTURE.md).

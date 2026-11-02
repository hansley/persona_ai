# PersonaAI architecture and delivery plan

## Working MVP (v0.1)

This is a local, single-user development prototype using FastAPI, SQLite and a small native web page. It persists chat history, allows persona edits, and supports explicit memory entry, listing and deletion. If an API key is supplied, the response engine sends the last 20 messages and up to 12 user-entered memories to OpenAI.

**Limitations:** no user authentication, no multi-user separation, no automated memory extraction, no vector retrieval, no event tracking, no background workers, and no relationship continuity beyond supplying explicit memories as context. The browser does not yet resume conversations after a reload. This is not production-ready.

## Target architecture

- Next.js responsive frontend with login, chat, personality studio, memory explorer and privacy settings.
- FastAPI application and LangGraph orchestration.
- PostgreSQL + pgvector for user-scoped episodic, semantic and event memory.
- Durable background jobs for memory extraction, confidence/provenance checks, approval and deduplication.
- Follow-up events that expire or close when no longer relevant.
- Prompt-injection defenses: memory and past dialogue are data, not instructions.
- OAuth/OIDC authentication and authorization checks on every data access.
- User-controlled data export, corrections, deletion and backup policies.

## Next milestones

1. Multi-user schema, OIDC auth, tenancy boundaries and permission tests.
2. PostgreSQL migration with embeddings and semantic memory ranking.
3. Memory approval, reconciliation and deletion propagation.
4. Continuity event processor and offline recall evaluations.
5. Frontend upgrade, streaming, rate limits, audit logs and deployment hardening.

## Local startup

Copy `.env.example` to `.env`, optionally supply `OPENAI_API_KEY`, and run `docker compose up --build`. Open http://localhost:8000. To test locally with Python, use `pip install -r requirements.txt && pytest -q`.

Never deploy the prototype to a public server. The Docker Compose port is intentionally bound to localhost only.

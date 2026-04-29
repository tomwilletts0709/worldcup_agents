# England World Cup Agent System

An agentic football companion for following England through the World Cup.

The aim of this project is to build a FastAPI backend powered by the LangChain
agent ecosystem, with specialist agents that can track England fixtures, analyse
players and opponents, reason about lineups, prepare match briefings, and make
predictions as the tournament unfolds.

After a pretty awful season following West Bromwich Albion, I thought I'd cheer myself 
up by really backing England to win the world cup. Usually I'm pretty negative about England's 
chances.. but not this year!

## Project Status

This is an early-stage build. The repository already contains the backend shape,
settings, football API client, data fixtures, agent module layout, and a health
endpoint. Several agent implementations are still placeholders while the core
interfaces and workflows are being worked out.

## What This Is For

The system is intended to answer questions such as:

- Who should England start against the next opponent?
- What are England's current strengths and weaknesses?
- Which players are in form, injured, or likely to start?
- How does the next opponent usually play?
- What tactical plan gives England the best chance?
- What does the data suggest about a coming fixture?

The longer-term goal is to make this feel less like a single chatbot and more
like a small coaching room: multiple agents with different jobs, shared context,
clear sources, and observable reasoning.

## Agent Architecture

The project is organised around specialist agents under `app/agents`.

| Agent | Purpose |
| --- | --- |
| `analyst` | Player, team, match, and tactical analysis. |
| `scout` | Opposition research and matchup notes. |
| `lineups` | Starting XI and squad selection reasoning. |
| `squad_planner` | Tournament squad planning and role coverage. |
| `tactician` | Shape, style, in-game plans, and tactical trade-offs. |
| `predictor` | Fixture predictions and confidence-scored outcomes. |
| `match_prep` | Match packs that combine news, form, tactics, and risks. |
| `orchestrator` | Coordinates specialist agents into a single workflow. |

The current plan is to use LangChain agents for tool use and structured
reasoning, with orchestration patterns evolving toward LangGraph where graph
state and multi-step routing become useful.

## Tech Stack

- FastAPI for the HTTP API.
- LangChain and `langchain-openai` for agent workflows.
- SQLModel and PostgreSQL for persistent data.
- Redis and Celery hooks for background or cached work.
- Football-data.org as the football data source. Need to workout better data sources. 
- Langfuse for observability, traces, prompt debugging, and evaluation.
- Pytest for tests.
- `uv` for dependency management.

## Repository Layout

```text
app/
  agents/              Specialist agent modules
  auth/                Authentication models and routing
  chat/                General chat agent scaffolding
  core/                Settings, logging, middleware, Redis, rate limiting
  data/                Local England data fixtures and schemas
  football/            Football API client and football domain models
  main.py              FastAPI application entrypoint

docs/
  planning.md          Early product and architecture notes

tests/
  test_main.py         API health check tests
  test_chat.py         Early chat test scaffolding
```

Each agent module follows the same rough shape:

```text
agent.py         LangChain agent definition
config.py        Agent-specific configuration
constants.py     Local constants
dependencies.py  FastAPI dependencies
exceptions.py    Agent-specific exceptions
models.py        SQLModel models
prompts.py       System prompts
repository.py    Persistence layer
router.py        API routes
service.py       Application logic around the agent
tools.py         Tools available to the agent
```

## Getting Started

Install dependencies:

```bash
uv sync
```

Create a `.env` file:

```bash
OPENAI_API_KEY=your_openai_api_key
FOOTBALL_STATS_API=your_football_data_api_key

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

REDIS_URL=redis://localhost:6379
FOOTBALL_API_BASE_URL=https://api.football-data.org/v4
```

Run the API:

```bash
uv run uvicorn app.main:app --reload
```

Check the health endpoint:

```bash
curl http://localhost:8000/health
```

## Configuration

Application settings are loaded from `app/core/settings.py` using Pydantic
settings. The main required values are:

- `OPENAI_API_KEY`
- `FOOTBALL_STATS_API`
- PostgreSQL connection settings
- `REDIS_URL`
- `FOOTBALL_API_BASE_URL`

Langfuse configuration is planned for the observability layer. Once wired in,
the project should trace agent runs, tool calls, prompts, model responses, and
evaluation metadata so match analysis can be inspected rather than guessed at.

## Running Tests

```bash
uv run pytest
```

Some tests are currently ahead of the implementation and may need updating as
the API shape settles.

## Roadmap

- Wire agent routers into the FastAPI application.
- Replace placeholder agent examples with England and World Cup workflows.
- Add Langfuse tracing around agent runs and tool calls.
- Add durable storage for analyses, predictions, match packs, and memory.
- Add scheduled jobs for fixtures, squad news, and matchday updates.
- Build a frontend for exploring reports and asking matchday questions.
- Add stronger test coverage around tools, services, and orchestrated agent
  flows.

## Notes

The architecture may change as the agent boundaries become clearer, but the north star stays the
same: make an agentic system that can follow England properly, explain its
thinking, and hopefully we'll win the world cup. 

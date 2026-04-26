ideas to map out for what sort of football related features I want and how this maps out in terms of structure etc. 


LangGraph/Chain - Will test both for agents

- Scout Agent
- Data Analyst Agent
- Transfer Agent
- LineUp Agent

The agent should:

- Understand latest team news (who is injured, who has recently started, predict lineup)
- What are the latest stats on the teams. 
- How should we lineup vs this opponent (Scout Agent)
- Analyse stats in the team and across the championship
- Understand strengths and weaknesses in the team based on stats


Example scenarios to handle:

1. How should West Brom lineup against Wolverhampton Wanderers based on recent form.
2. What is the prediction for the upcoming leage fixture against Birmingham City at St Andrews. 


Structure

following fastapi based on Netflix's Dispatch: 

app/
├── agents/
│   ├── scout/
│   │   ├── router.py        # POST /scout/lineup-advice
│   │   ├── schemas.py       # LineupRequest, LineupResponse
│   │   ├── service.py       # orchestrates the agent run
│   │   ├── agent.py         # LangGraph/LangChain agent definition
│   │   ├── tools.py         # tools specific to scouting
│   │   ├── prompts.py       # system prompts
│   │   ├── constants.py
│   │   └── exceptions.py
│   ├── analyst/
│   │   ├── router.py        # POST /analyst/stats
│   │   ├── schemas.py
│   │   ├── service.py
│   │   ├── agent.py
│   │   ├── tools.py
│   │   ├── prompts.py
│   │   └── constants.py

│   ├── transfers/
│   │   └── ...
│   └── lineup/
│       └── ...
├── football_api/
│   ├── client.py            # football-data.org HTTP client
│   ├── schemas.py           # raw API response models
│   ├── constants.py         # team IDs, league IDs
│   └── exceptions.py
├── cache/
│   └── redis.py
├── workers/
│   └── tasks.py             # Celery
├── database.py
├── config.py
├── models.py
├── exceptions.py
└── main.py

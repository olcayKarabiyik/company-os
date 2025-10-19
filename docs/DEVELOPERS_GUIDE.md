# Developers Guide

## Repository Overview
- `orchestrator/`: Core FastAPI backend controlling agents.
- `crew_configs/`: Defines crews (departments) and their goals.
- `langgraph/`: Graph workflows representing business processes.
- `agent_templates/`: Dockerized agent blueprints.
- `infra/k8s/`: Deployment and namespace manifests.

## Core Concepts
- **Agent Lifecycle:** creation → probation → registration → execution → decommission.
- **Crew:** logical grouping of agents around a shared mission.
- **Flow:** a LangGraph workflow representing a business process.

## Extending the System
1. Add new agent role under `agent_templates/`.
2. Register it in `crew_configs/`.
3. Define behavior in LangGraph flow.
4. Update orchestrator logic if new service boundaries are introduced.

## Coding Guidelines
- Modular imports only.
- All agent actions are idempotent.
- Configurations use YAML and environment variables.
- Logs must be structured JSON.

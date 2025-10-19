# System Design

## Architecture Overview
- **Orchestrator:** Central brain using FastAPI.
- **LangGraph Supervisor:** Cognitive planner defining workflows.
- **CrewAI Layer:** Handles team-level logic and role execution.
- **Agents:** Dockerized autonomous executors on Kubernetes.

## Data Flow
1. Orchestrator receives task or idea.
2. Passes context to LangGraph flow.
3. LangGraph determines next node and triggers CrewAI or orchestrator functions.
4. Agents perform assigned subtasks.
5. Results are logged and fed back into orchestrator memory or registry.

## Example Flow: Idea to Deployment
1. Receive idea.
2. Analyze market.
3. Build prototype.
4. Evaluate quality.
5. Deploy or hire more engineers.

## Integration Notes
- LangGraph triggers are asynchronous.
- CrewAI agents must publish results via orchestrator API.
- Kubernetes ensures runtime isolation.

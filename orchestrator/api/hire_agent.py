from fastapi import APIRouter
from orchestrator.services import registry, evaluator, k8s_client

router = APIRouter()

@router.post("/")
async def hire_agent(role: str, skills: list[str]):
    # Step 1. Create temporary namespace/pod
    pod_info = k8s_client.create_agent_pod(role, skills)

    # Step 2. Run probation tasks (simulate)
    results = evaluator.run_probation_tests(pod_info)

    # Step 3. Evaluate and register
    if results.get("score", 0) > 0.8:
        agent_id = registry.register_agent(pod_info)
        return {"status": "hired", "agent_id": agent_id}
    else:
        k8s_client.terminate_pod(pod_info)
        return {"status": "rejected"}

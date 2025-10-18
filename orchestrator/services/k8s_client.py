def create_agent_pod(role, skills):
    # Mock function for starter repo.
    # Replace with real Kubernetes API calls in production.
    pod_info = {"pod_name": f"agent-{role}-mock", "role": role, "skills": skills}
    return pod_info

def terminate_pod(pod_info):
    return True

import uuid
_REGISTRY = {}

def register_agent(pod_info):
    agent_id = str(uuid.uuid4())
    _REGISTRY[agent_id] = pod_info
    return agent_id

def list_agents():
    return _REGISTRY.copy()

import time
from langchain.llms import OpenAI

def main():
    # NOTE: This is a minimal mock agent for the starter repo.
    # In real usage, configure credentials and task queue integration.
    print('Code-writer agent starting (mock)')
    while True:
        # Poll tasks from orchestrator (omitted here)
        print('idle... (waiting for tasks)')
        time.sleep(10)

if __name__ == '__main__':
    main()

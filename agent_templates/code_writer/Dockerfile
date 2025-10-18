FROM python:3.11-slim
WORKDIR /app
COPY agent.py .
RUN pip install --no-cache-dir langchain openai
CMD ["python", "agent.py"]

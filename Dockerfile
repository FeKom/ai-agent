FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv

COPY pyproject.toml .
COPY src/ ./src/
COPY src/ ./logs/

RUN uv pip install --no-cache-dir --system -e .

RUN python -c "import httpx, langchain_community"

CMD ["docker exec -it ollama/ollama:latest bash ", "ollama run tinyllama"]
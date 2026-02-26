# Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1  
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    librdkafka-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY ingestion_service/requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# COPY shared/ ./shared/
COPY ingestion_service/app/ ./app/

CMD ["python", "-m", "ingestion_service.app.main"]

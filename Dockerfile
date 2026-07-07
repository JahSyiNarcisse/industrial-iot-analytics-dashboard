FROM python:3.11-slim AS builder

WORKDIR /app

# Only install build dependencies while building the image.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt --prefix /install

COPY src/ ./src/

FROM python:3.11-slim

WORKDIR /app

# Copy installed Python packages from the builder stage.
COPY --from=builder /install /usr/local
COPY --from=builder /app/src ./src/

# Create a non-root user and use it for runtime.
RUN useradd --create-home appuser && chown -R appuser /app
USER appuser

ENV PYTHONUNBUFFERED=1

EXPOSE 8000
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]

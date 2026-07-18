# Industrial IoT Analytics Dashboard

![Build, Scan, and Push Docker Image](https://github.com/JahSyiNarcisse/industrial-iot-analytics-dashboard/actions/workflows/docker-build-push.yml/badge.svg)

## Project
Industrial IoT (IIoT) Analytics Dashboard for AWS Cloud Engineering, DevOps, and Infrastructure as Code.

## Goals
- Build a cloud-native FastAPI application
- Containerize with Docker
- Deploy on AWS using Terraform and ECS Fargate
- Automate CI/CD with GitHub Actions
- Use CloudWatch for observability
- Practice security best practices and least-privilege IAM

## Current Status
- Project scaffold created
- FastAPI backend available with health, CPU, memory, disk, system, network, machine, and sensor endpoints
- Dark dashboard UI added at `/dashboard` with charts, cards, and live telemetry previews
- AWS deployment scaffolded with Terraform, ECS Fargate, ECR, and CloudWatch logging
- Local regression tests are included and passing with `python3 -m unittest discover -s tests -v`
- CI builds the Docker image, scans it with Trivy, and publishes it to GHCR on every push to `master`

## Local Development
1. `cd /Users/syi/industrial-iot-analytics-dashboard`
2. `python3 -m venv .venv`
3. `source .venv/bin/activate`
4. `pip install -r requirements.txt`
5. `uvicorn src.app.main:app --reload --host 0.0.0.0 --port 8000`
6. Open `http://localhost:8000`

## Docker
Build and run the container locally:

```bash
cd /Users/syi/industrial-iot-analytics-dashboard
docker compose build --no-cache
docker compose up -d
curl -sS http://127.0.0.1:8000/health
```

If you want to stop the service:

```bash
docker compose down
```

## Container Registry
CI publishes images to GitHub Container Registry (GHCR) on every push to `master`:
- `ghcr.io/jahsyinarcisse/industrial-iot-analytics-dashboard:<commit-sha>`
- `ghcr.io/jahsyinarcisse/industrial-iot-analytics-dashboard:latest`

## GitHub Actions
A workflow is included at `.github/workflows/docker-build-push.yml`.

What it does:
- builds the Docker image using `Dockerfile`
- scans the image with Trivy for high/critical vulnerabilities
- pushes the image to GHCR

## Project Structure
- `README.md` — project overview and next steps
- `.gitignore` — ignored files for Python and Terraform
- `.dockerignore` — ignored files during Docker build
- `Dockerfile` — container build definition
- `docker-compose.yml` — local compose development config
- `.github/workflows/docker-build-push.yml` — CI workflow for build/scan/push
- `requirements.txt` — Python dependencies
- `src/app/main.py` — FastAPI application entry point
- `src/app/routes.py` — API endpoints for telemetry and dashboard data
- `tests/test_routes.py` — unit tests for route functions

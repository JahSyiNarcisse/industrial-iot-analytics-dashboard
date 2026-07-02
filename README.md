# Industrial IoT Analytics Dashboard

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
- FastAPI backend skeleton available with health, CPU, memory, disk, system, network, machine, and sensor endpoints
- Local regression tests are included and passing

## Next Steps
1. `cd ~/ucf-cwep-iot-dashboard`
2. `python3 -m venv .venv`
3. `source .venv/bin/activate`
4. `pip install -r requirements.txt`
5. `uvicorn src.app.main:app --reload --host 0.0.0.0 --port 8000`
6. Visit `http://localhost:8000`

## Project Structure
- `README.md` — project overview and next steps
- `.gitignore` — ignored files for Python and Terraform
- `requirements.txt` — Python dependencies
- `src/app/main.py` — FastAPI application entry point
- `src/app/routes.py` — API endpoints for telemetry and dashboard data

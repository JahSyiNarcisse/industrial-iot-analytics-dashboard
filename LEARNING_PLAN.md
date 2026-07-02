# Learning Plan for CWEP Cloud Engineering Project

This plan is designed to help you learn while you build the project. Follow it week by week and use the project as hands-on practice.

## Week 1 — Git, GitHub, and Project Setup
- Learn Git basics: init, add, commit, branch, diff, merge, rebase
- Learn GitHub workflows: pull requests, branches, code reviews
- Resources:
  - Git Handbook: https://guides.github.com/introduction/git-handbook/
  - GitHub Learning Lab: https://lab.github.com/
  - Pro Git book: https://git-scm.com/book/en/v2
- Apply:
  - Initialize repo
  - Create a `main` branch and feature branches
  - Commit early and often with clear messages
  - Push code to GitHub

## Week 2 — Python and FastAPI
- Learn Python fundamentals: functions, classes, modules, environment variables
- Learn FastAPI basics: routes, request/response models, dependency injection
- Resources:
  - FastAPI docs: https://fastapi.tiangolo.com/
  - Real Python FastAPI tutorials
  - Python official tutorial: https://docs.python.org/3/tutorial/
- Apply:
  - Build the API endpoints in `src/app/routes.py`
  - Add environment-based configuration
  - Add simple tests later when ready

## Week 3 — Docker and Container Best Practices
- Learn Docker concepts: images, containers, Dockerfile, volumes, networking
- Learn best practices: multi-stage builds, non-root user, small images
- Resources:
  - Docker getting started: https://www.docker.com/get-started
  - Dockerfile best practices: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
- Apply:
  - Create a Dockerfile
  - Build and run locally
  - Use `curl` to verify endpoints

## Week 4 — AWS Basics and Infrastructure as Code
- Learn AWS core services: VPC, IAM, ECR, ECS, ALB, CloudWatch
- Learn Terraform basics: providers, resources, variables, state
- Resources:
  - AWS Cloud Practitioner Essentials
  - Terraform getting started: https://developer.hashicorp.com/terraform/tutorials
  - AWS Well-Architected Framework overview
- Apply:
  - Create Terraform scaffold for VPC and ECS
  - Define IAM roles and security groups
  - Plan and validate infrastructure with Terraform

## Week 5 — CI/CD and Deployment
- Learn GitHub Actions: workflows, jobs, secrets, actions marketplace
- Learn deployment flow: build, push, deploy, update containers
- Resources:
  - GitHub Actions docs: https://docs.github.com/actions
  - AWS ECR and ECS deployment guides
- Apply:
  - Add GitHub Actions workflow for lint/test/build/push/deploy
  - Use GitHub secrets for AWS credentials
  - Deploy the app through the workflow

## Week 6 — Observability and Security
- Learn CloudWatch logging, metrics, alarms, dashboards
- Learn AWS security fundamentals: least privilege, IAM roles, SSM Parameter Store
- Resources:
  - AWS CloudWatch docs: https://docs.aws.amazon.com/cloudwatch/
  - AWS IAM best practices
  - SSM Parameter Store docs
- Apply:
  - Configure application logs to CloudWatch
  - Add CloudWatch metrics for ECS
  - Store configuration in SSM Parameter Store

## Week 7 — Resume + Interview Preparation
- Learn how to describe architecture and decisions clearly
- Prepare answers for: scaling, security, trade-offs, AWS service choices
- Resources:
  - STAR interview method
  - AWS architecture question patterns
- Apply:
  - Write a polished README and project summary
  - Add architecture notes and deployment instructions
  - Practice explaining the project end to end

## Git Workflow Advice
- Branch naming:
  - `feature/api-endpoints`
  - `feature/docker-setup`
  - `feature/terraform-infra`
  - `feature/cicd-pipeline`
- Commit message examples:
  - `chore: initialize repo and add README`
  - `feat: add FastAPI health and system endpoints`
  - `chore: add Dockerfile and local run docs`
  - `infra: add Terraform VPC scaffold`
- Keep commits small and focused.

## Interview Talk Track
- Start with the problem: manufacturing telemetry, business insights, and cloud modernization
- Explain the architecture: GitHub → CI/CD → ECR → ECS Fargate → ALB → CloudWatch
- Highlight security: least-privilege IAM, SSM config, non-root container
- Mention what you learned: FastAPI, Docker, Terraform, AWS, GitHub Actions
- Frame it as an IIoT project with general cloud infrastructure applicability

# Terraform Guide for Industrial IoT Analytics Dashboard

This folder contains the Terraform scaffold to deploy the application to AWS ECS Fargate.

## What this project provisions
- `aws_ecs_cluster` for the application
- `aws_ecs_task_definition` referencing a Docker image
- `aws_ecs_service` running the task on Fargate
- IAM execution role for ECS tasks
- Security group allowing inbound HTTP traffic to port 8000

## AWS credentials
You should never store AWS credentials in the repository.
Use one of these local methods instead:

- `AWS_PROFILE=myprofile terraform apply`
- `export AWS_PROFILE=myprofile`
- `export AWS_ACCESS_KEY_ID=...`
- `export AWS_SECRET_ACCESS_KEY=...`
- `export AWS_REGION=us-east-1`

If you use GitHub Actions later, store secrets in GitHub repository settings and reference them in the workflow.

## Terraform basics
1. `terraform init`
   - downloads providers and initializes the working directory
2. `terraform plan -var-file=terraform.tfvars`
   - previews changes that Terraform will make
3. `terraform apply -var-file=terraform.tfvars`
   - creates or updates resources in AWS
4. `terraform destroy -var-file=terraform.tfvars`
   - removes the resources

## How to use this scaffold
1. Copy `terraform/terraform.tfvars.example` to `terraform/terraform.tfvars`
2. Fill in your own values for:
   - `container_image`
   - `vpc_id`
   - `subnet_ids`
3. From `terraform/`:
   ```bash
   terraform init
   terraform plan -var-file=terraform.tfvars
   terraform apply -var-file=terraform.tfvars
   ```

## What to expect
- Terraform will create an ECS cluster and service.
- The ECS task will use the container image URI you provide.
- The service is configured with `assign_public_ip = true` for easy initial access.
- You will still need a VPC and subnets in AWS.

## Learning points
- `terraform init` boots the directory and downloads plugins.
- `terraform plan` lets you review infrastructure changes.
- `terraform apply` actually provisions the resources.
- `variables.tf` defines the inputs your deployment needs.
- `outputs.tf` shows useful values after deployment.
- `main.tf` declares the actual AWS resources.

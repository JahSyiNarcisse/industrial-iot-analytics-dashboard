variable "aws_region" {
  description = "AWS region to deploy resources into"
  type        = string
  default     = "us-east-1"
}

variable "container_image" {
  description = "ECS container image URI"
  type        = string
}

variable "vpc_id" {
  description = "VPC ID for ECS service"
  type        = string
}

variable "subnet_ids" {
  description = "List of subnet IDs for ECS service"
  type        = list(string)
}

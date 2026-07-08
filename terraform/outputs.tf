output "ecs_cluster_id" {
  description = "ECS cluster ID"
  value       = aws_ecs_cluster.app_cluster.id
}

output "ecs_service_name" {
  description = "ECS service name"
  value       = aws_ecs_service.app_service.name
}

output "task_definition_arn" {
  description = "ECS task definition ARN"
  value       = aws_ecs_task_definition.app_task.arn
}

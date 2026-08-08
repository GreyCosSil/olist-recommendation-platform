resource "databricks_service_principal" "sp" {
  provider     = databricks
  display_name = var.service_principal_display_name
}

output "service_principal_name" {
  value = databricks_service_principal.sp.display_name
}

output "service_principal_id" {
  value = databricks_service_principal.sp.application_id
}

resource "databricks_schema" "teste_schema" {
  provider     = databricks
  catalog_name = "ml_training_dev"
  name         = var.schema_name
  comment      = "Schema criado via Terraform para testes do projeto"
}

output "schema_name" {
  value = databricks_schema.teste_schema.name
}
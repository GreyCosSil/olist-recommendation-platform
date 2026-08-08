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
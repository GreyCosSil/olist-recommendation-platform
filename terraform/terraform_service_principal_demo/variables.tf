variable "databricks_connection_profile" {
  description = "The name of the Databricks authentication configuration profile to use."
  type        = string
}

variable "service_principal_display_name" {
  description = "The display name for the service principal."
  type        = string
}

variable "service_principal_access_token_lifetime" {
  description = "The lifetime of the service principal's access token, in seconds."
  type        = number
  default     = 3600
}

variable "workspace_id" {
  description = "The Databricks workspace ID."
  type        = string
}

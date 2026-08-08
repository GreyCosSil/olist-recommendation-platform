# Olist Recommendation Platform

This repository contains a starter structure for building a recommendation platform on Databricks using Terraform, Databricks Asset Bundles, notebooks, and Python-based data science code.

## Overview

The project is organized to support:

- infrastructure provisioning with Terraform
- Databricks workflow orchestration with bundles
- data engineering and ML notebooks
- feature engineering and model training code
- documentation and tests for a scalable analytics workflow

## Project Structure

```text
olist-recommendation-platform/
├── README.md
├── requirements.txt
├── terraform/
│   └── terraform_service_principal_demo/
├── bundle/
│   ├── databricks.yml
│   └── resources/
├── notebooks/
├── src/
├── tests/
├── docs/
└── .github/workflows/
```

## Prerequisites

Before getting started, make sure you have:

- Python 3.10 or newer
- Terraform installed and available in your PATH
- Databricks CLI configured with a valid profile
- Access to a Databricks workspace

## Getting Started

1. Clone the repository.
2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure your Databricks authentication profile.

4. Initialize and apply the Terraform example:

   ```bash
   cd terraform/terraform_service_principal_demo
   terraform init
   terraform plan -var-file=terraform.tfvars
   terraform apply -var-file=terraform.tfvars
   ```

## Main Areas

- Terraform: infrastructure and access configuration
- Bundle: Databricks jobs and workflow definitions
- Notebooks: data processing, experimentation, and inference
- Src: reusable Python logic for feature engineering and modeling
- Docs: architecture and design references

## Next Steps

- Fill in the values in the Terraform variable files
- Add your real data sources and transformations
- Connect the workflows in the bundle configuration
- Expand the model training and inference pipeline

## Contributing

Feel free to adapt this structure to your machine learning and data platform needs. Keep the project organized by separating infrastructure, notebooks, code, and documentation.

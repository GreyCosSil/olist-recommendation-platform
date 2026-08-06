olist-recommendation-platform/
│
├── README.md
├── .gitignore
├── LICENSE
│
├── terraform/
│   ├── providers.tf
│   ├── variables.tf
│   ├── main.tf
│   ├── unity_catalog.tf
│   ├── workflows.tf
│   ├── permissions.tf
│   └── outputs.tf
│
├── bundle/
│   ├── databricks.yml
│   ├── resources/
│   │   ├── workflows.yml
│   │   └── jobs.yml
│   └── environments/
│       ├── dev.yml
│       └── prod.yml
│
├── notebooks/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
│   ├── features/
│   ├── training/
│   └── inference/
│
├── src/
│   ├── feature_engineering/
│   ├── models/
│   ├── utils/
│   └── config/
│
├── tests/
│
├── docs/
│   ├── architecture.md
│   ├── data_model.md
│   └── decisions.md
│
├── .github/
│   └── workflows/
│       ├── terraform.yml
│       └── databricks-bundle.yml
│
└── requirements.txt
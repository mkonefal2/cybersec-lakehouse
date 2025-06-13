# Databricks Lakehouse Data Engineering Capstone Project — **Cyber Security Log Analytics**

An end‑to‑end implementation blueprint demonstrating core Databricks Lakehouse capabilities for cybersecurity telemetry. The project leverages structured firewall logs and NetFlow v9 records to enable real-time ingestion, governance, transformation, orchestration, and serving of network-level data.

The solution includes batch and streaming ingestion pipelines, Delta Live Tables (DLT) with quality enforcement, Unity Catalog integration for secure governance, and final delivery via SQL dashboards. All components follow enterprise-grade architectural principles and can be deployed across development and production environments.

---

## 🗃️ Data Sources

* `firewall_logs.csv` — anonymized session log data (source/destination ports, bytes transferred, actions)
  → Source: [Internet Firewall Dataset – Kaggle](https://www.kaggle.com/datasets/tunguz/internet-firewall-data-set)

* `netflow_logs.csv` — NetFlow v9 network flow records (IP addresses, ports, durations, anomaly flags)
  → Source: [NetFlow V9 Network Data – Kaggle](https://www.kaggle.com/datasets/ashtcoder/network-data-schema-in-the-netflow-v9-format)

These files are processed via Auto Loader and should be made available in the object storage layer accessible by Databricks.

Additional data (e.g., synthetic anomalies, federated threat feeds) may be generated via `00_setup/01_generate_sample_data.py`.

---

## 🧱 Repository Layout

```text
.
├── 00_setup
│   ├── 01_generate_sample_data.py
│   ├── 02_create_uc_objects.sql
│   └── cluster_policy.json
├── 01_ingest_bronze
│   ├── 01_batch_fw_logs_autoloader.py
│   └── 02_stream_netflow_autoloader.py  <-- STREAMING INGESTION PIPELINE
├── 02_transform_silver
│   ├── 01_clean_fw_logs.sql
│   └── 02_cdc_upsert_netflow.py
├── 03_aggregate_gold
│   ├── 01_threat_indicator.sql
│   └── 02_traffic_baseline.sql
├── 04_dlt_pipeline
│   └── cybersec_dlt_pipeline.yaml
├── 05_workflows
│   └── cybersec_job.json
└── 99_tests
    └── test_data_quality.py
```

> For production automation or remote execution, all notebooks and pipelines support deployment via Databricks CLI and REST APIs.

---

## 🔁 Pipeline Stages

### 0. Environment Setup

* Unity Catalog metastore creation and configuration
* Cluster policy setup for secure, cost-controlled job execution
* Storage access configuration for ingestion layer

### 1. Bronze Layer Ingestion

| Task                      | Framework                                      | Script                                       |
| ------------------------- | ---------------------------------------------- | -------------------------------------------- |
| Ingest firewall batch     | Auto Loader (triggerOnce)                      | `01_batch_fw_logs_autoloader.py`             |
| Ingest NetFlow streaming  | Auto Loader (cloudFiles), Structured Streaming | `02_stream_netflow_autoloader.py`            |
| External query federation | PostgreSQL via Lakehouse Federation            | `SELECT * FROM cybersec_foreign.siem_alerts` |

### 2. Silver Layer Transformation

* Schema normalization, timestamp casting, column remapping
* Merge upserts using Change Data Feed (CDF)
* Constraint enforcement via Delta expectations and SQL constraints

### 3. Gold Layer Aggregation

* Multi-window aggregations of flow and threat data
* Z-ORDER clustering for high-performance filtering on `dest_ip` and `timestamp`
* Visualization-ready table generation for SOC dashboards

### 4. Declarative ETL with Delta Live Tables

* Modular DLT pipeline defined in YAML (`cybersec_dlt_pipeline.yaml`)
* Includes row-level expectations and continuous refresh scheduling
* Integrated monitoring via event logs and audit views

### 5. Orchestration

* Workflow definition in JSON (`cybersec_job.json`) supporting dependencies and alerts
* Execution graph: Bronze Ingest → DLT → Gold Aggregation → Notification

### 6. CI/CD and Deployment

* CLI-based deployment using Databricks Bundles 0.3+
* GitHub Actions pipeline with promotion across dev/staging/prod
* Secrets and environment config abstracted for multi-stage promotion

### 7. Monitoring and Optimization

* DLT log ingestion and visualization in Databricks SQL
* Photon engine activation, auto-scaling clusters, cloudFiles tuning

---

## 🧪 Testability

* Data quality assertions via expectations and unit tests
* Isolated test data for regression and logic verification (`99_tests/test_data_quality.py`)

---

## 🔐 Security & Governance

* Unity Catalog enforcement (catalogs, schemas, views, row-level security)
* Audit-ready lineage and permission granularity
* Reusable cluster policy with job scope limitation

---

## 🔗 Execution Snippets

```bash
# Trigger notebook or workflow execution
 databricks jobs run-now --job-id <job_id>

# Grant read access via Unity Catalog
 GRANT SELECT ON TABLE cybersec.gold.threat_indicator TO `soc_analyst_role`;

# Optimize and index gold table
 OPTIMIZE cybersec.gold.threat_indicator ZORDER BY (dest_ip, timestamp);

# Query federated threat intel
 SELECT * FROM cybersec_foreign.threatintel.feeds LIMIT 100;
```

---

## 📎 References

* Databricks Lakehouse Security Best Practices 2025
* Delta Live Tables: Production Deployment Guide
* Unity Catalog Administration & Auditability
* Federation Query Patterns for Multicloud Access

---

> This documentation describes a modular, production-oriented architecture for high-volume cybersecurity telemetry processing using Databricks Lakehouse Platform.

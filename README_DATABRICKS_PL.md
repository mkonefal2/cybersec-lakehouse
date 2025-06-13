# Instrukcja korzystania z repozytorium Cyber Security Lakehouse na platformie Databricks

Niniejszy dokument opisuje krok po kroku jak uruchomić skrypty i pipeline'y z repozytorium w środowisku Databricks. Całość bazuje na plikach znajdujących się w katalogach `00_setup` – `05_workflows`.

## 1. Przygotowanie środowiska

1. Utwórz lub wskaż metastore Unity Catalog i nadaj odpowiednie uprawnienia.
2. Opcjonalnie zastosuj politykę klastra z pliku `00_setup/cluster_policy.json`.
3. Wygeneruj przykładowe dane (jeśli nie posiadasz własnych plików) uruchamiając
   ```bash
   python 00_setup/01_generate_sample_data.py --output /path/do/storage
   ```
4. Utwórz obiekty w katalogu `cybersec` korzystając z zapytania SQL z pliku `00_setup/02_create_uc_objects.sql`.

## 2. Warstwa Bronze – Ingest danych

* Batchowe wczytanie logów zapory:
  ```bash
  spark-submit 01_ingest_bronze/01_batch_fw_logs_autoloader.py /path/do/firewall_logs
  ```
* Strumieniowe wczytanie logów NetFlow:
  ```bash
  spark-submit 01_ingest_bronze/02_stream_netflow_autoloader.py /path/do/netflow_logs
  ```
  Skrypt zakłada, że w katalogu wejściowym utworzone zostaną podkatalogi `_schema` oraz `_checkpoint`.

## 3. Warstwa Silver – Transformacja

1. Oczyść dane firewallowe uruchamiając zapytanie `02_transform_silver/01_clean_fw_logs.sql` w SQL Warehouse lub notebooku.
2. Wykonaj operację `MERGE` na logach NetFlow poleceniem
   ```bash
   spark-submit 02_transform_silver/02_cdc_upsert_netflow.py cybersec.bronze.netflow_logs
   ```
   Skrypt tworzy lub aktualizuje tabelę `cybersec.silver.netflow_logs`.

## 4. Warstwa Gold – Agregacja

Utwórz tabele agregacyjne wykonując kolejno zapytania z katalogu `03_aggregate_gold`:

```sql
-- Threat indicators
03_aggregate_gold/01_threat_indicator.sql

-- Podstawowe metryki ruchu
03_aggregate_gold/02_traffic_baseline.sql
```

## 5. Delta Live Tables

Plik `04_dlt_pipeline/cybersec_dlt_pipeline.yaml` definiuje pipeline DLT. Można go zaimportować w interfejsie Databricks lub uruchomić przez CLI:

```bash
databricks pipelines create --json-file 04_dlt_pipeline/cybersec_dlt_pipeline.yaml
```

Pipeline pracuje w trybie ciągłym (`continuous: true`).

## 6. Orkiestracja Workflow

Konfiguracja zadania w formacie JSON znajduje się w `05_workflows/cybersec_job.json`. Aby utworzyć zadanie, wykonaj:

```bash
databricks jobs create --json-file 05_workflows/cybersec_job.json
```

Następnie można je uruchomić poleceniem:

```bash
databricks jobs run-now --job-id <job_id>
```

## 7. Testy

Repozytorium zawiera prosty test jakości danych w `99_tests/test_data_quality.py`. Test można uruchomić lokalnie lub w środowisku Databricks:

```bash
pytest 99_tests/test_data_quality.py
```

## 8. Przydatne komendy SQL

```sql
-- Przyznanie dostępu do tabeli gold
GRANT SELECT ON TABLE cybersec.gold.threat_indicator TO `soc_analyst_role`;

-- Optymalizacja i indeksowanie
OPTIMIZE cybersec.gold.threat_indicator ZORDER BY (dest_ip, timestamp);
```

---

Dokument opisuje najważniejsze kroki umożliwiające uruchomienie i rozwijanie projektu cyberbezpieczeństwa w oparciu o platformę Databricks.

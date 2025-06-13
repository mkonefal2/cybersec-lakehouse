import csv
import os
from pathlib import Path

DATA_DIR = Path("data")


def test_firewall_log_exists():
    path = DATA_DIR / "firewall_logs.csv"
    assert path.exists(), "firewall_logs.csv should be generated"


def test_netflow_log_exists():
    path = DATA_DIR / "netflow_logs.csv"
    assert path.exists(), "netflow_logs.csv should be generated"


def test_firewall_schema():
    path = DATA_DIR / "firewall_logs.csv"
    with open(path) as f:
        reader = csv.reader(f)
        header = next(reader)
    assert "Source Port" in header
    assert "Destination Port" in header


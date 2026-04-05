"""runs the full pipeline end-to-end"""
import subprocess
from pathlib import Path
from typing import Dict, List, Set, Tuple
import sys


ROOT = Path(__file__).resolve().parent.parent

DATA_FILE = ROOT / "data" / "reviews_clean.jsonl"
METRICS_DIR = ROOT / "metrics"

subprocess.run([sys.executable, ROOT / "src" / "00_validate_repo.py"], check=True)

subprocess.run([sys.executable, ROOT / "src" / "01_collect_or_import.py"], check=True)

#Cleans review data, produces data/reviews_clean.jsonl
subprocess.run([sys.executable, ROOT / "src" / "02_clean.py"], check=True)


#Generate review groups data/review_groups_auto.json using data/reviews_clean.jsonl and personas output to personas/personas_auto.json
subprocess.run([sys.executable, ROOT / "src" / "05_personas_auto.py"], check=True)

#Generate requirements spec using personas. Spec file spec/spec_auto.md
subprocess.run([sys.executable, ROOT / "src" / "06_spec_generate.py"], check=True)

#Generate tests using spec. Output file tests/tests_auto.json
subprocess.run([sys.executable, ROOT / "src" / "07_tests_generate.py"], check=True)

#Generate metrics across pipelines: metrics/metrics_manual.json, metrics/metrics_auto.json, metrics/metrics_hybrid.json, metrics/metrics_summary.json
subprocess.run([sys.executable, ROOT / "src" / "08_metrics.py"], check=True)

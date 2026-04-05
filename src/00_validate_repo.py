"""checks required files/folders exist"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
required_dirs = [ROOT / "data", ROOT / "src", ROOT / "spec", ROOT / "personas", ROOT / "reflection", ROOT / "tests", ROOT / "metrics", ROOT / "prompts"]

required_files = [
    # data
    ROOT / "data/reviews_raw.jsonl",
    ROOT / "data/reviews_clean.jsonl",
    ROOT / "data/dataset_metadata.json",
    ROOT / "data/review_groups_manual.json",
    ROOT / "data/review_groups_hybrid.json",

    # personas
    ROOT / "personas/personas_manual.json",
    ROOT / "personas/personas_auto.json",
    ROOT / "personas/personas_hybrid.json",

    # spec
    ROOT / "spec/spec_manual.md",
    ROOT / "spec/spec_auto.md",
    ROOT / "spec/spec_hybrid.md",

    # metrics
    ROOT / "metrics/metrics_manual.json",
    ROOT / "metrics/metrics_auto.json",
    ROOT / "metrics/metrics_hybrid.json",

    # tests
    ROOT / "tests/tests_manual.json",
    ROOT / "tests/tests_auto.json",
    ROOT / "tests/tests_hybrid.json",

    # reflection + root
    ROOT / "reflection/reflection.md",
    ROOT / "README.md",

    # src
    ROOT / "src/00_validate_repo.py",
    ROOT / "src/01_collect_or_import.py",
    ROOT / "src/02_clean.py",
    ROOT / "src/03_manual_coding_template.py",
    ROOT / "src/04_personas_manual.py",
    ROOT / "src/05_personas_auto.py",
    ROOT / "src/06_spec_generate.py",
    ROOT / "src/07_tests_generate.py",
    ROOT / "src/08_metrics.py",
    ROOT / "src/run_all.py",
]

failed = False

# --- Check directories ---
print("\nChecking directories:")
for d in required_dirs:
    path = Path(d)
    if not path.exists():
        print(f"{d} does not exist")
        failed = True
    elif not path.is_dir():
        print(f"{d} exists but is not a directory")
        failed = True
    else:
        print(f"{d} is OK")

# --- Check files ---
print("\nChecking files:")
for f in required_files:
    if not f.exists():
        print(f"Missing file: {f}")
        failed = True
    elif not f.is_file():
        print(f"Not a file: {f}")
        failed = True
    else:
        print(f"OK: {f}")

# --- Final result ---
print("\n" + "="*40)

if failed:
    print("REPO VALIDATION FAILED")
    exit(1) 
else:
    print("REPO VALIDATION PASSED")
    exit(0)

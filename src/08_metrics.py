"""computes metrics: coverage/traceability/testability"""
import json
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple


ROOT = Path(__file__).resolve().parent.parent

DATA_FILE = ROOT / "data" / "reviews_clean.jsonl"
METRICS_DIR = ROOT / "metrics"

PIPELINES = {
    "manual": {
        "personas": ROOT / "personas" / "personas_manual.json",
        "spec": ROOT / "spec" / "spec_manual.md",
        "tests": ROOT / "tests" / "tests_manual.json",
    },
    "auto": {
        "personas": ROOT / "personas" / "personas_auto.json",
        "spec": ROOT / "spec" / "spec_auto.md",
        "tests": ROOT / "tests" / "tests_auto.json",
    },
    "hybrid": {
        "personas": ROOT / "personas" / "personas_hybrid.json",
        "spec": ROOT / "spec" / "spec_hybrid.md",
        "tests": ROOT / "tests" / "tests_hybrid.json",
    },
}


REQ_ID_PATTERN = re.compile(
    r"^\s*#+\s*Requirement ID:\s*([A-Za-z0-9_-]+)\s*$",
    re.MULTILINE,
)

SOURCE_PERSONA_PATTERN = re.compile(
    r"^\s*-\s*Source Persona:\s*(.+?)\s*$",
    re.MULTILINE,
)

def count_dataset_size(path: Path) -> int:
    with path.open("r", encoding="utf-8") as f:
        return sum(1 for line in f if line.strip())


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def parse_requirements_from_spec(path: Path) -> Tuple[List[str], int]:
    text = path.read_text(encoding="utf-8")

    requirement_ids = REQ_ID_PATTERN.findall(text)
    source_persona_matches = SOURCE_PERSONA_PATTERN.findall(text)

    traced_requirements = len(source_persona_matches)

    return requirement_ids, traced_requirements


def extract_review_ids_from_personas(personas_data: dict) -> Set[str]:
    review_ids: Set[str] = set()

    for persona in personas_data.get("personas", []):
        for rid in persona.get("evidence_reviews", []):
            if isinstance(rid, str) and rid.strip():
                review_ids.add(rid.strip())

    return review_ids


def extract_requirement_ids_from_tests(tests_data: dict) -> List[str]:
    ids: List[str] = []

    for test in tests_data.get("tests", []):
        rid = test.get("requirement_id")
        if isinstance(rid, str) and rid.strip():
            ids.append(rid.strip())

    return ids


def compute_pipeline_metrics(
    pipeline_name: str,
    personas_path: Path,
    spec_path: Path,
    tests_path: Path,
    dataset_size: int,
) -> Dict:
    personas_data = load_json(personas_path)
    tests_data = load_json(tests_path)

    persona_count = len(personas_data.get("personas", []))
    unique_review_ids = extract_review_ids_from_personas(personas_data)
    review_count_used = len(unique_review_ids)

    requirement_ids, traced_requirements = parse_requirements_from_spec(spec_path)
    unique_requirement_ids = list(dict.fromkeys(requirement_ids))
    requirements_count = len(unique_requirement_ids)

    test_requirement_ids = extract_requirement_ids_from_tests(tests_data)
    tests_count = len(tests_data.get("tests", []))

    tested_requirements = set(test_requirement_ids) & set(unique_requirement_ids)
    requirements_with_tests = len(tested_requirements)

    review_coverage_ratio = (
        review_count_used / dataset_size if dataset_size > 0 else 0.0
    )
    traceability_ratio = (
        traced_requirements / requirements_count if requirements_count > 0 else 0.0
    )
    testability_rate = (
        requirements_with_tests / requirements_count if requirements_count > 0 else 0.0
    )

    metrics = {
        "pipeline": pipeline_name,
        "dataset_size": dataset_size,
        "persona_count": persona_count,
        "requirements_count": requirements_count,
        "tests_count": tests_count,
        "review_coverage_ratio": round(review_coverage_ratio, 5),
        "traceability_ratio": round(traceability_ratio, 5),
        "testability_rate": round(testability_rate, 5),
    }

    return metrics


def main() -> None:
    METRICS_DIR.mkdir(parents=True, exist_ok=True)

    dataset_size = count_dataset_size(DATA_FILE)

    summary = {}

    for pipeline_name, paths in PIPELINES.items():
        metrics = compute_pipeline_metrics(
            pipeline_name=pipeline_name,
            personas_path=paths["personas"],
            spec_path=paths["spec"],
            tests_path=paths["tests"],
            dataset_size=dataset_size,
        )

        output_path = METRICS_DIR / f"metrics_{pipeline_name}.json"
        with output_path.open("w", encoding="utf-8") as f:
            json.dump(metrics, f, indent=2)

        summary[pipeline_name] = metrics

    summary_path = METRICS_DIR / "metrics_summary.json"
    with summary_path.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print("Metrics computed successfully.")
    for pipeline_name, metrics in summary.items():
        print(f"\n{pipeline_name.upper()}:")
        for key, value in metrics.items():
            if key != "pipeline":
                print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
import argparse
import csv
import json
from pathlib import Path


ACTION_TERMS = {"approved", "piloted", "mapping", "planning", "resilience", "continuity"}
DEFERRED_TERMS = {"review", "planned", "pending", "under review"}
SOURCE_REVIEW_FIELDS = ("source_type", "retrieval_date", "quote_permission")


def score_excerpt(excerpt: str) -> int:
    text = excerpt.lower()
    score = sum(1 for term in ACTION_TERMS if term in text)
    score -= sum(1 for term in DEFERRED_TERMS if term in text)
    return score


def summarize_source_review(rows: list[dict[str, str]]) -> dict[str, object]:
    ready_rows = sum(
        1
        for row in rows
        if all(row.get(field, "").strip() for field in SOURCE_REVIEW_FIELDS)
    )
    permission_statuses = sorted(
        {
            row.get("quote_permission", "").strip()
            for row in rows
            if row.get("quote_permission", "").strip()
        }
    )
    return {
        "required_fields": list(SOURCE_REVIEW_FIELDS),
        "ready_rows": ready_rows,
        "missing_rows": len(rows) - ready_rows,
        "permission_statuses": permission_statuses,
    }


def summarize(path: Path) -> dict[str, object]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    if not rows:
        raise ValueError("At least one disclosure row is required.")

    scored = [
        {
            "company": row["company"],
            "sector": row["sector"],
            "score": score_excerpt(row["excerpt"]),
        }
        for row in rows
    ]

    average_score = sum(item["score"] for item in scored) / len(scored)
    sectors = sorted({row["sector"] for row in rows})
    return {
        "rows": len(scored),
        "average_score": round(average_score, 2),
        "sector_count": len(sectors),
        "sectors": sectors,
        "source_review": summarize_source_review(rows),
        "highest_signal": max(scored, key=lambda item: item["score"]),
        "scored_companies": scored,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize synthetic climate adaptability excerpts.")
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()
    print(json.dumps(summarize(args.csv_path), indent=2))


if __name__ == "__main__":
    main()


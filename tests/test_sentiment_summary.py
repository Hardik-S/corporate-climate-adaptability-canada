import unittest
from pathlib import Path

from src.sentiment_summary import score_excerpt, summarize


FIXTURE = Path(__file__).resolve().parents[1] / "data" / "synthetic_disclosures.csv"


class SentimentSummaryTests(unittest.TestCase):
    def test_action_terms_raise_score(self) -> None:
        self.assertGreater(score_excerpt("The board approved resilience planning."), 0)

    def test_deferred_terms_lower_score(self) -> None:
        self.assertLess(score_excerpt("Funding remains under review and pending."), 0)

    def test_summary_identifies_highest_signal(self) -> None:
        result = summarize(FIXTURE)
        self.assertEqual(result["rows"], 4)
        self.assertIn("highest_signal", result)
        self.assertGreaterEqual(result["highest_signal"]["score"], 1)


if __name__ == "__main__":
    unittest.main()


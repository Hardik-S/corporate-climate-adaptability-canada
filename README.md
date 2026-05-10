# Corporate Climate Adaptability in Canada

Public-safe research methodology package for a resume-backed sustainability and data-analysis project. This first pass uses synthetic excerpts so the repository can demonstrate workflow, sentiment scoring, and source review without publishing private notes or unverified claims.

## Recruiter Proof Point

This repository currently includes:

- `index.html` and `styles.css` for a Vercel-ready methodology page.
- `data/synthetic_disclosures.csv` with sample disclosure excerpts.
- `src/sentiment_summary.py` for transparent keyword-based scoring.
- `tests/test_sentiment_summary.py` for deterministic verification.
- `docs/methodology.md` documenting assumptions and rejected approaches.

## Publication Boundaries

The sample data is synthetic. It is not a ranking of Canadian companies, not investment research, and not a claim about any specific issuer. Future work can add public filings only after source links, extraction dates, and quote permissions are documented.

## Quick Start

```powershell
python -m unittest discover -s tests
python src\sentiment_summary.py data\synthetic_disclosures.csv
```

The static page can be opened directly or deployed with Vercel.


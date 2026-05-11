# Methodology Notes

## Scope

This repository demonstrates a public-safe version of a corporate climate adaptability research workflow. The first proof point focuses on structure, not empirical claims.

## Source Review Plan

Future public-source expansion should record:

- issuer name
- filing or report title
- publication date
- retrieval date
- URL
- excerpt length and quote permission notes
- whether the source describes adaptation action, risk disclosure, governance, or financing

The current synthetic fixture now carries `source_type`, `retrieval_date`, and `quote_permission` fields. The analyzer reports how many rows are complete against those required fields so source hygiene is visible before any scoring output is treated as public research evidence.

## Approaches Considered And Rejected

- Publishing private research notes was rejected because the public repo should be independently reviewable.
- Scraping current issuer reports was deferred because source permissions and timestamps must be tracked carefully.
- Using a black-box sentiment library was rejected for the first pass because a transparent keyword scorer is easier to audit.

## Scoring Interpretation

The current script assigns a small positive score when an excerpt contains adaptation-action terms such as `approved`, `piloted`, `mapping`, or `planning`. It assigns a lower score when language indicates unresolved review or deferral. This is a smoke-testable proxy, not a research conclusion.

The summary also reports unique sector coverage. That field is a fixture-quality check, not a claim that the sample represents the Canadian market. It helps future reviewers see when public filings need broader sector balance before conclusions are drafted.

Source-review readiness is likewise a process control, not a conclusion. A row can be source-ready and still excluded later if the public filing is stale, quote permissions are unclear, or the excerpt does not support the claim being drafted.


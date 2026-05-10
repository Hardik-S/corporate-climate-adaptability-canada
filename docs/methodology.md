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

## Approaches Considered And Rejected

- Publishing private research notes was rejected because the public repo should be independently reviewable.
- Scraping current issuer reports was deferred because source permissions and timestamps must be tracked carefully.
- Using a black-box sentiment library was rejected for the first pass because a transparent keyword scorer is easier to audit.

## Scoring Interpretation

The current script assigns a small positive score when an excerpt contains adaptation-action terms such as `approved`, `piloted`, `mapping`, or `planning`. It assigns a lower score when language indicates unresolved review or deferral. This is a smoke-testable proxy, not a research conclusion.


# Literature Cache

This folder stores the local literature and source snapshot for the current Mont Terri OGS model chapter.

Scope:

- The inventory follows `paper/references.bib`.
- DOI-backed article references are stored as PDFs in `fulltexts/`.
- Official OGS documentation references are stored as HTML snapshots in `web_docs/`.
- Local project/audit references cited by the paper are copied into `local_sources/`.
- No paywall bypass was used. If a publisher endpoint denied access but another public source provided the same paper, the public source is recorded in `download_manifest.md`.

Files:

- `download_manifest.md`: source, DOI/URL, local file, and acquisition status for each cited source.
- `nonavailable_dois.md`: DOI-backed references that remained unavailable after this pass.
- `citation_evidence.md`: source locations checked against the chapter claims.
- `paper_claim_audit.md`: section/table-level claim audit for the current paper.
- `fulltexts/`: downloaded or copied PDF fulltexts.
- `web_docs/`: downloaded official OGS documentation pages.
- `local_sources/`: local Markdown/XML project sources copied from the neighboring project workspace.

The cache was prepared on 3 June 2026.

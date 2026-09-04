# Log

## [2026-09-04] init | Mangrove Carbon Credit LLM Wiki
- Instantiated persistent LLM wiki from user-provided LLM Wiki pattern.
- Set Premium T-VER / T-VER-P-METH-13-02 v01 as default methodology.
- Added version preflight because TGO 2026 work plan lists methodology/tool revisions.
- Added core formulas, carbon pools, SOC default, uncertainty deduction, field/remote-sensing MRV rules, non-permanence/buffer separation.
- Added project data templates, source registry, core arithmetic tool and wiki lint.
- Project-specific data not yet ingested.

## [2026-09-04] persistence | Canonical GitHub repository
- Canonical durable repository set to `saratchai1/carbon-credit-wiki-llm`.
- `main` is the durable source of truth for current Wiki state.
- Future relevant project information should be integrated with provenance, index/source-registry maintenance, conflict tracking, and append-only log entries.
- Sandbox files and chat memory are not evidence of repository state.
- Repository is public; do not commit secrets or confidential raw material.

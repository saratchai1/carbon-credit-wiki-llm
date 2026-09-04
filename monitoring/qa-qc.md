# QA/QC

## Data QA checks

- coordinates inside project boundary
- area sum consistency
- rai ↔ hectare conversion explicit
- date ordering: t2 > t1
- duplicate plot/tree
- species valid
- allometry domain
- measurement point rule
- missing units
- fuel unit/NCV match
- SOC cohort age ≤ 20 years for default rate
- optional pools not double counted
- baseline source date prior to project
- buffer rate has evidence

## Calculation QA

Every output must include:
- equation ID
- input IDs
- units
- intermediate values
- uncertainty
- exclusions
- source IDs
- run ID

## Review flags

- `PASS`
- `WARNING`
- `FAIL`
- `NEEDS_VVB_REVIEW`
- `NEEDS_TGO_METHOD_CHECK`

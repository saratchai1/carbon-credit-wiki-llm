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

## Validation-derived QC gates — STC+VSD Standard T-VER Group 2

The 2024 VGreen KU validation raised 4 Material Misstatements, 2 Misstatements and 4 Nonconformities; the revised PDD closed them. Preserve the following as reusable project-derived QC gates:

1. **Boundary water exclusion** — remove water/channel areas that are not participating in the carbon project.
2. **Cross-source geometry consistency** — GIS boundary, PDD area, sample-plot geometry/coordinates and calculation workbook must agree.
3. **Recalculation dependency** — if boundary/area changes, recalculate baseline stock, project stock and projected reductions before accepting outputs.
4. **Tree identity mapping** — tree tag must map to the correct species.
5. **Field-supported species/allometry** — do not include a species or its equation merely because it appears in a template/earlier revision; field evidence must support it. An earlier Casuarina/สนทะเล treatment was challenged when field inspection did not find that species.
6. **Species/growth-form description** — botanical/field descriptions must match observed evidence.
7. **Monitoring-parameter alignment** — parameters and frequencies in PDD/MR must match the methodology/tool actually selected.

These checks do not replace current official methodology requirements.

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

For registered-project reproductions also preserve:
- official reported value;
- workbook-exact value;
- rounding/reporting convention if known;
- project-specific methodology lock.

## Review flags

- `PASS`
- `WARNING`
- `FAIL`
- `NEEDS_VVB_REVIEW`
- `NEEDS_TGO_METHOD_CHECK`

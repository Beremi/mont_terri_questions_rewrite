# Question Note Quality Audit

Date: 2026-06-06.

Scope:

- `mont_terri_questions_reorganized.md`
- `docs/question_traceability_audit.md`
- `paper/resources/tables/question_answers.tex`
- `paper/resources/tables/measurement_questions.tex`

## Style And Structure

The Markdown inventory follows the local style signature for a question note:
formal applied-science wording, questions grouped by modelling function, definitions
before derived uses, and explicit OGS roles for inputs, boundary and initial
conditions, material fields, outputs, observation operators, diagnostics, priors,
and gates.  The current structure is retained because it follows the required order:
OGS equations, input parameters, boundary and initial conditions, outputs, material
fields, measurement streams, and activation gates.

The inventory contains 158 substantive question bullets.  A duplicate scan using
normalised question text found no exact duplicates and no near-duplicate pairs above
the selected similarity threshold.  The repeated stream metadata pattern is
intentional: each measurement stream must still state meaning, position, time,
measured quantity, units/reference convention, OGS tie, and uncertainty/use.

## Classification Check

The traceability audit has 158 rows, one for each source question bullet.  Current
status counts are:

| Status | Count | Interpretation |
| --- | ---: | --- |
| `answered` | 42 | The paper gives a factual answer supported by OGS XML/source files, generated reductions, published papers, official documentation, email resources, or paper tables. |
| `policy` | 23 | The paper records a modelling or inversion decision rather than a measured fact. |
| `diagnostic` | 18 | The paper allows plotting or comparison, but not hard likelihood weighting. |
| `gate` | 65 | The paper gives the current best answer and names the missing source, convention, or decision. |
| `blocked` | 10 | Residual use is impossible with the available exports or metadata. |

The paper answer tables use a finer local vocabulary:

- `question_answers.tex`: Established, Checked input, Fixed context, Release policy, Gate, and Caveat.
- `measurement_questions.tex`: Ready, Diagnostic, Policy, Gate, and Blocked.

This is consistent with the traceability statuses.  `Established`, `Checked input`,
and `Fixed context` map to `answered`; `Release policy` maps to `policy`; `Caveat`
maps to `gate` unless the caveat is only contextual; `Ready` maps to `answered`;
`Diagnostic`, `Policy`, `Gate`, and `Blocked` map directly.

## Source And Reference Check

All traceability rows point to existing paper labels.  The current check found
489 `\ref{...}` occurrences in `docs/question_traceability_audit.md`, with 41
unique labels and no missing labels in the current paper sources.

The paper-facing question tables were revised to avoid treating internal folders as
scientific evidence.  They now describe generated reductions as processing products
of the source files, while evidence is bounded by OGS XML/source files, original
email or TeamBeam filenames, published papers, official OGS documentation, or
explicitly stated gates.

## Relevance And Compactness Decision

No substantive questions were merged in this pass.  Merging would reduce traceability
without improving the technical message, because the apparent repetitions are
stream-specific metadata requirements rather than duplicate questions.  The wording
was compacted where needed by replacing stale `audit` or `local` phrasing with
`check`, `source record`, `provided export`, or `generated reduction`.

## Remaining Gated Topics

The remaining open items are not style defects.  They are correctly classified as
gates, diagnostics, or blocked streams:

- pressure-boundary implementation and open-niche curve provenance;
- prestress magnitude, orientation, sign convention, and excavation reference state;
- initial pressure evidence near model start;
- NMR free-water versus bound/interlayer-water residual policy;
- ERT transform, coordinate support, electrical anisotropy, and covariance;
- Taupe/TDR unit, calibration, baseline, and grouped uncertainty;
- RH sensor selection, Kelvin constants, filtering, extrapolation, and boundary
  uncertainty;
- direct-pressure, Geoscope, laser, levelling, extensometer, crackmeter, and
  mini-piezometer residual-ready exports;
- fault/fracture/crack projection, aperture/effect, and quantitative use.

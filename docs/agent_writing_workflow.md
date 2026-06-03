# Agent Writing Workflow

This workflow embeds the practical writing rules from `Beremi/style_guide` for this Mont Terri question repository. Use it when the external style-guide repository is unavailable or when a fast local reminder is enough.

## 1. Choose The Target Form

Choose the closest form before writing:

- Question inventory: compact, granular bullets grouped by modeling function.
- Scientific report section: motivation, definitions, model relation, evidence, limitations.
- Manuscript-style text: motivation, state of the art, contributions, formulation, numerical evidence, conclusions.
- Long explanatory note: more background is allowed, but do not import thesis-length paragraphs into compact notes.

Default for this repository: question inventory with scientific-report discipline.

## 2. Build The Outline Before Drafting

Use the modeling role as the organizing principle:

1. OGS model: equations, input parameters, boundary and initial conditions, outputs.
2. Material fields: material meaning, dependency on other fields, OGS role.
3. Measurements: meaning, position, time, measured quantity and method, units, OGS tie, uncertainty/use.

Do not organize primarily by source-file accident or by a collaborator's shorthand if a modeling structure is clearer.

For OGS model sections, keep the current design explicit:

- The reference implementation is an OGS TRM project with displacement, liquid
  pressure, and temperature variables, but the active temperature constraints imply
  \(T=T_0=298.15\,\mathrm{K}\). State the reduced isothermal interpretation
  directly; do not imply that flow or displacement can change temperature in the
  active parametrization.
- Put parameter tables immediately under the equations that introduce the
  parameters.
- Split field inventories into unknown/output fields, material input fields, and
  intermediate or derived values.
- Use \(\Gamma_A,\Gamma_B,\Gamma_C,\Gamma_D\) for the square boundary and
  \(\Gamma_E\) for the niche. Put the boundary-condition table directly under the
  schematic and include \(\Gamma\)-symbol or union, XML tag, mechanical boundary
  data, and hydraulic boundary data.
- Preserve the boundary distinction: the mathematical reference inventory uses
  pressure Dirichlet data on all four square sides and a time-dependent pressure
  boundary on the niche, while the checked run-local XML explicitly shows pressure
  Dirichlet data only on `cd-a_top` and `cd-a_niche4`.
- Keep pressure questions separate: source of the time-dependent boundary curve,
  interpolation and date origin, absolute/gauge/capillary/suction convention,
  negative values and sign convention, initial pressure field, and consistency with
  far-field and niche states.
- Treat excavation/startup and prestress as explicit gates: clarify whether the
  model starts from a post-excavation state, instant excavation, staged excavation,
  or another transition, and how the prestress tensor and zero-Neumann excavation
  boundary are represented.

For material-field sections, apply the same mini-outline to every field:

- material meaning in Opalinus Clay or the EDZ;
- relation to other fields and whether it is base, derived, correlated, or
  computable only after assumptions;
- OGS role as XML parameter, mesh field, constitutive parameter, boundary curve,
  initial condition, output, observation operator, prior, diagnostic, or caveat;
- heterogeneity, anisotropy, uncertainty, release status, and possible time
  dependence.

Always include the important field families when relevant: intrinsic permeability,
hydraulic conductivity, porosity, storage/storativity, Biot coefficient, Bishop
factor, elastic and orthotropic parameters, bedding angle, retention, relative
permeability, swelling, thermal parameters, EDZ/fracture/fault fields, and
boundary or observation parameters. The conservative first-stage release is still
the intrinsic-permeability tensor magnitude field only.

For measurement sections, preserve the full metadata chain before discussing use:

1. meaning;
2. position and 2D support/projection;
3. time, campaign, interval, or reference date;
4. physically measured quantity and processing/calibration;
5. units and reference/sign convention;
6. OGS tie as input, boundary forcing, initial-condition constraint,
   material-field prior, output residual, observation operator, diagnostic, or
   caveat;
7. uncertainty, noise, quality flags, aggregation, and reliability.

Apply this to NMR, ERT, Taupe/TDR, RH/suction, direct pressure sensors,
fault/fracture `.dat` sources, geoscope/crackometer/visible cracks, and other
available streams. NMR and ERT must keep the free-water versus bound-water question
visible. ERT must also keep resistivity-water transform, Archie-like calibration,
electrical anisotropy, bedding, and material-property dependence visible. RH/suction
must say whether it informs boundary conditions, retention, or validation. Large
3D faults and small niche-surface cracks must remain separate topics.

## 3. Draft In The Current Style

Use formal applied-mathematics prose with moderate reader guidance.

Preferred moves:

- Start from the concrete modeling bottleneck or decision.
- Introduce definitions before asking about derived quantities.
- Use explicit technical nouns: `intrinsic permeability`, `hydraulic conductivity`, `saturation`, `retention curve`, `liquid pressure`, `observation operator`.
- Use authorial `we` when describing our modeling workflow: `we compare`, `we treat`, `we release`, `we keep fixed`.
- Keep paragraphs around 60-80 words when prose is needed.
- Keep bullets direct and self-contained.

Avoid:

- Unsupported novelty or certainty claims.
- Vague phrasing when a modeling role can be named.
- Combining several unrelated decisions in one bullet.
- Repeated `we can`; prefer `we compare`, `we use`, `we derive`, `we treat`, `we exclude`, `we keep fixed`.

## 4. Question Pattern For This Repository

For OGS model questions, use:

```text
- Which exact [equation/condition/field/output] is active, and where is it defined in the transferred model?
- What assumptions or inactive terms must be recorded so comparisons are not misinterpreted?
- How should this choice affect candidate fitting, validation, or diagnostics?
```

For material-field questions, use:

```text
- Material meaning: What physical or effective property does this field describe in Opalinus Clay?
- Relation to other fields: Can it be computed from base fields, or is it independent enough to release?
- Relation to OGS: Is it an XML parameter, mesh field, constitutive-law parameter, boundary curve, initial condition, output, or post-processing diagnostic?
```

For measurement questions, use:

```text
- Meaning: What does the stream represent before modeling interpretation?
- Position in domain: Where is it located relative to the current 2D OGS slice?
- Time of measurement: What timestamp, campaign, or interval defines the value?
- What/how measured: What instrument, inversion, calibration, or processing produced it?
- Units: What units, reference convention, and sign convention apply?
- OGS tie: Is it an input, boundary forcing, initial-condition constraint, material-field prior, output residual, diagnostic, or caveat?
- Uncertainty/use: What noise, support, projection, or quality flag controls its weight?
```

## 5. Mathematical And Technical Prose Rules

When writing LaTeX or manuscript text, follow the style-guide habits:

- Use `Let ... be`, `Let ... denote`, `We assume`, and `We define`.
- Treat displayed equations as parts of sentences and punctuate them.
- Use `$...$` for inline math.
- Use `\eqref{...}` for equations.
- Use `Section~\ref{...}`, `Figure~\ref{...}`, and `Table~\ref{...}` for non-equation references.
- Use prefixed labels such as `eq:`, `sec:`, `fig:`, and `tab:`.
- Prefer `:=` for local definitions.
- Interpret numerical results in body text, not only in captions.

For Markdown-only notes, preserve the same logic without forcing LaTeX conventions where they are not needed.

## 6. Revision Passes

Run these passes before finalizing a text change:

1. Structure: Does the section order follow the modeling role?
2. Meaning: Are definitions and assumptions visible before dependent questions?
3. Granularity: Does each bullet ask one question or one tightly coupled decision?
4. OGS tie: Is each line connected to input, output, material field, boundary/initial condition, observation operator, prior, diagnostic, or caveat?
5. Measurement metadata: For each stream, are position, time, measured quantity, units, and uncertainty addressed?
6. Voice: Is the text formal, precise, and evidence-aware without overclaiming?
7. Consistency: Are terms such as pressure, suction, saturation, water content, permeability, and hydraulic conductivity used consistently?

## 7. Final Output Contract

Final text should read as formal applied-science exposition. It should give the reader a clear technical route, preserve granular modeling decisions, and make each uncertainty actionable as a collaborator query, data requirement, or modeling gate.

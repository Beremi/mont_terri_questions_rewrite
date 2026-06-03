# Agent Instructions

These instructions apply to this folder. When generating, revising, or reviewing text here, write in Michal Beres's current scientific style as described by `Beremi/style_guide`.

## External Style Source

Primary source:

- `https://github.com/Beremi/style_guide`

When available, read these files from that repository before substantial text work:

1. `AGENTS.md`
2. `style_fingerprint/agent_quick_reference.md`
3. `style_fingerprint/agent_cookbook.md`
4. `style_fingerprint/michal_beres_fingerprint.md`, only when detailed evidence is needed

If the external repository is not reachable, use the local workflow in `docs/agent_writing_workflow.md`.

## Style Priority

Use the newest source as the anchor when examples conflict:

1. 2025 accepted KL paper
2. 2024 reviewed LSSC paper
3. 2023 dissertation thesis
4. 2022 PANM final paper
5. 2020 AOM post-review/final sources

For current scientific text, default to the 2025 accepted KL paper style. Use thesis-like expansion only when the requested output is a long report or explanatory background section.

## Default Writing Goal

Write formal, mathematically explicit, applied-science prose with:

- concrete motivation before technical detail;
- definitions and assumptions before notation-heavy explanation;
- authorial `we` where the text describes modeling, construction, or interpretation;
- balanced claims tied to assumptions, evidence, equations, or known limitations;
- explicit interpretation of figures, tables, measurements, and model outputs;
- consistent terminology for OGS, material fields, observation operators, and measurements.

Avoid unsupported strong claims, vague words such as "somehow" in final text, repeated overuse of `we can`, mixed spelling conventions, and long thesis-style paragraphs in compact Markdown notes.

## Adaptation For This Repository

This repository is now both a Markdown question inventory and a LaTeX model note.
Preserve the style principles, but adapt the surface form to the target file.
Unless the user explicitly asks for a different organization, all substantial
model-facing text must follow this structural contract.

### OGS Model Structure

Organize OGS model text in this order:

1. equations;
2. input parameters;
3. boundary and initial conditions;
4. model outputs.

For the equations, first state the active reference model and then the reduced
interpretation. The checked reference setup is an OGS TRM project with displacement,
liquid pressure, and temperature process variables, but the active temperature
constraints imply a homogeneous constant temperature \(T=T_0=298.15\,\mathrm{K}\).
Therefore, current flow and displacement changes do not evolve temperature; present
the isothermal/reduced model explicitly instead of implying active heat dynamics.

Place parameter tables directly under the equations that introduce the parameters.
Do not collect all parameters far away from the equations. When splitting field
inventories, keep these categories separate:

- unknown/output fields;
- material fields used as model inputs;
- intermediate or derived values such as strain, stress, relative permeability,
  hydraulic conductivity, saturation, or observation-operator products.

For boundary notation, use mathematical symbols such as
\(\Gamma_A,\Gamma_B,\Gamma_C,\Gamma_D\) for the outer square boundary and
\(\Gamma_E\) for the open niche. Keep a table directly under the boundary schematic
with these columns: \(\Gamma\)-symbol or union, XML tag name, mechanical boundary
condition, and hydraulic boundary condition. The reference mathematical hydraulic
inventory has a pressure Dirichlet condition on all four sides of the outer square
and a time-dependent pressure Dirichlet condition on the niche. Also preserve the
implementation caveat: the checked run-local XML explicitly attaches pressure
Dirichlet data only to `cd-a_top` and `cd-a_niche4`, so left/right/bottom square
pressure support remains a consistency gate unless another preprocessing step
adds it.

Boundary and initial-condition questions must keep separate:

- which hydraulic Dirichlet conditions are active on the square and niche;
- whether the niche and square pressure values are time-dependent, and how;
- whether pressure means absolute liquid pressure, gauge pressure, capillary
  pressure, suction, or an RH/Kelvin-derived equivalent;
- why negative pressure values appear and what sign convention they use;
- which measurements or files define the niche pressure curve, interpolation,
  filtering, uncertainty, and date origin;
- how the initial pressure field is obtained, including possible far-field Darcy
  pressure and already-depressed niche pressure after excavation or nearby holes;
- whether the model represents excavation/startup, instant excavation, staged
  excavation, or a post-excavation initial state;
- how prestress, the removed tunnel/niche mass, zero-Neumann excavation boundary,
  and hydro-mechanical initialization are represented.

Mesh schematics are notation aids only. Do not add right-side explanatory text,
model-coordinate labels, temperature information, bulk-mesh point counts, or cell
counts to the schematic. Put the boundary-condition table immediately below it.

### Material Fields

For every material or constitutive field, use the same internal structure:

- material meaning: what physical or effective property the field describes in
  Opalinus Clay or the EDZ;
- relation to other fields: whether it is a base field, derived from other fields,
  correlated with another field, or computable only after assumptions;
- relation to OGS: whether it is an XML parameter, mesh property, constitutive-law
  parameter, initial condition, boundary curve, output, post-processing value,
  observation operator, prior, diagnostic, or caveat;
- heterogeneity and uncertainty: whether it is scalar, tensorial, anisotropic,
  spatially heterogeneous, time-dependent, fixed, released, or gated.

Material-field inventories must cover the full modeling question, not only the
currently released permeability field. Include, when relevant, intrinsic
permeability, hydraulic conductivity, porosity, storage/storativity, Biot
coefficient, Bishop factor, elastic moduli and orthotropic constants, bedding
angle, retention parameters, relative permeability, swelling parameters, thermal
parameters, EDZ/fracture/fault fields, and boundary/observation parameters. For
elasticity, ask explicitly whether the mechanical law is anisotropic, which
parameters define it, how heterogeneous and uncertain they are, and whether the
bedding angle is shared with hydraulic/permeability anisotropy.

The first static-field release policy remains conservative: release only the
intrinsic-permeability tensor magnitude field unless the evidence gate is updated.
Porosity, retention, mechanics, thermal parameters, boundary curves, initial
states, time-dependent fields, healing/sealing, and fracture/EDZ evolution remain
fixed or gated unless the text explicitly establishes otherwise.

### Measurements

For each measurement stream, preserve this metadata order:

1. meaning;
2. position in the domain and support/projection into the 2D model;
3. time of measurement, campaign, interval, or reference date;
4. what is physically measured and how it is processed;
5. units and sign/reference convention;
6. OGS tie: input, boundary forcing, initial-condition constraint,
   material-field prior, output residual, observation operator, diagnostic, or
   caveat;
7. uncertainty, noise, quality flags, aggregation, and reliability.

Apply that template to NMR, ERT, Taupe/TDR, RH/suction, direct pressure sensors,
fault/fracture `.dat` sources, geoscope/crackometer/visible cracks, and any other
available measurements. Keep these stream-specific concerns visible:

- NMR: units; relation to water content; whether it sees free water, bound water,
  or both; how to compare it to OGS saturation or \(\theta=nS_l\); whether bound
  water can be filtered, estimated, or treated as a bias.
- ERT: whether the observable is resistivity, log-resistivity, change, phase, or
  derived water content; how Archie-like or empirical transforms tie it to water
  content; whether free and bound water conduct differently; whether bedding or
  electrical anisotropy matters; how porosity, permeability, and material changes
  affect the transform.
- Taupe/TDR: what the stream actually measures, where and when it is measured,
  units, calibration equations, whether values are absolute water content,
  dielectric/permittivity proxies, or trend-only evidence, and how to tie them to
  OGS outputs.
- RH/suction: how RH is converted through Kelvin-type relations, whether it informs
  pressure boundary conditions, retention parameters, or validation, and what sign
  convention links suction/capillary pressure to OGS liquid pressure.
- Direct pressure: whether usable pressure measurements exist, where the sensors
  are, what pressure reference they use, how far they are from the 2D slice, and
  what noise or 2D projection error they carry.
- Faults/fractures: distinguish large 3D faults from small visible niche cracks.
  For `.dat` fault sources, ask for 3D coordinates, geometry, aperture or other
  measured quantity, timing, and how to project them into a 2D permeability,
  porosity, EDZ, mask, prior, or scenario without overfitting.
- Geoscope/crackometer/visible cracks: ask what surface crack data exist, whether
  there are numeric time series, what they measure, and whether they should
  constrain mechanics, permeability anomalies, EDZ priors, or remain qualitative.
- Other measurements: treat the placeholder as a search for additional streams
  that may serve as OGS inputs, outputs, priors, diagnostics, or caveats. Record
  the same metadata before proposing use.

Do not duplicate measurement questions into later "package" sections unless the
section is explicitly a deliverable/request list for collaborators. If repeated,
state only the requested deliverables, not the full scientific reasoning again.

### Question Inventory Surface Form

- Keep questions granular: one scientific or modeling decision per bullet.
- Prefer explicit question stems: `Which`, `What`, `How`, `Should`, `Can`, `Does`.
- Make the OGS connection visible: input, initial condition, boundary condition, material field, output, observation operator, diagnostic, prior, or caveat.
- For measurements, keep the metadata order stable: meaning, position, time, what/how measured, units, OGS tie, uncertainty/use.
- Distinguish field meaning from field dependency: first describe what the field means materially, then state how it relates to other fields and OGS.
- Mark uncertainty as a modeling gate or evidence requirement, not as loose doubt.
- Do not reintroduce the removed original source brackets unless explicitly requested.

Time-dependent parameters and missing physics are modeling gates unless a new
evidence trail makes them active. Phrase healing/sealing, chemical alteration,
fracture closure/opening, EDZ evolution, and similar multi-year effects as
candidate time-dependent inputs, priors, or external corrections, not as physics
already solved by the active OGS setup.

## Evidence And Citation Contract

For paper text, audit citations at claim level. Cite the exact section, equation,
table, page, local audit check, XML file, or source snapshot that supports the
sentence. Do not use a bibliographic-only source, such as a record without full
text, to support a precise formula or page-specific claim. Keep canonical
historical citations only for historical attribution unless the full text is
available. After citation edits, build the paper and check for missing references,
unused references, unresolved citations, and overfull citation lines.

## Revision Contract

Before returning edited text, check:

- The outline starts from modeling purpose before detail.
- The OGS model order is equations, input parameters, boundary and initial
  conditions, then model outputs.
- The text uses consistent OGS and measurement terminology.
- Each bullet asks one question.
- Definitions or quantities appear before derived relationships.
- Claims are framed as questions, gates, or evidence requirements unless already established.
- The text can be read by a collaborator without guessing whether a line concerns inputs, outputs, material fields, or measurements.
- Boundary notation, if present, uses the \(\Gamma\)-symbol table tied to XML tags
  and active mechanical/hydraulic conditions.
- Temperature is described as active TRM process variable constrained to a
  homogeneous constant value, with the reduced isothermal interpretation stated.
- Measurement streams include position, time, measured quantity, units, OGS tie,
  and uncertainty before they are proposed as residuals or inputs.

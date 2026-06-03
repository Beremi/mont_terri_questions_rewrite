# Text Requirements

This checklist records the requirements used for the current rewrite of the Mont
Terri CD-A Niche 4 model note.

## Scope and Source Handling

- Translate and rewrite the Czech draft notes into clear English; do not keep the
  original bracketed Czech text in the final paper version.
- Preserve the draft intent that several short notes often meant several separate
  questions; keep the final structure granular rather than collapsing them into one
  broad question.
- Base proposed answers on the repository evidence in the root folder and record
  uncertainty as a gate when the evidence is incomplete.
- Reorganize the material by modelling role rather than by the accident of the
  original tables: OGS model, material or constitutive fields, measurements, and
  unresolved gates.
- For this paper pass, restrict the proposed question/answer rows to model boundary
  conditions, initial conditions, OGS inputs, OGS outputs, and material or
  constitutive field descriptions.  Measurement-package questions belong to a later
  measurement chapter unless they define an observation-operator gate for a model
  output.

## Document Form

- Use A4 paper with 1.5 cm margins.
- Follow the local writing workflow derived from `Beremi/style_guide`: formal
  applied-science prose, concrete motivation, definitions before notation-heavy
  claims, and explicit evidence-aware limitations.
- Write compact scientific paragraphs; avoid loose phrasing, unsupported certainty,
  and broad claims that are not tied to equations, XML evidence, audits, or gates.
- Use authorial `we` only where it describes our modelling workflow, release policy,
  comparison rule, or interpretation.

## Model Exposition

- Separate the scientific mathematical model from the OGS implementation layer.
- Introduce the rock setting before the equations: Opalinus Clay, bedding,
  excavation damaged zone, hydraulic desaturation, suction, swelling, and
  hydro-mechanical coupling.
- State only the physics represented by the current reference TRM setup; keep
  vapor diffusion, discrete fractures, chemical effects, healing/sealing kinetics,
  staged excavation, and full 3D fault geometry as external gates or scenarios.
- Define variables before equations, and place parameter tables directly under the
  equations that introduce them.
- Keep the model faithful to the reference OGS setup: TRM with displacement,
  liquid pressure, temperature, van Genuchten retention and relative permeability,
  orthotropic elasticity, Biot/Bishop coupling, saturation-dependent swelling,
  zero body force, homogeneous constant active temperature, and run-local mesh
  fields for permeability and porosity.
- State the isothermal reduction explicitly: the OGS project is still TRM, but the
  active temperature data imply \(T=T_0=298.15\,\mathrm{K}\), so flow and
  displacement do not evolve temperature in the active parametrization.
- Make the boundary notation explicit with \(\Gamma_A,\Gamma_B,\Gamma_C,\Gamma_D\)
  for the square boundary and \(\Gamma_E\) for the open niche.
- State the intended hydraulic boundary inventory clearly: constant square pressure
  \(p_\square=1.5\,\mathrm{MPa}\) on all four outer sides and time-dependent niche
  pressure \(p_E(t)\) on the open-niche boundary.
- Preserve the implementation caveat that the checked run-local XML explicitly
  attaches pressure Dirichlet data only to `cd-a_top` and `cd-a_niche4`; attaching
  the left/right/bottom square pressure is therefore a reference-setup consistency
  gate unless another preprocessing step does it.
- Keep the mesh schematic as notation only: no right-side explanatory text, no
  model-coordinate label, and no temperature, bulk-mesh, point, or cell counts in
  the figure.
- Put the boundary-condition table immediately under the mesh schematic.  The table
  must map \(\Gamma\)-symbols or unions to XML tags, mechanical boundary data, and
  hydraulic boundary data.

## Questions and Proposed Answers

- Keep questions granular: one model question or decision per row.
- Use stable organization levels: boundary and initial conditions, OGS inputs,
  model outputs, material or constitutive fields, and implementation gates.
- For each proposed answer, distinguish established repo evidence from gates or
  external decisions.
- Ask specifically whether a field is a base input, derived state, OGS output,
  observation-operator product, prior, diagnostic, or inactive XML/provenance entry.
- For fields, always state material meaning, relation to other fields, and OGS role.
- Preserve the current release policy: first-stage fitting releases only the
  intrinsic-permeability tensor magnitude field; porosity, retention, mechanics,
  thermal parameters, boundary curves, initial state, and time-dependent fields stay
  fixed or gated.

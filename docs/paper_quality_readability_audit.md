# Paper Quality and Readability Audit

Date: 2026-06-04.

Scope: `paper/sections/chapter_01_ogs_model.tex`,
`paper/sections/chapter_02_measurements.tex`, and
`paper/resources/tables/*.tex`.  Evidence was checked against the local citation
and claim audits, the local OGS/XML source copies, and the generated measurement
stream audits.  Raw data and provenance files were not edited.

## Style And Structure Check

| Area | Audit result | Action |
|---|---|---|
| Chapter 1 order | The chapter follows the intended order: evidence boundary, physical setting, unknowns, equations, boundary/initial data, OGS realization, inputs, outputs, and gates. | Kept. |
| Boundary notation | `\Gamma_A`--`\Gamma_D`, `\Gamma_\square`, and `\Gamma_E` are introduced in the mathematical boundary subsection before the mesh schematic and boundary tables use them. | Kept. |
| Chapter 2 measurement style | Measurement sections keep the paired meaning/position/time/value/uncertainty/use/grounding-question structure. | Kept. |
| Gate wording | Unsupported items are stated as gates, diagnostics, policy choices, or blocked streams rather than closed facts. | Kept. |
| Raw-data provenance | Figures and source-slide statements remain described as diagnostics or source evidence, not residual-ready exports. | Kept. |

## Symbol And Definition Check

| Symbol group | Issue found | Resolution |
|---|---|---|
| Liquid properties | `\rho_l` appeared in Darcy and mass equations while the initial table only named `\rho_l^0`. | The table now defines `\rho_l(\TT,\pl)`, `\rho_l^0(\pl)`, and `\mu_l`; the Darcy prose defines density, viscosity, mass flux, and intrinsic permeability before the equation. |
| Retention variables | `S_e`, residual saturations, `m`, `p_b`, and `k_{\min}` were introduced mostly by equations. | The retention prose now defines them before the displayed laws, and the parameter table gives active values. |
| Mass-balance variables | `\beta_l`, `\alpha_T^s`, `Q_H`, and overdot notation needed explicit first-use descriptions. | The mass-balance prose now defines them before the equation; the mass table now records `\beta_l` and the CTE caveat for `\alpha_T^s`. |
| Thermal strain | `\eps^T` could be read as transpose. | Replaced by `\eps^{\mathrm{th}}` and defined in the derived-quantity table. |
| Mechanics body force | `\bm f` appeared in the momentum equation before local description. | The mechanics prose now identifies it as the body-force term and the table retains the zero active value. |
| Heat-balance terms | Effective heat storage, effective conductivity, liquid heat capacity, and `Q_T` were compactly introduced by the equation. | The heat-balance prose now introduces these terms before the display. |
| Permeability operator | `\mathcal C_i`, `w_{ic}`, `\mathbf e_i`, and `\KK_c` were implicit. | The direct-permeability section now defines each term immediately after the display. |
| NMR observation model | Bound-water and error terms were implicit. | The NMR section now defines `\theta_{\mathrm{bound}}` and `\epsilon_{\mathrm{NMR}}`. |
| ERT operator | `\rho_{\Omega\mathrm{m}}` and `\mathcal O_{\mathrm{ERT}}` were implicit. | The ERT section now defines resistivity units and the projection/aggregation operator. |
| Taupe/TDR trend symbol | `T_{\mathrm{Taupe}}` could be confused with OGS temperature. | The Taupe/TDR section now states that it is the source series value, not `\TT`. |
| RH Kelvin constants | `R` and `M_w` were not described. | The RH section now identifies them as the molar gas constant and water molar mass used by the local conversion. |
| Crackmeter normal | `\mathbf n` was used while the paper macro is `\nn`. | Chapter 2 and the measurement-question table now use `\nn` and define it as the local crack-normal or instrument-axis direction. |

## Citation Check

| Check | Result |
|---|---|
| Cited keys present in bibliography | Passed: 102 citation occurrences, 35 unique cited keys, and no missing `references.bib` keys. |
| Citation placement | Claims in Chapters 1 and 2 map to `literature/citation_evidence.md` and `literature/paper_claim_audit.md`. Local OGS values cite local XML/audits; external papers support general formulation or measurement-method claims. |
| Bibliographic-only sources | `Bishop1959EffectiveStress` remains limited to historical naming; OGS/local sources support the active equation and parameter substitution. |
| Unused bibliography entries | `CDAModellingSlides2025`, `Kleinberg1996NMR`, and `Topp1980TDR` are not cited by the current paper. The citation-evidence audit already records that the NMR/TDR entries are not used for fulltext-specific claims. |

## Remaining Gated Questions

The following are correctly presented as gates rather than paper defects:

- pressure-boundary implementation/provenance for left, right, and bottom square
  boundary attachment versus generated-project preprocessing;
- active open-niche pressure-curve provenance, sensor selection, filtering,
  time-origin, and uncertainty;
- CTE value and unit provenance;
- prestress, excavation unloading, and mechanical reference-state policy;
- initial pressure state versus post-excavation drainage evidence;
- NMR bound/mobile-water split and absolute-offset policy;
- ERT coordinate transform, near-niche support, covariance, and clay/surface
  conduction calibration;
- Taupe/TDR units and CD-A-specific calibration;
- direct-pressure numeric export, support, unit/reference convention, and quality
  flags;
- fault/fracture 3D-to-2D projection, aperture or hydraulic-effect policy, and
  whether structural evidence is a hard input, prior, or scenario;
- other HM stream exports, supports, reference zeros, sign conventions, and
  uncertainties.

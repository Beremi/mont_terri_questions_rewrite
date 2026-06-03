# Citation Evidence Audit

This audit records the source locations checked for the current model chapter. It is not a bibliography replacement. It is a claim-support ledger for the paper text and tables.

Date: 3 June 2026.

## Fulltext Sources

| Key | Exact checked part | Supported use in the chapter | Audit decision |
|---|---|---|---|
| `Wang2009THM` | Sections 2.1-2.3, especially Eq. 1 for Darcy flow, Eq. 7 for momentum balance, and Eqs. 8-9 for heat transport. | General coupled THM notation and the use of pressure, temperature, and displacement as coupled field variables. | Kept as a background/formulation citation only. The exact active OGS equations are cited to the OGS TRM documentation and local XML audits. |
| `VanGenuchten1980` | Page 892, Eqs. 2-3 for dimensionless/effective water content and the retention relation; page 893, Eq. 8 for the Mualem-based closed-form relative hydraulic conductivity. The PDF is image-only, so these locations were checked from rendered page images. | Retention and relative-permeability equations in the Darcy/retention subsection. | Citation made precise to page and equation numbers. |
| `Mualem1976` | Page 513, abstract and Eqs. 1-2; pages 514-515, especially Eq. 14 and the suggested Eq. 21 form with the empirical exponent. | The Mualem side of the Mualem-van Genuchten relative-permeability closure. | Citation made precise. The chapter avoids implying that Mualem alone defines the exact OGS van Genuchten closed form. |
| `Ziefle2021CDA` | Abstract, pages 79-80, on CD-A as a two-niche Mont Terri experiment studying hydraulic-mechanical effects, climatic conditions, deformation, water content, and pore pressure. | Physical-setting paragraph for CD-A motivation and multidisciplinary measurements. | Kept as introductory CD-A source; detailed model and measurement claims are supported by later CD-A papers. |
| `Ziefle2024Characterization` | Abstract; Section 2; Table 1. These parts describe CD-A twin niches, upper sandy facies, fault zones, open/closed humidity conditions, and measurement streams including ERT, Taupe/TDR, NMR, mini-piezometer, psychrometer, suction, and deformation methods. | Physical setting, measurement-program context, and claims about water content, pressure, deformation, fault zones, and EDZ/permeability measurements. | Citation made precise to abstract, Section 2, and Table 1. |
| `WaterContentEDZ2024` | Abstract; Sections 1-2 for CD-A water-content evolution and measurement program; Section 3 for the 2D OGS HM model, Richards assumption, constant gas pressure, negative pore pressure/capillary pressure convention, van Genuchten equation, RH-to-pressure Kelvin equation, and Eq. 3 for theta = n S_w; Section 4.1 for ERT support and water-content interpretation. | Water-content evolution, OGS/Richards sign convention, RH-derived boundary-pressure interpretation, and theta = nS_l model-side proxy. | Citation made precise. Current numerical values still come from local XML/audits, not from this paper's earlier model version. |
| `Amann2017Opalinus` | Abstract; Section 2 for bedding and tectonic structures; Section 3.2 for suction effects on strength, stiffness, and desiccation; Section 3.3 for pore-pressure response in CU/CD tests. | General Opalinus Clay geomechanical context: suction, bedding, pore pressure, faults, and EDZ development. | Citation made precise. The chapter uses this as context, not as a source for the active OGS parameter values. |
| `Marschall2017EDZ` | Abstract; Section 1 for EDZ as transport path and simplified safety abstractions; Sections 2.1-2.5 for EDZ evolution phases, ventilation/desiccation, fault/fracture controls, hydraulic characterization, several-orders permeability increase, and self-sealing/fracture closure. | EDZ claims about release paths, hydraulic significance, evolution, swelling/closure/self-sealing, and simplified representation needs. | Citation made precise. |
| `Hale2021EDZ` | Abstract; Introduction; Section 2.1 for study site and EDZ/fracture setting; Section 3.1.1 for measured hydraulic aperture, open fractures, self-sealing under saturated/backfilled conditions, and suppression of self-sealing under open ventilated conditions. | EDZ aperture/permeability and open-condition evolution claims. | Citation made precise. |

## Web Documentation Sources

| Key | Exact checked part | Supported use in the chapter | Audit decision |
|---|---|---|---|
| `OpenGeoSysTRMDocs` | Heading "Governing equations without vapor diffusion"; displayed heat, mass, Darcy, momentum, Hooke-law, and process-variable sections. | Active mathematical equation structure, process variables, no-vapor TRM formulation, Darcy velocity, capillary-pressure sign convention, Bishop term, heat storage, and temperature role. | Used for equation-level citations. |
| `OpenGeoSysParametersDocs` | Sections "CurveScaled", "Function", and "MeshElement and MeshNode". | Claims about how OGS parameters can be constants, functions, curve-scaled data, or mesh fields. | Used for OGS parameter-realization statements. |
| `OpenGeoSysProcessVariablesDocs` | Initial-condition and boundary-condition sections; Dirichlet and Neumann explanation. | Claims about how OGS attaches initial and boundary data to process variables. | Used only for generic OGS process-variable structure; active CD-A values are cited to local audits. |

## Local Source Sources

| Key | Exact checked part | Supported use in the chapter | Audit decision |
|---|---|---|---|
| `GesaProjectionModel2025` | Copied `.prj`, process-variable XML, parameter XML, media XML, curve XML, and time-loop XML under `literature/local_sources/GesaProjectionModel2025/`. | Active file-level OGS model realization. | Used as provenance and checked through the audits below. |
| `ModelAudit2026` | Sections "Source Copies", "Provenance", and "Active Model Features Read From XML". | Source-package provenance, active model feature inventory, time-loop provenance, and fixed-context caveats. | Used for model-provenance claims. |
| `FormulationAudit2026` | Summary and Checks table, especially `process_type_and_primary_variables`, `process_variable_orders_and_bcs`, `gravity_specific_body_force_off`, `liquid_density_linear_temperature_pressure`, `vapor_terms_absent_from_active_phase`, `saturation_van_genuchten_retention`, `relative_permeability_van_genuchten`, `bishop_power_law_saturation`, `linear_elastic_orthotropic`, `swelling_stress_active`, `thermal_conductivity_effective_porosity_mixing`, `biot_coefficient_one`, `intrinsic_permeability_source_constant_run_mesh_field`, `porosity_run_mesh_field_fixed_support`, `cte_value_tracked_provenance_caveat`, `run_local_output_variables_for_observation_operators`, and `active_boundary_conditions_and_inactive_defined_parameters`. | Active equations, XML parameter values, boundary attachments, inactive parameters, output arrays, and release/fixed-context interpretation. | This is the main local evidence source for active-model claims. |
| `RunInputAudit2026` | Checks table and mesh table. | Mesh-field availability, required output variables, boundary/support mesh presence, and OGS execution acceptance. | Used for run-input and mesh-support claims. |
| `ReleaseGateAudit2026` | Opening release policy and run summary. | Claim that only `k_i_rd` varies in the first workflow, while porosity, retention, mechanics, thermal properties, boundary, and initialization remain fixed or gated. | Used for release-policy statements. |
| `QuestionInventory2026` | Sections 1-3. | Source of granular modelling, material-field, and measurement questions. | Used only to explain where the question inventory comes from, not as independent physical evidence. |
| `Bishop1959EffectiveStress` | Stable bibliographic record at `https://cir.nii.ac.jp/crid/1570854174118446592`; no fulltext found. | Historical citation for the unsaturated effective-stress principle. | Citation is bibliographically unambiguous, but no unsupported fulltext-specific claim is made. OGS implementation details are cited to OGS docs and local audit instead. |

## Claim Corrections And Boundaries

- The CD-A literature supports the general HM setting, measurement program, and earlier 2D OGS/Richards modelling choices. The active numerical values in this repo are not copied from the papers; they are cited to the local XML and audits.
- The negative pressure interpretation is supported by `WaterContentEDZ2024`, Section 3, where constant gas pressure and negative pore pressure/capillary pressure are described, and by the OGS TRM formulation.
- The Mualem-van Genuchten closure is supported by both `VanGenuchten1980` and `Mualem1976`. The exact equation in the chapter matches the van Genuchten closed-form relative-conductivity expression with Mualem theory, not a standalone Mualem table value.
- The EDZ claim was narrowed to "can differ by orders of magnitude" and "can evolve through swelling, closure, and self-sealing"; these are supported by `Marschall2017EDZ` and `Hale2021EDZ`.
- Bishop is retained only as a historical/theoretical reference. Since the fulltext was not found, active equations and parameter substitutions are supported through OGS and local XML evidence.

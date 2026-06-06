# Reorganized Source Questions by Modelling Function
This inventory organizes the source-driven questions by how they affect the current
OGS workflow.  Its purpose is to make each collaborator query precise: which part of
OGS it touches, which material field or measurement it concerns, and what metadata
or decision is needed before using it in fitting or validation.

## 1. OGS model

### 1.1 Equations
Questions to keep separate:
- Which exact OGS process is active in the exchanged model: Thermo-Richards-Mechanics, with displacement, liquid pressure, and temperature as primary variables?
- Which equation source should be treated as authoritative for this project: OGS documentation, OGS source implementation, the report formulation check, Wang/Kosakowski/Kolditz notation, or a specific project paper?
- Which simplifications are active in this CD-A run: no vapor transport, gravity/body force off, Backward Euler, Newton solve, linear liquid density, van Genuchten saturation, van Genuchten relative permeability, Bishop b(S_l)=S_l, swelling, and orthotropic mechanics?
- Which terms are absent or inactive even if they appear in related TRM theory: vapor diffusion, hydrostatic gravity, active top mechanical load, active initial-stress/prestress parameter, and the outside pressure parameter that is defined but not attached?
- In Darcy flow, do we compare permeability through intrinsic permeability K, relative permeability k_rel(S_l), viscosity, and pressure gradient, rather than confusing this with hydraulic conductivity or saturation itself?
- Which secondary variables should be expected from OGS or derived after sampling: saturation S_l, porosity, water content theta = n*S_l, pressure, temperature, displacement, strain/stress diagnostics, Darcy velocity/flux, and observation-operator products?

### 1.2 Input parameters and parameterisation
Questions to keep separate:
- What are all real material fields or constitutive fields that could matter: intrinsic permeability, hydraulic conductivity, porosity, saturation, storativity/storage, Biot coefficient, elastic stiffness/moduli, retention/WRC parameters, relative permeability, swelling, density, viscosity, thermal properties, EDZ/fault masks, and boundary/observation parameters?
- Which of those are explicit OGS XML parameters or mesh fields in the current transferred model, and which exist only as derived quantities, observation operators, or future inversion candidates?
- Which parameters are base modelling parameters for inversion, and which must be computed from others, for example hydraulic conductivity from intrinsic permeability, viscosity, density, relative permeability, and saturation?
- Which parameter relationships must be written explicitly so dependent quantities are not calibrated independently, for example Biot relations, storage/storativity definitions, porosity-saturation-water-content relations, and stiffness-tensor versus modulus relations?
- Which field support is scientifically defensible for each candidate parameter: scalar constant, material-region value, mesh-element field, tensor field, time curve/table, observation-model parameter, or external scenario field?
- Which parameters are fixed for the current workflow, which are active/released, which are inactive/commented provenance, and which are later-stage candidates gated by measurement semantics?
- In the current repo state, should the first active field remain intrinsic permeability magnitude in the mesh-cell tensor k_i_rd, while porosity n_rd is fixed support and retention, mechanical, thermal, and boundary parameters remain gated?
- If a parameter changes between candidate runs, is it an OGS model-input field or XML replacement generated externally, not a silent change to governing equations?

### 1.3 Boundary and initial conditions
Questions to keep separate:
- What are the active boundary and initial conditions for each primary variable: displacement, liquid pressure, and temperature?
- For liquid pressure, which Dirichlet boundaries are active in the XML: top/outside support at 1.5 MPa and open-niche pressure through open_niche_seasonal?
- Is the outer/top pressure boundary constant at 1.5 MPa, or time-dependent in any active run variant?
- Is the open-niche pressure boundary time-dependent, and exactly which curve, table, source file, scaling factor, and interpolation/extrapolation rule defines it?
- If bc_pressure_outside or other outside pressure parameters exist in XML, are they active boundary conditions, inactive source parameters, reference values, or only visible in support/output files?
- Why do some niche-boundary or output pressures go negative, and are these OGS liquid-pressure values relative to gas/atmospheric reference, equivalent to positive suction/capillary pressure through p_c = -p_l, rather than negative absolute water pressure?
- What is the current source of the active niche boundary pressure curve: XML only, provider spreadsheet, RH-derived Kelvin reconstruction, fitted seasonal curve, pressure sensor data, or another processed measurement?
- Which measurements could improve or extend the niche pressure boundary: RH/T, suction/psychrometer, direct pressure or mini-piezometer data, ventilation/open-niche context, open/closed comparison, or Geoscope context?
- What uncertainty or noise should be attached to the boundary values: sensor error, RH/T conversion error, source-selection spread, time interpolation, smoothing/model-form error, active-curve provenance mismatch, and time-range extension error?
- What physical time does model time zero represent: intact rock, excavation instant, monitoring start, or already post-excavation state transferred into the 2D model?
- Is the niche/tunnel excavation represented as a staged process, or does the model start with an already-open geometry and prescribed initial fields?
- How should mechanical prestress and excavation unloading enter the model: in-situ stress tensor, support removal to zero Neumann, gradual unloading, post-excavation initialized state, or only a caveat because current initial-stress/load parameters are inactive?
- For hydraulic initial state, should the initial pressure be uniform 1.5 MPa, a heterogeneous field, or a post-excavation field already drained near the niche by previous excavations and boreholes?
- Do direct pressure, hydraulic-head, mini-piezometer, RH/suction, or older pressure records exist near simulation start that can constrain the initial pressure field?
- If such initial-pressure measurements exist, how are they converted to OGS liquid pressure, including elevation correction, gauge/absolute convention, atmospheric reference, capillary/suction sign, and density/temperature assumptions?

### 1.4 Model outputs and observation operators
Questions to keep separate:
- What model outputs are produced directly by OGS, and which are derived after sampling: pressure, displacement, temperature, saturation, porosity, stress/strain, Darcy velocity or flux, water content theta = n*S_l, resistivity proxy, crack opening from displacement differences, and residual diagnostics?
- Which outputs are primary variables and which are secondary variables or post-processing products, so measurements are not compared to the wrong field?
- Which output quantity is intended for each measurement stream: intrinsic permeability for pulse tests, theta/free-water theta for NMR and Taupe/TDR, resistivity or log-resistivity for ERT, pressure for mini-piezometers, displacement/strain/opening for HM monitoring, and boundary pressure for RH/suction?
- Which observation operators are required: point sampling, borehole-line/interval averaging, support-cell averaging, mesh-to-geophysics projection, 3D-to-2D projection, band averaging, anomaly/trend operator, or support-mask filtering?
- Which outputs should be used only for diagnostics until transforms and uncertainties are accepted, especially ERT, Taupe/TDR, RH, and other HM monitoring?
- How should model-output comparisons handle time: OGS output timestep, calendar date, measurement timestamp, survey epoch, monthly ERT schedule, seasonal campaign, interpolation, extrapolation, and early numerical adjustment from inconsistent initial states?

## 2. Material fields in OGS or tied to OGS fields

### 2.1 Field inventory and dependency map
Questions to keep separate:
- For every candidate material field, what does it describe materially in Opalinus Clay, and is it a matrix property, pore-fluid property, structural/fault/EDZ property, mechanical property, retention law, or observation-model parameter?
- For every field, how does it tie to other fields in clay: can it be computed from base parameters, is it an effective property, or is it independent enough to release?
- For every field, how does it tie to OGS: XML parameter, material property law, phase property, mesh-element field, boundary curve, initial condition, output field, or post-processing diagnostic?
- Which definitions must stay separate because they are easy to conflate: intrinsic permeability, hydraulic conductivity, relative permeability, effective mobility, porosity, saturation, water content, storativity/storage, elastic modulus, stiffness tensor, Biot coefficient, and Bishop coefficient?

### 2.2 Intrinsic permeability, hydraulic conductivity, and anisotropy
Questions to keep separate:
- Material meaning: Is permeability a clay matrix/EDZ/fault/fracture property controlling intrinsic Darcy mobility, and does the current model represent it as a tensor field rather than a scalar hydraulic conductivity?
- Relation to other fields: How do intrinsic permeability, relative permeability, viscosity, density, saturation, and pressure gradient combine into hydraulic conductivity or Darcy flux?
- Relation to OGS: Which OGS input is active now: base k_i tensor, run-local mesh-element k_i_rd, fixed anisotropy ratio/orientation, or later tensor-shape release?
- Are pulse-test measurements scalar interval observations of e^T K e or a support-averaged permeability response, not direct tensor components and not hydraulic conductivity?
- What anisotropy model is defensible: fixed bedding-informed angle, global anisotropy ratio, spatially variable tensor orientation, fracture/fault/EDZ masks, or scalar magnitude field only?
- Does the same bedding angle control Darcy permeability anisotropy, ERT electrical anisotropy, and mechanical orthotropy, or are these separate modelling choices?
- Can the current repeated and conflicting pulse-test supports justify releasing local tensor shape, or should the first workflow keep tensor shape fixed and fit only magnitude?

### 2.3 Porosity, saturation, water content, and storage
Questions to keep separate:
- Material meaning: Does porosity describe total pore volume, water-accessible porosity, free-water capacity, or another effective clay porosity relevant to OGS?
- Relation to other fields: How do porosity n, saturation S_l, and volumetric water content theta = n*S_l differ, and which measurements see total water versus mobile/free water?
- Relation to OGS: Is porosity an OGS input field n_rd fixed at 0.105 in current runs, used in storage and thermal mixing, and not an active unknown until NMR/ERT/Taupe semantics are settled?
- How are storage and storativity related to porosity, fluid compressibility, Biot coefficient, saturation derivative, and mechanical coupling; are they explicit inputs or derived/effective terms?
- If observed NMR/Taupe water content exceeds fixed porosity, does that imply bound/interlayer water, calibration offset, porosity mismatch, unit issue, or an invalid comparison to OGS theta?
- Can porosity be released as a scalar or field, or would it be non-identifiable because it trades directly with saturation, NMR bound water, ERT calibration, and Taupe calibration?

### 2.4 Retention curve, relative permeability, and suction
Questions to keep separate:
- Material meaning: What retention/WRC parameters define S_l(p_c) for this clay, and what does p_c mean relative to OGS liquid pressure and atmospheric/gas reference?
- Relation to other fields: How do retention, relative permeability, porosity, saturation, suction/capillary pressure, and hydraulic mobility couple in the model?
- Relation to OGS: Which van Genuchten parameters are active and fixed now: residual liquid saturation, residual gas saturation, exponent m, air-entry pressure p_b, and minimum relative permeability?
- Is RH converted through Kelvin equation to suction/capillary pressure or OGS liquid pressure, and what constants/sign convention are used?
- Should retention parameters remain fixed until RH boundary provenance, NMR policy, ERT/Taupe transforms, and state-output residual policies are settled?
- Which parts of saturation dependence are already OGS constitutive laws and should not be double-counted as time-dependent external material change?

### 2.5 Mechanical fields, prestress, Biot coupling, and swelling
Questions to keep separate:
- Material meaning: Is the elastic part of the model orthotropic, what are the E, G, nu parameters, and how heterogeneous or uncertain are they in Opalinus Clay?
- Relation to other fields: How do elastic stiffness, Biot coefficient, Bishop function, pore pressure, saturation, swelling, and prestress couple to displacement and stress?
- Relation to OGS: Are orthotropic elasticity, Biot coefficient, Bishop b(S_l)=S_l, and saturation-dependent swelling fixed model inputs in the current workflow?
- Does the mechanical bedding angle match the permeability bedding angle, or should mechanical orthotropy, permeability anisotropy, and ERT electrical anisotropy be independent choices?
- What in-situ stress tensor and stress sign/reference convention should be used for a deep tunnel/niche model, and are initial_stress, ic_sigma0, and load_top active or only inactive provenance?
- Should excavation unloading be simulated as staged support removal, gradual zero-Neumann release, or an already post-excavation initialized stress/displacement state?
- Is there enough displacement, crack, levelling, extensometer, pressure, or laser-scan data to release mechanical parameters, or should they remain fixed/context until numeric HM residuals exist?

### 2.6 Thermal and fluid-property fields
Questions to keep separate:
- Material meaning: What do solid density, solid heat capacity, solid thermal conductivity, liquid heat capacity, liquid thermal conductivity, viscosity, and liquid density law represent in this near-isothermal hydraulic workflow?
- Relation to other fields: Which thermal/fluid fields influence hydraulic response through density, viscosity, storage, thermal mixing, or temperature coupling, and which are effectively fixed because no thermal experiment is active?
- Relation to OGS: Which of these are XML constants or phase-property laws, and which are not defensible inversion parameters now?
- Is the active CTE value physically meaningful, inactive, typo/copied heat capacity, or a provenance issue that must be confirmed before interpreting thermal-mechanical coupling?

### 2.7 Faults, fractures, EDZ, cracks, and time-dependent fields
Questions to keep separate:
- Material meaning: Are large faults, local fractures, visible niche cracks, and EDZ damage separate material/support features, and what properties could they affect: permeability, porosity, hydraulic aperture, retention, storage, anisotropy, or mechanical stiffness?
- Relation to other fields: If aperture is measured, can it be translated to permeability through hydraulic-aperture/cubic-law style relations, and what scale correction and uncertainty are required for clay/fault/EDZ conditions?
- Relation to OGS: Should faults/fractures/cracks become hard geometry inputs, structural priors, EDZ/fault material masks, permeability/porosity fields, mechanical caveats, or qualitative diagnostics?
- Which 3D-to-2D projection is defensible for large fault .dat data: intersection trace, nearest-distance influence band, projected mask, equivalent material class, or no projection if the feature misses the slice?
- Which material inputs may need time dependence over the multi-year experiment, especially EDZ permeability decreasing through clay healing/sealing, fracture closure/opening, porosity/retention changes, or boundary-curve changes?
- If OGS does not compute healing/sealing or chemical/crack evolution internally, should it be represented externally as k(x,t), n(x,t), retention(t), EDZ/fault masks by time window, or scenario-only parameter fields?
- What evidence would justify releasing time-dependent material fields: repeated same-support permeability, NMR/Taupe/ERT trend drift under fixed fields, crack-aperture time series, Geoscope/laser/levelling data, pressure-response changes, or geochemical/mineralogical sealing evidence?

## 3. Measurements

### 3.1 Metadata required for every measurement stream
Questions to keep separate:
- For each measurement, where is it taken: sensor id, coordinates, borehole/support geometry, niche side, depth/elevation, interval/band/surface, and relation to the current 2D OGS slice?
- For each measurement, when is it taken: timestamp, survey epoch, campaign date, averaging window, time zone/date convention, and relation to OGS time zero/output timesteps/boundary-curve times?
- For each measurement, what exactly does it measure before modelling interpretation, and by what physical or processing method?
- For each measurement, what are the units, reference convention, sign convention, calibration state, raw/processed status, source files, and quality flags?
- For each measurement, how does it tie to OGS: input/boundary forcing, initial-condition constraint, material-field prior, model-output residual, diagnostic screen, qualitative caveat, or coordinate/support operator?
- For each measurement, what preprocessing is required: unit conversion, coordinate transform, 3D-to-2D projection, support averaging, baseline/reference-zero definition, time interpolation, filtering, and uncertainty/correlation model?

### 3.2 Permeability pulse tests
Questions to keep separate:
- Meaning: Are pulse tests interpreted as noisy scalar interval observations of intrinsic permeability/transmissibility, not as direct tensor components, hydraulic conductivity, relative permeability, or saturation?
- Position in domain: What are the exact borehole intervals, endpoints, orientations, active mesh cells, and blocked historical endpoint geometries for BCD-A24/25/26/27, BCD-A32/A33, BFM-D19, and related rows?
- Time of measurement: Which campaign/workbook date applies to each interpreted row and raw pressure-decay row, and should repeated support rows be treated as independent, duplicates, or time evolution?
- What/how measured: What gas, pressure-decay protocol, correction, Klinkenberg/slip treatment, interval length, and interpretation method produced each permeability value?
- Units: Are values intrinsic permeability in m2, transmissibility, log10 permeability, hydraulic conductivity, or workbook-specific units, and how are zeros/missing values handled?
- OGS tie: Should each row compare to interval/support average of e^T K e from the OGS intrinsic permeability tensor field k_i_rd, with explicit support weights and uncertainty?
- Uncertainty/use: Should the likelihood remain rowwise Gaussian, robust, support-cell aggregated, capped, or duplicate-weighted, given strong same-support conflicts?

### 3.3 NMR water-content measurements
Questions to keep separate:
- Meaning: Does NMR measure total NMR-visible water, mobile/free water, bound/interlayer water, or another hydrogen/water proxy in the supplied CD-A data?
- Position in domain: Which NMR labels, profiles, borehole points, wall/profile supports, and current Niche 4 mesh supports are active or outside support?
- Time of measurement: Which rows are weekly time series and which are seasonal/campaign profiles, and how do their timestamps map to OGS output times?
- What/how measured: What NMR signal, T2 distribution, calibration, detuning caveat, campaign processing, or label/borehole conversion produces the reported water-content value?
- Units: Are values volumetric percent, fraction, raw NMR amplitude, calibrated water content, or confidence-interval reported quantity?
- OGS tie: Should comparison be to OGS saturation S_l, theta = n*S_l, corrected/free-water theta, label-bias corrected theta, or within-label trend/anomaly only?
- Bound water: How should bound/interlayer water not active in OGS saturation be filtered, modelled, estimated, held constant, or represented as bias/uncertainty?
- Uncertainty/use: What uncertainty floor and confidence-interval conversion should be used, and how should rows above fixed porosity be interpreted?

### 3.4 ERT resistivity measurements
Questions to keep separate:
- Meaning: Is the primary ERT observable resistivity, log resistivity, resistivity change, phase angle, or a derived water-content field?
- Position in domain: What coordinate transform, projection mesh, near-niche support mask, 35 cm depth/support handling, and aggregation should map ERT cells to the OGS 2D slice?
- Time of measurement: Which ERT timesteps, monthly campaigns, folders, and VTK fields correspond to OGS output times?
- What/how measured: Is the ERT field an inversion product from electrode data, local apparent resistivity, processed VTK field, or workbook-derived relation, and what correlation structure does the inversion impose?
- Units: Are values in ohm m, log10 ohm m, relative resistivity, percent change, or converted water content?
- OGS tie: Should OGS saturation or theta = n*S_l be converted to resistivity through an Archie-type, empirical CD-A-specific, NMR-calibrated, or clay-specific relation?
- Bound water and clay conduction: Does bound/locked water conduct current like free pore water, and how do clay surface conduction, salinity, porosity, pore-water conductivity, cracks/faults, and saturation history affect resistivity?
- Anisotropy: Does electrical anisotropy matter, and should it connect to bedding, fractures/faults, or permeability anisotropy?
- Uncertainty/use: What uncertainty/covariance/aggregation model prevents over-weighting dense correlated ERT cells, and should ERT remain diagnostic until transform/support/uncertainty are approved?

### 3.5 Taupe/TDR measurements
Questions to keep separate:
- Meaning: Does TAUPE mean the Taupe/TDR workbook stream in the repo, and what physical quantity does it represent?
- Position in domain: Which sensors, boreholes, EDZ bands, A3/A4/A7/A8 sheets, line supports, and 2D mesh supports are inside or outside the current model domain?
- Time of measurement: What timestamp/date convention and baseline/reference date apply to each Taupe/TDR series and anomaly/trend calculation?
- What/how measured: Are values calibrated volumetric water content, apparent relative dielectric permittivity, ARDP/TDR proxy, sensor-specific trend, or qualitative moisture signal?
- Units: What are the workbook units, calibration equations, constants, baseline normalization, and sensor/band-specific scaling rules?
- OGS tie: Should Taupe/TDR compare to absolute theta = n*S_l, saturation S_l, band-averaged theta anomaly, or grouped trend diagnostics only?
- Uncertainty/use: What uncertainty and weighting should be assigned by sensor, band, time, calibration quality, support projection, and grouping?

### 3.6 RH/suction and pressure-boundary provenance
Questions to keep separate:
- Meaning: What do RH/suction sensors measure physically, and are they measuring relative humidity, suction, capillary pressure, or a proxy for open-niche liquid-pressure boundary forcing?
- Position in domain: Which RH/suction sensors correspond to the open niche or open twin, and which should inform the niche boundary rather than interior cell residuals?
- Time of measurement: What is the RH/T timestamp convention, valid interval, high-RH caution period, low-outlier period, and relation to the active open_niche_seasonal curve time axis?
- What/how measured: How is RH converted through Kelvin equation, and what constants are assumed: temperature, density, gas constant, water molar mass/volume, RH percent/fraction convention, and gas/atmospheric reference?
- Units: Are derived quantities RH percent, suction, capillary pressure, gauge liquid pressure, absolute liquid pressure, MPa, or Pa?
- OGS tie: Is RH used to reconstruct or check a pressure boundary input, validate active forcing, inform retention parameters, or provide uncertainty on boundary scenarios?
- Curve provenance: Why does the local RH-derived envelope differ from the active seasonal pressure curve, and what source table/script/sensor-screening policy generated the active curve?
- Uncertainty/use: What uncertainty should be assigned if RH becomes a boundary or retention likelihood, and how do we avoid double-counting the same data as both forcing and validation?

### 3.7 Direct pressure or mini-piezometer measurements
Questions to keep separate:
- Meaning: Do direct pressure, hydraulic-head, pore-pressure, or mini-piezometer measurements exist, including the two more distant sensors remembered from Gesa material?
- Position in domain: Where are the sensors in coordinates, elevation, borehole/support geometry, distance from the niche, and 2D model frame?
- Time of measurement: What timestamps, campaigns, maintenance intervals, reference-zero periods, and overlap with simulation outputs exist?
- What/how measured: What pressure quantity is measured: pore pressure, hydraulic head, gauge pressure, absolute pressure, suction/capillary pressure, or a processed Geoscope value?
- Units: Are values Pa, MPa, bar, head in m, gauge pressure, absolute pressure, or relative to atmospheric/gas reference?
- OGS tie: Can these measurements compare directly to OGS liquid pressure p_l, or do they require head/elevation/gauge/reference conversion?
- Uncertainty/use: Are they reliable enough for hard residuals, or only qualitative validation because of distance, noise, sensor failures, maintenance, calibration, or 2D-model error?

### 3.8 Large fault or fault-surface .dat geometry
Questions to keep separate:
- Meaning: Does the faulty/.dat source mean large fault/fault-surface/fracture geometry rather than niche-surface crackmeter data?
- Position in domain: Which exact .dat file/source contains the 3D fault geometry, coordinate system, units, axes, trace/surface/polygon/point-cloud representation, and relation to the current Niche 4 2D slice?
- Time of measurement: Is the fault dataset static mapped geometry, excavation-time mapping, repeated survey, or time-dependent aperture/activation information?
- What/how measured: Does the source describe geometry, aperture, hydraulic aperture, mechanical aperture, fracture opening, displacement, fault-zone class, or only visualization geometry?
- Units: What units apply to coordinates and aperture/opening if present?
- OGS tie: Should the projected fault become a geometry input, structural prior, EDZ/fault material class, permeability or porosity mask, retention/storage prior, mechanical caveat, or qualitative context?
- Projection/use: What 3D-to-2D projection is accepted, and how do we avoid overfitting a 2D permeability field to unresolved 3D structures?

### 3.9 Niche-surface cracks, Geoscope, crackometer, laser scan, levelling, extensometers
Questions to keep separate:
- Meaning: What visible or measurable crack/opening/deformation data exist on the niche surface, separate from large 3D fault geometry?
- Position in domain: Where exactly are cracks/openings measured: niche wall location, trace geometry, coordinates, sensor position, open/closed niche side, gauge length, support surface, and 2D slice relation?
- Time of measurement: Are data static maps, campaign surveys, continuous Geoscope/crackometer time series, laser-scan epochs, levelling epochs, extensometer series, or reference-zero differences?
- What/how measured: Are quantities crack width, aperture, crack opening displacement, displacement jump, strain, surface displacement, laser-scan difference, convergence, levelling vertical displacement, pressure response, or qualitative crack class?
- Units: Are values mm, m, strain, Pa response, relative displacement, survey difference, or qualitative class?
- OGS tie: Should comparison use OGS displacement, strain, stress, derived crack opening from displacement difference, pressure response, swelling/deformation pattern, or only mechanical plausibility screening?
- Material-field tie: Can measured cracks/openings justify local permeability anomaly, porosity/damage zone, hydraulic aperture relation, fracture/EDZ mask, mechanical stiffness reduction, or time-dependent permeability/porosity change?
- Uncertainty/use: What numeric exports, support geometry, reference-zero/sign convention, quality flags, registration uncertainty, sensor noise, and 2D projection error are needed before hard residuals?

### 3.10 Coordinates, layout, bedding/geology, projection inputs, and other available streams
Questions to keep separate:
- Meaning: Which non-residual support layers are available and required for model use: coordinates/layout, borehole endpoints, mesh projection inputs, bedding/geology, source-to-OGS transforms, and source-file catalogues?
- Position in domain: Which coordinate rows, borehole endpoints, support points, line samples, ERT mesh cells, NMR/Taupe supports, and fault/bedding geometries are inside, outside, or near the current 2D mesh?
- Time of measurement: Which support layers are static geometry and which have campaign dates or time-dependent survey states?
- What/how measured: Are these direct measurements, digitized geometry, derived projections, source catalogues, layout/support operators, or structural priors?
- Units: What coordinate system, length unit, angle convention, bedding-angle convention, and mesh index/support unit apply?
- OGS tie: Should these streams be treated as observation-operator support, material-field priors, geometry masks, mesh-parameter inputs, or qualitative caveats rather than residuals?
- Other measurements: What additional measurement streams exist in the data beyond those listed here, and for each one what are where, when, units, measured quantity, and OGS input/output/prior/diagnostic status?
- Activation/use: Which streams are active likelihood terms now, which are diagnostic, which are boundary/input provenance, which are support/prior only, and which are blocked by missing numeric exports or metadata?

### 3.11 Current activation gates to keep visible
Questions to keep separate:
- Which direct permeability rows are active now, which are blocked by missing endpoint geometry, and which need likelihood/support policy before more same-support OGS spending?
- Is NMR active only with tracked caveats, and should the final policy be raw absolute theta, bias-corrected theta, corrected free-water theta, within-label trend/anomaly, or exclusion?
- Should ERT remain diagnostic until transform/support/uncertainty/covariance are accepted?
- Should Taupe/TDR remain diagnostic until unit/calibration/baseline/uncertainty are confirmed?
- Should RH remain boundary-check/provenance evidence until active curve generation, sensor screening, Kelvin constants, and extension policy are confirmed?
- Should other HM pressure/deformation streams remain inactive until Geoscope, laser-scan, levelling, extensometer, crackmeter, and mini-piezometer numeric exports with uncertainty are supplied?
- Should CTE and prestress remain model-provenance caveats until Gesa/BGR confirms intended values and active/inactive status?

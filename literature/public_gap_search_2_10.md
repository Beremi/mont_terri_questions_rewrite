# Public Gap Search For Section 2.10

Date: 2026-06-04

This note records the public-source pass used while expanding the granular
measurement questions in Section 2.10.  The purpose was to check whether questions
left open by the local CD-A catalogue could be answered from public sources and to
identify any new report/literature source that should be added to the paper
library.

## Search Scope

Public searches covered the unresolved stream-specific gates:

- CD-A Taupe/TDR meaning, ARDP/permittivity, and water-content calibration.
- CD-A mini-piezometer pressure exports, especially BCD-A28--BCD-A31.
- CD-A ERT/NMR water-content and resistivity calibration.
- CD-A Geoscope, crackmeter, laser-scan, and levelling exports.
- CD-A large-fault/fracture geometry and 2D projection context.

Representative queries included:

- `Mont Terri CD-A experiment TAUPE TDR ARDP water content`
- `Mont Terri CD-A mini-piezometer BCD-A28 BCD-A31 pore pressure`
- `Mont Terri CD-A ERT NMR water content Kruschwitz resistivity`
- `Mont Terri CD-A crackmeter Geoscope laser scan levelling`
- `Mont Terri CD-A twin niches characterization open access 105624`
- `Mont Terri CD-A water content evolution EDZ Opalinus Clay NMR ERT TDR RH Kelvin equation`

## Results

The useful public sources found in this pass are already present in the current
library and bibliography:

- `Ziefle2024Characterization` confirms the CD-A twin-niche measurement inventory,
  structural/fault context, permeability tests, ERT, Taupe/TDR, suction/pressure,
  and broader interpretation setting.
- `WaterContentEDZ2024` confirms the OGS water-content proxy, RH/Kelvin pressure
  convention, ERT/NMR interpretation caveats, Archie-type water--resistivity
  relation, bound/interlayer-water issues, and transform uncertainty.
- `Ziefle2017SeasonalHM` and `Graebling2022VEIS` confirm broader Mont Terri
  seasonal HM monitoring and the existence of sensor database concepts, but they do
  not publish the missing CD-A Geoscope numeric exports.
- Existing general sources (`Archie1942`, `Revil1998ShalySands`,
  `Robinson2003TDRReview`, `Cui2022DualScaleNMR`, `Thomson1871Kelvin`,
  `Klinkenberg1941`, and `Marschall2005`) remain sufficient for the general
  measurement-physics claims used in Section 2.10.

No new public source found in this pass provided the missing project-specific
machine-readable data needed to close the open gates:

- No public BCD-A28--BCD-A31 mini-piezometer export with timestamps, coordinates,
  reference convention, and quality flags was found.
- No public Geoscope crackmeter/extensometer export with signs, zero dates, axes,
  and uncertainties was found.
- No public Taupe workbook calibration note proving whether `Taupe_WC.xlsx` stores
  calibrated volumetric water content, apparent relative dielectric permittivity,
  ARDP, or another processed proxy was found.
- No public ERT-to-OGS transform/support/covariance answer for this exact VTK
  archive was found.
- No public RH active-curve provenance for `08_08_open_niche_seasonal.xml` was
  found.
- No public feature-by-feature 3D-to-2D projection table for the local
  `VisualisationCDA.dat` fault/fracture zones was found.

## Consequence For Section 2.10

The expanded table answers now use local audits and the public literature where
they are sufficient.  Rows that remain unresolved state the best available answer:
the stream is physically meaningful, but the project-specific file, calibration,
support transform, quality flag, reference convention, or covariance is still
missing and must be supplied by the measurement provider or recorded as an explicit
modelling-team decision.

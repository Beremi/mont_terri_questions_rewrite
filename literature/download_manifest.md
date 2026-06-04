# Download Manifest

This manifest follows the citation keys in `paper/references.bib`. "Copied" means that the file was already available in the neighboring local literature library and was copied here for this paper. "Downloaded" means that the file was fetched from an openly reachable web URL during this pass.

## DOI-backed articles

| BibTeX key | DOI | Local file | Status | Source used | Notes |
|---|---|---|---|---|---|
| `Wang2009THM` | `10.1016/j.cageo.2008.07.007` | `fulltexts/Wang2009THM.pdf` | Copied | `../SOTA_OGS_Mont_Terri_work/Library/fulltexts/Wang_Kosakowski_Kolditz_2009_THM_OGS.pdf` | Local fulltext already present. |
| `VanGenuchten1980` | `10.2136/sssaj1980.03615995004400050002x` | `fulltexts/VanGenuchten1980.pdf` | Copied | `../SOTA_OGS_Mont_Terri_work/Library/fulltexts/van_Genuchten_1980_Hydraulic_Conductivity_Unsaturated_Soils.pdf` | Local fulltext already present. |
| `Mualem1976` | `10.1029/WR012i003p00513` | `fulltexts/Mualem1976.pdf` | Downloaded | `https://hwbdocs.env.nm.gov/Los%20Alamos%20National%20Labs/TA%2054/11570.pdf` | The Wiley/AGU publisher PDF endpoint returned HTTP 403; this public government-hosted PDF was verified by title text. |
| `Amann2017Opalinus` | `10.1007/s00015-016-0245-0` | `fulltexts/Amann2017Opalinus.pdf` | Copied | `../SOTA_OGS_Mont_Terri_work/Library/fulltexts/Amann_et_al_2017_Geomechanical_Opalinus_Clay.pdf` | Local fulltext already present. |
| `Marschall2017EDZ` | `10.1007/s00015-016-0246-z` | `fulltexts/Marschall2017EDZ.pdf` | Downloaded | `https://link.springer.com/content/pdf/10.1007/s00015-016-0246-z.pdf` | Springer PDF verified by title text. |
| `Hale2021EDZ` | `10.5194/se-12-1581-2021` | `fulltexts/Hale2021EDZ.pdf` | Downloaded | `https://se.copernicus.org/articles/12/1581/2021/se-12-1581-2021.pdf` | Copernicus open-access PDF verified by title text. |
| `Ziefle2021CDA` | `10.5194/sand-1-79-2021` | `fulltexts/Ziefle2021CDA.pdf` | Copied | `../SOTA_OGS_Mont_Terri_work/Library/fulltexts/Ziefle_et_al_2021_CD_A_setup_first_results.pdf` | Local fulltext already present. |
| `Ziefle2024Characterization` | `10.1016/j.ijrmms.2023.105624` | `fulltexts/Ziefle2024Characterization.pdf` | Copied | `../SOTA_OGS_Mont_Terri_work/Library/fulltexts/Ziefle_et_al_2024_CDA_twin_niches_characterization.pdf` | Local fulltext already present. |
| `WaterContentEDZ2024` | `10.1007/s00603-023-03717-1` | `fulltexts/WaterContentEDZ2024.pdf` | Copied | `../SOTA_OGS_Mont_Terri_work/Library/fulltexts/Ziefle_et_al_2024_Water_Content_EDZ_Opalinus_Clay.pdf` | Local fulltext already present. |
| `Ziefle2017SeasonalHM` | `10.1007/s00015-016-0252-1` | `fulltexts/Ziefle2017SeasonalHM.pdf` | Downloaded | `https://sjg.springeropen.com/counter/pdf/10.1007/s00015-016-0252-1.pdf` | SpringerOpen fulltext verified and text-extracted. |
| `Graebling2022VEIS` | `10.3389/feart.2022.946627` | `fulltexts/Graebling2022VEIS.pdf` | Downloaded | `https://www.frontiersin.org/journals/earth-science/articles/10.3389/feart.2022.946627/pdf` | Frontiers open-access PDF verified and text-extracted. |
| `Marschall2005` | `10.2516/ogst:2005008` | `fulltexts/Marschall2005.pdf` | Downloaded | `https://nora.nerc.ac.uk/id/eprint/15905/1/marchal_vol60n1%5B1%5D.pdf` | NERC-hosted fulltext verified and text-extracted. |
| `Archie1942` | `10.2118/942054-G` | `fulltexts/Archie1942.pdf` | Downloaded | `https://personal.ems.psu.edu/~radovic/EME590_Archie_1942.pdf` | Penn State-hosted scan verified and text-extracted. |
| `Revil1998ShalySands` | `10.1029/98JB02125` | `fulltexts/Revil1998ShalySands.pdf` | Downloaded | `https://larrycathles.eas.cornell.edu/files/2020/11/61-1998-Revil-et-al.-Electrical-conductivity-in-shaly-sands-with-geophy.pdf` | Author-hosted PDF verified and text-extracted. |
| `Cui2022DualScaleNMR` | `10.1007/s11242-022-01752-0` | `fulltexts/Cui2022DualScaleNMR.pdf` | Downloaded | `https://link.springer.com/content/pdf/10.1007/s11242-022-01752-0.pdf` | Springer open-access PDF verified and text-extracted. |
| `Robinson2003TDRReview` | `10.2136/vzj2003.4440` | `fulltexts/Robinson2003TDRReview.pdf` | Downloaded | `https://citeseerx.ist.psu.edu/document?doi=54e738ea97da6ab7af79dbddcd4d1e24ade8c237&repid=rep1&type=pdf` | CiteSeerX endpoint required `curl -k` because of a local certificate-chain verification failure; PDF verified and text-extracted. |
| `Thomson1871Kelvin` | `10.1080/14786447108640606` | `fulltexts/Thomson1871Kelvin.pdf` | Downloaded | `https://zenodo.org/records/1742066/files/article.pdf?download=1` | Zenodo fulltext scan verified and text-extracted. |
| `Topp1980TDR` | `10.1029/WR016i003p00574` | None | Not downloaded | `https://agupubs.onlinelibrary.wiley.com/doi/pdf/10.1029/WR016i003p00574` | Publisher PDF returned HTTP 403; citation retained bibliographically but not used for a fulltext-specific claim. |
| `Kleinberg1996NMR` | `10.1016/S0730-725X(96)00161-0` | None | Not downloaded | ScienceDirect bibliographic/abstract page | No trusted open fulltext was found during this pass; citation retained bibliographically but Chapter 2 relies on downloaded WaterContentEDZ2024 and Cui2022 for NMR-specific fulltext claims. |

## Official OGS documentation snapshots

| BibTeX key | URL | Local file | Status | Notes |
|---|---|---|---|---|
| `OpenGeoSysTRMDocs` | `https://www.opengeosys.org/6.5.7/docs/processes/thermal-processes/trm/` | `web_docs/OpenGeoSysTRMDocs.html` | Downloaded | Official OGS TRM process documentation snapshot. |
| `OpenGeoSysParametersDocs` | `https://www.opengeosys.org/6.5.7/docs/userguide/blocks/parameters/` | `web_docs/OpenGeoSysParametersDocs.html` | Downloaded | Official OGS parameter-block documentation snapshot. |
| `OpenGeoSysProcessVariablesDocs` | `https://www.opengeosys.org/6.5.7/docs/userguide/blocks/process_variables/` | `web_docs/OpenGeoSysProcessVariablesDocs.html` | Downloaded | Official OGS process-variable documentation snapshot. |

## Local project sources

| BibTeX key | Local copy | Original source | Status | Notes |
|---|---|---|---|---|
| `GesaProjectionModel2025` | `local_sources/GesaProjectionModel2025/` | `../SOTA_OGS_Mont_Terri_work/GESA_model_original/projection_on_mesh_2025-09-05/` | Copied partially | Copied the `.prj`, included XML files, and `README.txt`. Bulky mesh and visualization files remain at the original source path. |
| `ModelAudit2026` | `local_sources/ModelAudit2026.md` | `../SOTA_OGS_Mont_Terri_work/MODEL_AUDIT.md` | Copied | Local model-package provenance and XML update audit. |
| `FormulationAudit2026` | `local_sources/FormulationAudit2026.md` | `../SOTA_OGS_Mont_Terri_work/inversion_workflow/ogs_formulation_consistency_audit.md` | Copied | Local OGS formulation audit. |
| `RunInputAudit2026` | `local_sources/RunInputAudit2026.md` | `../SOTA_OGS_Mont_Terri_work/inversion_workflow/current_permeability_field/OGS_RUN_INPUT_AUDIT.md` | Copied | Local run-input and mesh-field audit. |
| `ReleaseGateAudit2026` | `local_sources/ReleaseGateAudit2026.md` | `../SOTA_OGS_Mont_Terri_work/inversion_workflow/inversion_release_gate_audit.md` | Copied | Local inversion release-gate audit. |
| `QuestionInventory2026` | `local_sources/QuestionInventory2026.md` | `mont_terri_questions_reorganized.md` | Copied | Local reorganized collaborator-question inventory. |

## Internal CD-A measurement pages copied for figure provenance

| Source key | Local evidence copy | Original source | Status | Notes |
|---|---|---|---|---|
| `CDATDSlides2026Local` | `source_pages/CD-A_Slides_TD_260427x_page32.png` | `../cda_knowledge_base/measurements/other_hm_monitoring/source_files/CD-A_Slides_TD_260427x.pdf`, PDF p. 32 | Copied rendered page | Mini-piezometer trend source figure used in Chapter 2. |
| `CDATDSlides2026Local` | `source_pages/CD-A_Slides_TD_260427x_page33.png` | `../cda_knowledge_base/measurements/other_hm_monitoring/source_files/CD-A_Slides_TD_260427x.pdf`, PDF p. 33 | Copied rendered page | Crackmeter trend source figure used in Chapter 2. |
| `Levelling2026Local` | `source_pages/Folien_Niv_TD_CDA_2026_page5.png` | `../cda_knowledge_base/measurements/other_hm_monitoring/source_files/Folien_Niv_TD_CDA_2026.pdf`, PDF p. 5 | Copied rendered page | Precision-levelling values backing the extracted bar plot. |
| `Levelling2026Local` | `source_pages/Folien_Niv_TD_CDA_2026_page6.png` | `../cda_knowledge_base/measurements/other_hm_monitoring/source_files/Folien_Niv_TD_CDA_2026.pdf`, PDF p. 6 | Copied rendered page | Precision-levelling uncertainty and summary backing the text. |

## Bibliographic reference without DOI

| BibTeX key | Local file | Status | Notes |
|---|---|---|---|
| `Bishop1959EffectiveStress` | None | Not downloaded | The BibTeX entry does not record a DOI. The stable bibliographic record is `https://cir.nii.ac.jp/crid/1570854174118446592`; no clearly trusted downloadable fulltext source was identified. |
| `Klinkenberg1941` | `fulltexts/Klinkenberg1941.pdf` | Downloaded | No DOI in the BibTeX entry; public scan downloaded from `https://faculty.ksu.edu.sa/sites/default/files/klinkenbergspaper-1941.pdf` and text-extracted. |

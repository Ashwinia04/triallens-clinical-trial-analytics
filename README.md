# TrialLens — Clinical Trial Data Quality & Safety Analytics

[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ashwinia04/triallens-clinical-trial-analytics/blob/main/notebooks/TrialLens_Clinical_Trial_Analytics_Colab.ipynb)

**A reproducible Python and SQL portfolio project using a fully synthetic Phase II clinical-study dataset.**

> **Important data and safety notice:** All study names, participants, sites, records and results are fictional. No real patient data or clinical-trial system is used. This is an educational portfolio simulation, not validated software, and must not be used for clinical, safety, regulatory or treatment decisions.

TrialLens demonstrates a structured workflow for reviewing clinical-style data exports: source profiling, traceable rule-based quality checks, visit-window metrics, descriptive adverse-event summaries, query-resolution measures, exploratory biomarker analysis, SQLite queries and an interactive Streamlit dashboard.

## Project snapshot

| Area | Synthetic project result |
|---|---:|
| Participant rows in source export | 121 |
| Unique participant IDs | 120 |
| Participants retained after documented eligibility and chronology checks | 117 |
| Rule-based data-quality findings | 11 (2 Critical, 7 High, 2 Medium) |
| Query closure rate with a valid close date | 72.3% |
| Median query turnaround among validly closed queries | 7 days |
| Participants with valid paired Baseline and Week 12 hsCRP | 116 |

These values describe only the generated demonstration dataset. The hsCRP analysis is exploratory and does not provide evidence of efficacy or safety.

## Open and run the notebook

- **Browser-based:** Click the Colab badge above or [open the Colab notebook](https://colab.research.google.com/github/Ashwinia04/triallens-clinical-trial-analytics/blob/main/notebooks/TrialLens_Clinical_Trial_Analytics_Colab.ipynb). In Colab, run the first setup cell and upload the companion [`triallens-clinical-trial-analytics.zip`](./triallens-clinical-trial-analytics.zip) file when prompted. Then run the dependency cell and execute the notebook from top to bottom.
- **Local Jupyter:** Open [`notebooks/TrialLens_Clinical_Trial_Analytics.ipynb`](./notebooks/TrialLens_Clinical_Trial_Analytics.ipynb) from the extracted project folder after installing dependencies with `pip install -r requirements.txt`.

The Colab notebook is available at [`notebooks/TrialLens_Clinical_Trial_Analytics_Colab.ipynb`](./notebooks/TrialLens_Clinical_Trial_Analytics_Colab.ipynb). The companion ZIP contains the synthetic CSV inputs and Python source used by the Colab setup cell.

## What the project demonstrates

- **Data profiling:** row counts, column review, missingness and intended-key duplicate checks across six synthetic exports.
- **Data-quality review:** 11 rule-based checks spanning participant demographics, visit records, laboratory units, adverse-event chronology and query closure dates.
- **Clinical operations analytics:** visit completion and protocol-window rates, protocol-deviation summaries, query closure rate and turnaround.
- **Safety summaries:** descriptive adverse-event counts by seriousness and randomized group, with participant counts and interpretation caveats.
- **Exploratory biomarker analysis:** paired Baseline-to-Week-12 hsCRP summaries by randomized group; incomplete or invalid-unit pairs are excluded under documented rules.
- **Technical implementation:** Python, pandas, NumPy, SQLite, SQL, Matplotlib, Streamlit and pytest.

## Repository structure

```text
triallens-clinical-trial-analytics/
├── README.md
├── app.py                              # Streamlit dashboard
├── requirements.txt
├── pyproject.toml
├── LICENSE
├── data/
│   ├── README.md                       # Dataset dictionary and caveats
│   └── raw/                            # Six synthetic CSV exports
├── notebooks/
│   ├── TrialLens_Clinical_Trial_Analytics.ipynb
│   └── TrialLens_Clinical_Trial_Analytics_Colab.ipynb
├── src/triallens/
│   ├── generate_data.py                # Deterministic synthetic data generator
│   ├── quality.py                      # Validation rules
│   ├── analysis.py                     # Cohort, operations, safety and lab analysis
│   └── pipeline.py                     # End-to-end pipeline and SQLite creation
├── sql/analysis_queries.sql
├── tests/test_quality.py
├── outputs/                            # Generated summaries, plots and SQLite DB
├── reports/analysis_summary.md
└── docs/INTERVIEW_GUIDE.md
```

## Run locally

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
python -m triallens.pipeline --regenerate
pytest -q
streamlit run app.py
```

Python 3.10 or newer is recommended.

## Data-quality rule catalogue

| Rule ID | Domain | Check |
|---|---|---|
| DM-001 | Demographics | Duplicate participant identifier |
| DM-002 | Demographics | Missing required participant fields |
| DM-003 | Demographics | Age outside the simulated 18–80 eligibility range |
| DM-004 | Demographics | Invalid date or randomization before consent |
| SV-001 | Visits | Duplicate participant/visit record |
| SV-002 | Visits | Completed visit without a valid actual date |
| SV-003 | Visits | Completed visit outside its permitted window |
| LB-001 | Labs | Duplicate participant/visit/test result |
| LB-002 | Labs | Unit inconsistent with the expected test unit |
| AE-001 | Safety | AE end date before onset date |
| QRY-001 | Queries | Closed query without a valid close date |

The pipeline flags findings; it does not silently overwrite source exports. A data-quality finding is not automatically a protocol deviation or a clinical safety signal.

## Limitations and interpretation

- This is synthetic data; the study, drug code TRX-101, participants, sites and results are fictional.
- The adverse-event analysis is descriptive, not exposure-adjusted or medically adjudicated.
- The hsCRP comparison is an educational statistical exercise; it is not a clinical efficacy analysis.
- The example does not claim CDISC/SDTM conformance, validated EDC integration, GxP validation, commercial EDC experience or production clinical-data-management experience.
- No clinical, safety, regulatory or treatment decisions should be made from this project.

## Suggested portfolio description

**TrialLens — Clinical Trial Data Quality & Safety Analytics (Python, SQL, pandas, Streamlit).** Built a reproducible analytics workflow using a simulated Phase II dataset; implemented 11 traceable validation checks across participant, visit, laboratory, adverse-event and query records; summarized protocol-window compliance, query resolution and descriptive safety patterns; and added exploratory biomarker analysis, SQLite queries, a dashboard and automated tests.

Use this wording only when you can explain the code and results in an interview. Keep the word **simulated** visible so this work is not mistaken for professional clinical-trial experience.

## License

MIT. See [`LICENSE`](./LICENSE).

"""Streamlit dashboard for TrialLens. Run the pipeline before launching."""
from pathlib import Path
import json
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"

st.set_page_config(page_title="TrialLens | Clinical Trial Analytics", page_icon="🧪", layout="wide")
st.title("TrialLens | Clinical Trial Data Quality & Safety Analytics")
st.caption("Simulated Phase II study • synthetic data only • portfolio demonstration")

metrics_file = OUT / "metrics.json"
if not metrics_file.exists():
    st.warning("Analysis outputs are missing. Run `python -m triallens.pipeline` from the project root first.")
    st.stop()

metrics = json.loads(metrics_file.read_text(encoding="utf-8"))
issues = pd.read_csv(OUT / "quality_issues.csv")
visits = pd.read_csv(OUT / "visit_summary.csv")
ae = pd.read_csv(OUT / "ae_summary.csv")
biomarker = pd.read_csv(OUT / "biomarker_summary.csv")

k1, k2, k3, k4 = st.columns(4)
k1.metric("Participants analysed", metrics["participants_in_analysis"])
k2.metric("QA findings", len(issues))
k3.metric("Valid query closure", f'{metrics["query_closure_rate_pct"]}%')
k4.metric("Serious AE records", metrics["serious_ae_count"])

st.subheader("Data-quality review")
left, right = st.columns([1, 2])
with left:
    st.write("**Findings by severity**")
    if not issues.empty:
        st.bar_chart(issues.groupby("severity").size())
    st.write("**Rule-level findings**")
    st.dataframe(issues.groupby(["rule_id", "domain", "severity"]).size().rename("count").reset_index(), use_container_width=True, hide_index=True)
with right:
    st.write("**Review queue**")
    severity_filter = st.multiselect("Filter by severity", sorted(issues["severity"].unique()), default=sorted(issues["severity"].unique()))
    filtered = issues[issues["severity"].isin(severity_filter)]
    st.dataframe(filtered, use_container_width=True, hide_index=True)

st.subheader("Study conduct and safety")
left, right = st.columns(2)
with left:
    st.write("**Visit completion and window compliance**")
    st.dataframe(visits, use_container_width=True, hide_index=True)
    st.bar_chart(visits.set_index("visit_name")[["completion_rate_pct", "within_window_rate_pct"]])
with right:
    st.write("**Adverse events by group and seriousness**")
    st.dataframe(ae, use_container_width=True, hide_index=True)
    terms_path = OUT / "ae_term_summary.csv"
    if terms_path.exists():
        terms = pd.read_csv(terms_path)
        if not terms.empty:
            st.bar_chart(terms.set_index("ae_term").head(8))

st.subheader("Exploratory biomarker analysis")
st.dataframe(biomarker, use_container_width=True, hide_index=True)
st.info(
    f"Exploratory Welch p-value: {metrics['exploratory_welch_p_value']} | "
    f"Cohen's d: {metrics['exploratory_cohens_d']}. These values describe synthetic data only; "
    "they are not clinical evidence or a treatment recommendation."
)

st.subheader("Interpretation notes")
st.markdown(
    "- Data-quality findings are review prompts, not automatic corrections.\n"
    "- Clinical reference-range flags are not equated with data-entry errors.\n"
    "- Analysis uses explicit eligibility, chronology, duplicate, and unit checks.\n"
    "- No real patient data, regulated EDC system, or validated clinical workflow is represented."
)

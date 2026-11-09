# college_dataset.csv

One row per U.S. college: **selectivity** (admissions, test scores), **what families pay by income bracket**, **Pell share**, and **Opportunity Insights (Chetty et al.) parent-income and mobility measures**. Built for the college selectivity project in the data science course.

**Built by:** `college_dataset_builder.ipynb` (run in Google Colab; takes a few minutes). Rerun it to refresh the data or change `YEAR`.
**Data year:** IPEDS / Urban Institute data for 2021 (the `YEAR` setting in the notebook); Opportunity Insights data for students who attended college roughly 1999-2013 (see their documentation). The two sources cover different years, so don't treat them as a single snapshot.
**Downloaded:** November 2026.

## Sources (please cite)

1. **Urban Institute, Education Data Portal** (https://educationdata.urban.org), which serves NCES **IPEDS** data. Endpoints used: `ipeds/directory`, `ipeds/admissions-enrollment`, `ipeds/sfa-grants-and-net-price`, `ipeds/sfa-ftft`. See the portal's terms of use.
2. **Opportunity Insights, Mobility Report Cards**, `mrc_table2.csv` (https://opportunityinsights.org/data/): Chetty, Friedman, Saez, Turner, and Yagan, "Mobility Report Cards: The Role of Colleges in Intergenerational Mobility" (2017/2020). Check the license on their data page before reusing.

## Load it

```python
import pandas as pd
df = pd.read_csv("URL_OR_PATH/college_dataset.csv")
```

## Columns

| Column | Meaning |
|---|---|
| `unitid` | IPEDS college ID (the key for all Urban Institute data) |
| `inst_name`, `state_abbr`, `inst_control`, `inst_level` | Name, state, public/private control and level (integer codes; see the Education Data Portal codebook) |
| `opeid` | 8-digit Department of Education ID; first 6 digits link to Chetty's `super_opeid` |
| `applicants`, `admitted`, `enrolled` | Counts from IPEDS admissions data |
| `admit_rate` | `admitted / applicants` (0-1). Open-admission schools show 1.0 |
| `yield` | `enrolled / admitted` (0-1): the share of admitted students who enroll |
| `sat_math_mid`, `sat_reading_mid`, `sat_total_mid` | **Midpoint of the 25th and 75th percentile**, not the average (IPEDS doesn't publish averages) |
| `act_composite_mid` | Same, for the ACT composite |
| net price columns ending `_inc1` ... `_inc5` | What families in each income bracket pay after grants. Suffix = Scorecard income bracket: 1 = $0-30k, 2 = $30-48k, 3 = $48-75k, 4 = $75-110k, 5 = $110k+. Confirm the code meanings in the portal codebook |
| columns containing `pell` | Share of first-time, full-time students receiving Pell grants (a stand-in for low-income enrollment) |
| `super_opeid` | Opportunity Insights college ID |
| `oi_*` | Columns from Opportunity Insights Table 2, e.g. `oi_par_median` (median parent income), `oi_par_top1pc` (share of students from the top 1%), `oi_par_q1` (share from the bottom quintile), `oi_k_median` (students' own median income in their mid-30s), `oi_mr_kq5_pq1` (mobility rate: bottom quintile to top quintile). See their codebook for the full list and dollar year |

## Things to know before analyzing

- **Missing data.** The Urban API codes missing values as negative numbers (-1, -2, -3); the notebook converts them to `NaN`. Many columns have a lot of `NaN`.
- **Test-optional schools.** Many schools stopped requiring SAT/ACT around 2020, so test-score columns are missing or unrepresentative for them.
- **Not every college has Chetty data.** The match is on 6-digit OPEID, and Chetty groups multi-campus systems under one ID. Where several campuses share an ID, the notebook keeps the one with the most applicants. Check `df["super_opeid"].notna().sum()` to see how many matched.
- **Suspicious rows.** A few colleges have an `admit_rate` of exactly 0, which is probably a data problem worth investigating.
- **Related file:** `top_colleges.csv` is a small hand-assembled table of famous schools (acceptance rate, average SAT/ACT, endowment, tuition). Useful for comparison, but its numbers come from a different source and year.

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
| `inst_name`, `state_abbr`, `inst_control` | Name, state, and control (integer code: 1 = public, 2 = private nonprofit, 3 = private for-profit; confirm in the Education Data Portal codebook) |
| `opeid` | 8-digit Department of Education ID; first 6 digits link to Chetty's `super_opeid` |
| `applicants`, `admitted`, `enrolled` | Counts from IPEDS admissions data |
| `admit_rate` | `admitted / applicants` (0-1). Open-admission schools show 1.0 |
| `yield` | `enrolled / admitted` (0-1): the share of admitted students who enroll |
| `open_admissions_policy` | IPEDS open-admissions flag (integer code; see codebook) |
| `sat_percent_submitting`, `act_percent_submitting` | Percent of enrolled students whose SAT / ACT scores were used in admissions. Low values signal test-optional policies |
| `sat_ebrw_25/75`, `sat_math_25/75` | 25th and 75th percentile SAT section scores of enrolled first-year students (IPEDS publishes percentiles, **not** averages). The `_50` (median) versions of these columns exist but are **empty in the 2021 data** |
| `sat_total_25/75` | Sum of the EBRW and math percentiles. An approximation, since percentiles don't strictly add. `sat_total_50` is empty in the 2021 data |
| `act_composite_25/75` | 25th and 75th percentile ACT composite (`act_composite_50` is empty in the 2021 data) |
| `net_price_inc1` ... `inc5`, `net_price_inc99` | Average net price (cost after grants) for students in each family-income bracket. Suffix: 1 = $0-30k, 2 = $30-48k, 3 = $48-75k, 4 = $75-110k, 5 = $110k+, 99 = all students (confirm codes in the portal codebook) |
| `average_grant_inc*`, `total_grant_inc*`, `number_of_students_inc*`, `number_receiving_grants_inc*` | Grant aid and student counts for the same income brackets |
| `pell_pct`, `pell_students`, `pell_avg_amount` | Share (a fraction from 0 to 1, e.g. 0.19 = 19%) and number of first-time, full-time students receiving Pell grants, and the average Pell amount: a stand-in for low-income enrollment. Note that `sat_percent_submitting` and `act_percent_submitting` are on a 0-100 scale instead |
| `super_opeid` | Opportunity Insights college ID |
| `oi_match`, `oi_name_similarity` | How the Chetty row was linked (`opeid` or `name`) and how similar the two college names are (0-1) |
| `oi_*` | Columns from Opportunity Insights Table 2, e.g. `oi_par_median` (median parent income), `oi_par_top1pc` (share of students from the top 1%), `oi_par_q1` (share from the bottom quintile), `oi_k_median` (students' own median income in their mid-30s), `oi_mr_kq5_pq1` (mobility rate: bottom quintile to top quintile). See their codebook for the full list and dollar year |

## Things to know before analyzing

- **Missing data.** The Urban API codes missing values as negative numbers (-1, -2, -3); the notebook converts them to `NaN`. Many columns have a lot of `NaN`.
- **Test-optional schools.** Many schools stopped requiring SAT/ACT around 2020, so test-score columns are missing or unrepresentative for them. Check `sat_percent_submitting` before comparing scores.
- **Coverage.** 5,346 colleges in all; about 1,850 have admit rates, about 960-970 have SAT/ACT percentiles, about 4,600 have Pell data, and 2,007 have Chetty data. 1,152 have both admit rates and Chetty data (776 with SAT/ACT percentiles too).
- **How colleges are linked to Chetty's data.** First by 6-digit OPEID (IPEDS `opeid` = Chetty `super_opeid`); colleges still unmatched are then matched by exact name (`oi_match` says which method was used). Chetty's `super_opeid` is their own construction and sometimes differs from IPEDS (Harvard is 129 in their file), so ID matches are not perfect. `oi_name_similarity` (0-1) compares the two names; values below about 0.5 can be a renamed school or a coincidental ID collision, so check them by hand. Chetty groups multi-campus systems under one ID; where several campuses share an ID, the notebook keeps the one with the most applicants. Not every college is in Chetty's data at all (e.g. Tulane isn't). Check `df["super_opeid"].notna().sum()` for the match count.
- **Admit rate of 0.** A few tiny schools report 1-2 applicants and none admitted, so `admit_rate` is 0. Consider filtering on `applicants`.
- **Related file:** `top_colleges.csv` is a small hand-assembled table of famous schools (acceptance rate, average SAT/ACT, endowment, tuition). Useful for comparison, but its numbers come from a different source and year.

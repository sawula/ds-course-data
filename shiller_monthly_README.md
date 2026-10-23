# shiller_monthly.csv

Monthly U.S. stock market data, **January 1871 – October 2026** (1,870 rows).

**Source:** Robert J. Shiller, *Irrational Exuberance* data (`ie_data.xls`), https://shillerdata.com/
Cleaned from the "Data" sheet; downloaded October 2026.

Shiller's disclaimer: the data were assembled from public sources and are not guaranteed to be accurate or complete.

## Load it

```python
import pandas as pd
sh = pd.read_csv("URL_OR_PATH/shiller_monthly.csv", parse_dates=["Date"], index_col="Date")
```

## Columns

| Column | Meaning |
|---|---|
| `Date` | First day of the month (YYYY-MM-01) |
| `Price` | S&P Composite stock price index (monthly average of daily closes) |
| `Dividend` | Dividends per share, annualized |
| `Earnings` | Earnings per share, annualized |
| `CPI` | Consumer Price Index (inflation) |
| `Rate_10yr` | Long-term interest rate (10-year Treasury yield since 1953), in percent |
| `Real_Price` | Price adjusted for inflation (in today's dollars) |
| `Real_Dividend` | Dividend adjusted for inflation |
| `Real_Earnings` | Earnings adjusted for inflation |
| `Real_Total_Return_Price` | Inflation-adjusted value with dividends reinvested ("what $ grew to") |
| `CAPE` | Cyclically Adjusted P/E ratio: real price ÷ average real earnings over the past 10 years |
| `TR_CAPE` | CAPE version using total-return (dividends reinvested) prices |
| `Excess_CAPE_Yield` | (1 / CAPE) minus the real bond yield; higher = stocks cheaper relative to bonds |
| `Fwd10yr_Real_Stock_Return` | Annualized real stock return over the **next** 10 years (0.05 = 5%/yr) |
| `Fwd10yr_Real_Bond_Return` | Annualized real bond return over the **next** 10 years |

## Gaps (blank cells are normal)

- `CAPE`, `TR_CAPE`, `Excess_CAPE_Yield` start in **1881** (CAPE needs 10 years of earnings).
- `Fwd10yr_...` columns end in **Oct 2016**: they need 10 years of future data.
- `Dividend` / `Earnings` lag a few months (last value: June 2026).
- Oct 2026 price is the Oct 2 close; Sept/Oct 2026 CPI is estimated by Shiller.

## Benchmarks to check against

| Date | CAPE |
|---|---|
| Sep 1929 | 32.6 |
| Dec 1999 (all-time high) | 44.2 |
| May 2007 | 27.5 |
| Oct 2026 | 40.7 |

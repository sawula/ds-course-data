# macro_monthly_1962.csv — Stocks, rates, inflation, gold and oil by month

One row per month, January 1962 to October 2026 (778 rows). Built in Google
Colab by a notebook (`econ_macro_monthly_1962.ipynb`) that downloads everything
fresh each time it runs, so it can be re-run to update the file.

## Load it

```python
import pandas as pd
url = "https://raw.githubusercontent.com/sawula/ds-course-data/main/macro_monthly_1962.csv"
macro = pd.read_csv(url, parse_dates=["date"], index_col="date")
```

## Where the data comes from

| Columns | Source | Notes |
|---|---|---|
| `sp500` | Yahoo Finance, ticker `^GSPC` (via the `yfinance` package) | Daily closes, reduced to each month's last trading day |
| `gs10`, `tb3ms`, `fedfunds`, `cpi`, `unrate`, `oil`, `recession` | FRED (Federal Reserve Bank of St. Louis), series `GS10`, `TB3MS`, `FEDFUNDS`, `CPIAUCSL`, `UNRATE`, `WTISPLC`, `USREC` | Free. A free FRED API key makes the download more reliable |
| `gold` | World Bank Commodity Markets ("Pink Sheet"), via the open `datasets/gold-prices` repository on GitHub | Monthly average price |

## Column dictionary

**Raw (nominal) columns — as published by the source**

| Column | Meaning | Units |
|---|---|---|
| `date` | Month | YYYY-MM |
| `sp500` | S&P 500 index, last trading day of the month. Price only, dividends not included | index points |
| `gold` | Gold price, monthly average | US dollars per troy ounce |
| `oil` | West Texas Intermediate crude oil, monthly average | US dollars per barrel |
| `gs10` | 10-year US Treasury yield, monthly average | percent per year |
| `tb3ms` | 3-month US Treasury bill rate, monthly average | percent per year |
| `fedfunds` | Effective federal funds rate (the rate banks charge each other overnight; the Fed's main policy rate), monthly average | percent per year |
| `cpi` | Consumer Price Index for all urban consumers, all items. Measures the price level, so it only goes up over the long run | index, 1982–84 = 100 |
| `unrate` | Unemployment rate | percent of labor force |
| `recession` | 1 if the month falls in an NBER-dated US recession, otherwise 0 | 0 / 1 |

**Derived columns — calculated from the raw columns**

| Column | How it is calculated | What it tells you |
|---|---|---|
| `cpi_yoy_pct` | Percent change in `cpi` vs. 12 months earlier | The inflation rate |
| `yield_curve_10y_3m` | `gs10` − `tb3ms` | The "yield curve" slope. Negative means *inverted* (short rates above long rates), which has often come before recessions |
| `real_10yr_rate` | `gs10` − `cpi_yoy_pct` | Interest rate after inflation. Often more relevant to gold than the headline rate |
| `real_fedfunds` | `fedfunds` − `cpi_yoy_pct` | Same idea for the Fed's policy rate |
| `sp500_real`, `gold_real`, `oil_real` | price ÷ `cpi` × (latest month's `cpi`) | The price expressed in **today's dollars**, so a 1970s value and a 2020s value can be compared fairly |

## Reading the data: things to know

1. **Nominal vs. real.** Nominal means the dollar amount at the time. Real
   means adjusted for inflation. Compare `gold` with `gold_real` on a chart:
   gold's 1980 peak looks modest in nominal terms but enormous in real terms.
2. **Gold was not a free market for the first years.** The price was fixed at
   $35 per ounce until 1971 and Americans could not legally own gold until
   1975. The flat line then jump around 1971–1980 is real history, not a data
   error.
3. **Oil was also managed early on.** Crude sat around $3 a barrel through the
   1960s. The big jumps start with the 1973 embargo and the 1979 oil shock.
4. **Month-end vs. monthly average.** `sp500` is a month-end level. The rate,
   oil and gold columns are monthly averages. Fine for trends, but not for
   comparing what happened on a specific day.
5. **S&P 500 excludes dividends.** Real long-run stock returns were higher than
   `sp500` alone suggests.
6. **Bond prices are not included.** Bond ETFs such as TLT only date back to
   about 2002. For a 1962 start, the yield (`gs10`) is the bond data. Bond
   prices move opposite to yields: when `gs10` rises, existing bonds lose
   value.
7. **Revisions.** FRED shows the latest revised figures for CPI, unemployment
   and the recession flag, not what people knew at the time. Recession dates
   are announced by NBER months after they begin.
8. **The current month is dropped** if any market series (S&P 500, rates, oil,
   gold) is not complete yet, so the last row may be a month or two behind
   today.
9. **October 2025 has blanks.** The 2025 US government shutdown stopped data
   collection, so the Bureau of Labor Statistics never published CPI or the
   unemployment rate for that month. The row is kept, but `cpi`, `unrate`,
   and every column calculated from CPI are empty. Because year-over-year
   inflation compares to the same month a year earlier, `cpi_yoy_pct`,
   `real_10yr_rate` and `real_fedfunds` are also empty for **October 2026**.
10. **Why the first inflation values are available.** `cpi_yoy_pct` for early
   1962 uses CPI from 1961, which the script downloads even though the file
   starts in 1962.

## Ideas for analysis

- Chart `sp500_real` and `gold_real` as growth of $100 on a log scale.
- Plot `gs10` against `cpi_yoy_pct`. Do rates follow inflation, and with what lag?
- Shade the `recession == 1` months and mark when `yield_curve_10y_3m` was negative.
- Compute a rolling 36-month correlation between monthly S&P 500 changes and
  monthly changes in `gs10`. Does it stay the same sign across decades?
- Compare `gold_real` with `real_10yr_rate`. Does gold do better when real
  rates are low or negative?
- Look at `oil_real` against `cpi_yoy_pct` during 1973–74 and 1979–80.

## Licensing and attribution

FRED data are free to use with attribution to the original sources (BLS,
Federal Reserve Board, NBER, EIA, etc.). The gold dataset is released under the
Open Data Commons Public Domain Dedication. Yahoo Finance data are for
personal and educational use. Check their terms before redistributing the
S&P 500 column.

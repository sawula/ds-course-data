# Survey-of-Python-data-science-stack
Files, links for a series of lessons to introduce someone to a Python data science stack.

* NYC ER ... file was downloaded (and cleaned a bit) from NYC Health Dept EpiQuery on 4Jun20, https://a816-health.nyc.gov/hdi/epiquery/visualizations?PageType=ps&PopulationSource=Syndromic

* PandasJumble0.csv, PandasJumble1.csv, PandasJumble2.csv added to help practice with select, sort, groupby.

* coldmed.csv ... 5 years of Google Trends data for 'cold medicine' added to compare with patterns in NYC ER 

* resume.csv is Kosuke Imai's abridgement of the data from Marianne Bertrand and Sendhil Mullainathan's "Are Emily and Greg more employable than Lakisha and Jamal?" in the American Economic Review, vol. 94, pp. 991-1013. Imai's repo is at https://github.com/kosukeimai/qss/tree/master/CAUSALITY

* resume_city_eoe.csv is an abridgement (4 columns) of the Bertrand and Mullainathan data via https://dev.openicpsr.org/openicpsr/project/108486/version/V1/view;jsessionid=D57159F04E26C7F92F83177737DDEDA6

* college_dataset.csv (with college_dataset_README.md and the Colab notebook college_dataset_builder.ipynb that builds it) merges IPEDS admissions and net-price-by-income data from the Urban Institute Education Data Portal with Opportunity Insights (Chetty et al.) college mobility data, one row per college, for a project on college selectivity. See college_dataset_README.md for sources, columns and caveats.

* college_selectivity_starter.ipynb is the student starter notebook for the college selectivity project: it loads college_dataset.csv and lays out the dataset's strengths and weaknesses without doing the analysis.

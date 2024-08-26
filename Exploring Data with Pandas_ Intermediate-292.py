## 1. Introduction ##

import pandas as pd
# read the data set into a pandas dataframe
f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None

# replace 0 values in the "previous_rank" column with NaN
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

f500_selection = f500[['rank', 'revenues', 'revenue_change']].head()



## 2. Reading CSV Files with pandas ##

import pandas as pd

f500 = pd.read_csv('f500.csv')

f500.loc[f500['previous_rank'] == 0, 'previous_rank'] = np.nan

## 3. Using iloc to Select by Integer Location ##

fifth_row = f500.iloc[4]

company_value = f500.iloc[0,0]

duas_colunas = f500.iloc[:, 0:2]

## 4. Using iloc to Select by Integer Location (Continued) ##

primeira = f500.iloc[:,0]
segunda = f500.iloc[:,0:2]

colunas_0_1_2_5_10 = f500.iloc[:, [0, 1, 2, 5, 10]]

top_3 = f500.iloc[[0, 1, 2]]


first_three_rows = f500.iloc[[0,1,2]]

first_seventh_row_slice = f500.iloc[[0, 6], :5]

duas_linhas_duas_colunas = f500.iloc[[0, 2], [0, 2]]

top_10 = f500.iloc[:10, [0, 1, 2]]

## 5. Using pandas Methods to Create Boolean Masks ##

null_previous_rank = f500[['company', 'rank', 'previous_rank']][f500['previous_rank'].isnull()]


## 6. Working with Integer Labels ##

null_previous_rank = f500[f500["previous_rank"].isnull()]

top5_null_prev_rank = null_previous_rank.iloc[:5]
top5_null_prev_rank_loc = null_previous_rank.loc[48:140]

## 7. Pandas Index Alignment ##

previously_ranked = f500[f500['previous_rank'].notnull()]

rank_change = previously_ranked['previous_rank'] - previously_ranked['rank']

f500['rank_change'] = rank_change



## 8. Using Boolean Operators ##

large_revenue = f500['revenues'] > 100000

negative_profits = f500['profits'] < 0

combined = large_revenue & negative_profits

big_rev_neg_profit = f500[combined]

France_200000 = f500[(f500['country'] == 'France') & (f500['revenues'] > 200000)]

Germany_200000 = f500[(f500['country'] == 'Germany') & (f500['revenues'] > 200000)]

top10 = f500.head(10)

## 9. Using Boolean Operators (Continued) ##

brazil_venezuela = f500[(f500['country'] == 'Brazil') | (f500['country'] == 'Venezuela')]


tech_outside_usa = f500[~(f500['country'] == 'USA') & (f500['sector'] == 'Technology')].head()

## 10. Sorting Values ##

TOP_japanese_employer = f500[f500['country'] == 'Japan'].sort_values('employees', ascending=False).head(1)


Japan = f500[f500['country'] == 'Japan']
japan_employees = Japan.sort_values('employees', ascending=False)

top_japanese_employer = japan_employees.iloc[0].loc['company']

top5_japanese_revenues = f500[f500['country'] == 'Japan'].sort_values('revenues', ascending=False).head(5)

top_japanese_stocks = f500[f500['country'] == 'Japan'].sort_values('total_stockholder_equity', ascending=False).iloc[0].loc['company']

## 11. Using Loops with pandas ##

top_employer_by_country = {}

countries = f500['country'].unique()

for c in countries:
    selected_rows = f500[f500["country"] == c].sort_values('employees', ascending=False).iloc[0].loc['company']
    top_employer_by_country[c] = selected_rows

## 12. Challenge: Calculating Return on Assets by Sector ##

f500['roa'] = f500['profits'] / f500['assets']

sector = f500['sector'].unique()

top_roa_by_sector = {}

for c in sector:
    sectores_paises_roa = f500[f500['sector'] == c].sort_values('roa', ascending=False).iloc[0].loc['company']
    top_roa_by_sector[c] = sectores_paises_roa
    
pais = f500['country'].unique()
top_roa_por_pais = {}
for p in pais:
    empresas_pais_roa = f500[f500['country']==p].sort_values('roa', ascending=False).iloc[0].loc['company']
    roa = f500[f500['country']==p].sort_values('roa', ascending=False).iloc[0].loc['roa']
    top_roa_por_pais[p] = empresas_pais_roa, roa

Subaru = f500[f500['company'] == 'Subaru']
Toyota = f500[f500['company'] == 'Toyota Motor']


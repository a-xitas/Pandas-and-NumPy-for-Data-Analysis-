## 1. Introduction to the Data ##

f500_head = f500.head(10)

f500.info()

## 2. Vectorized Operations ##

profit_per_sale = (round(f500.loc[:, 'profits'] / f500.loc[:, 'revenues'], 3))

profit_per_sale_20_TOP = profit_per_sale.head(20)
profit_per_sale_20_TAIL = profit_per_sale.tail(20)

rank_change = f500.loc[:, 'previous_rank'] - f500.loc[:, 'rank']

profit_per_sale_countries = profit_per_sale, f500.loc[:, 'country']

#print(profit_per_sale_countries)

countries = f500['country']
#France = countries[:, 'France']

Christian_Dior = profit_per_sale.loc['Christian Dior']
Coca_Cola = profit_per_sale.loc['Coca-Cola']

Auto = f500.loc[['AutoNation'], ['rank', 'previous_rank']]


## 3. Series Data Exploration Methods ##

rank_change =  f500["previous_rank"] - f500["rank"]

rank_change_max = rank_change.max()
rank_change_min = rank_change.min()



## 4. Series Describe Method ##

rank = f500['rank']
rank_desc = rank.describe()

prev_rank = f500['previous_rank']
prev_rank_desc = prev_rank.describe()

sector = f500['sector']
sector_desc = sector.describe()
perc_Financ_F500 = (sector_desc['freq'] / sector_desc['count']) * 100

## 5. Method Chaining ##

zero_previous_rank = f500['previous_rank'].value_counts().loc[0]

Israel = f500.loc[:,'country'].value_counts().loc['Israel']


France=f500['country'].value_counts().loc['France']

Germany = f500['country'].value_counts().loc['Germany']


## 6. Dataframe Exploration Methods ##

# Calcular o valor máximo do DataFrame F500, mas apenas
# para as colunas (axis=0), e para aquelas colunas q
# apresentam valores numericos (numeric_only=True):
max_f500 = f500.max(axis=0, numeric_only=True)

max_stock = f500['total_stockholder_equity'].max()

revenue_TOTAL = f500['revenues'].sum()

medias = f500[['revenues', 'profits']].mean(axis=0)
mediana = f500[['revenues', 'profits']].median(axis=0) 

## 7. Dataframe Describe Method ##

#Retornar estatisticas descritivas de um DF (DataFrame):
f500_desc = f500.describe()

f500_country_desc = f500['country'].describe()

f500_object_desc = f500.describe(include=['O'])


## 8. Assignment with pandas ##

top10_rank_revenue = f500[['rank', 'revenues']].head(10)

top10_rank_revenue.loc['Apple', 'revenues'] = 0

#Walmart_rank_change
top10_rank_revenue.loc['Walmart', 'rank'] = 10


f500.loc['Dow Chemical', 'ceo'] = 'Jim Fitterling'

Dow_Chemical = f500.loc['Dow Chemical', :]


## 9. Using Boolean Indexing with pandas Objects ##

Alemanha = f500[f500['country'] == 'Germany']

motor_bool = f500['industry'] == 'Motor Vehicles and Parts'
motor_countries = f500.loc[motor_bool, 'country']

motor_cities = f500.loc[motor_bool, 'hq_location']



## 10. Using Boolean Arrays to Assign Values ##

import numpy as np
prev_rank_before = f500["previous_rank"].value_counts(dropna=False).head()

f500.loc[f500['previous_rank'] == 0, 'previous_rank'] = np.nan

#bol = f500['previous_rank'] == 0
#f500.loc[bol, 'previous_rank'] = np.nan

prev_rank_after = f500['previous_rank'].value_counts(dropna=False).head()

## 11. Creating New Columns ##

f500['rank_change'] = f500['previous_rank'] - f500['rank']

rank_change_desc = f500['rank_change'].describe()

max_up_change = f500.loc[f500['rank_change'] == 226.000000, 'rank_change']
Centene = f500.loc['Centene', :]

max_down_change = f500.loc[f500['rank_change'] == -199.000000, 'rank_change']

E_ON = f500.loc['E.ON', :]


## 12. Challenge: Top Performers by Country ##

top_5_countries = f500['country'].value_counts().head(5)

# Aqui 1º criei um DataFrame (CHINA) que é composto por todas as empresas cujo o pais (country) é igual (==) a China:
CHINA = f500.loc[f500['country'] == 'China']
# Depois de ter criado o DF acima, usei-o, mas apenas a coluna que diz respeito ao sector, e contei todos os sectores que faziam parte dele, mas pedi para me retornar apenas os 3 primeiros, ou seja os 3 + comuns:
sector_china = CHINA['sector'].value_counts().head(3)

# Aqui fiz a mm operação q em cima, m em vez de criar 1º um novo DF, usei logo essa info (f500.loc[f500'country' == 'USA']) na mesma linha, poupando desta forma memória:
industry_usa = f500.loc[f500['country'] == 'USA']['industry'].value_counts().head(2)

industry_Germany = f500.loc[f500['country'] == 'Germany']['industry'].value_counts().head()


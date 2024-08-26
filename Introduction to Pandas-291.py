## 2. Introduction to the Data ##

import pandas as pd
f500 = pd.read_csv('f500.csv',index_col=0)
f500.index.name = None

f500_type = type(f500)
f500_shape = f500.shape




## 3. Introducing DataFrames ##

import pandas as pd

animais = pd.DataFrame({'ANIMAIS':['galinhas', 'abelhas', 'cães',
                                   'gatos', 'tigres', 'leopardos',
                                   'zebras', 'burros', 'humanos']})

# Por defeito o método DataFrame.head() dá-nos as 5 primeiras linhas
animais_top5 = animais.head()
print(animais_top5)

animais_top3 = animais.head(3)
print(animais_top3)

# Por defeito o método DataFrame.tail() dá-nos as 5 primeiras linhas
animais_last5 = animais.tail()
print(animais_last5)

animais_last3 = animais.tail(3)
print(animais_last3)


# 6 primeiras linhas do DataSet Fortune_500(f500)
f500_head = f500.head(6)
# Últimas 8 linhas do DataSet Fortune_500(f500)
f500_tail = f500.tail(8)


## 4. Introducing DataFrames (Continued) ##

f500.info()

## 5. Selecting a Column from a DataFrame by Label ##

industries = f500['industry']
industries_type = type(industries)

industries_2 = f500.loc[:'Toyota Motor','industry']

                       

## 7. Selecting Columns from a DataFrame by Label (Continued) ##

countries = f500.loc[:, 'country']

revenues_years = f500[['revenues', 'years_on_global_500_list']]

ceo_to_sector = f500.loc[:, 'ceo':'sector']


## 8. Selecting Rows from a DataFrame by Label ##

toyota = f500.loc['Toyota Motor', :]

drink_companies = f500.loc[['Anheuser-Busch InBev', 'Coca-Cola', 'Heineken Holding'], :]

middle_companies = f500.loc['Tata Motors':'Nationwide', 'rank':'country']

primeiras_5_linhas = f500['Walmart':'Toyota Motor']

## 10. Value Counts Method ##

industries = f500.loc[:, 'industry']
industries_n = industries.value_counts()
print(industries_n)

countries = f500_sel.loc[:, 'country']
country_counts = countries.value_counts()
print(country_counts)

# Agora sacar o nmr de países reprensentados na lista toda da F500:
countries_all = f500.loc[:, 'country']
countries_all_counts = countries_all.value_counts()
print(countries_all_counts)

## 11. Selecting Items from a Series by Label ##

countries = f500['country']
countries_counts = countries.value_counts()

india = countries_counts.loc["India"]

north_america = countries_counts.loc[["USA", 'Canada', 'Mexico']]

Europe = countries_counts.loc[['France', 'Spain', 'Germany', 'Netherlands', 'Britain', 'Italy', 'Ireland', 'Sweden', 'Norway', 'Belgium', 'Denmark', 'Luxembourg', 'Finland']]

usa = countries_counts.loc['USA']

print(sum(north_america))
print(sum(Europe))



## 12. Summary Challenge ##

big_movers = f500.loc[['Aviva', 'HP', 'JD.com', 'BHP Billiton'], ['rank', 'previous_rank']]

bottom_companies = f500.loc['National Grid':'AutoNation', ['rank', 'sector', 'country']]

top_5 = f500.loc['Walmart':'Toyota Motor', ['rank', 'sector', 'country', 'revenues', 'profits']]

top_5_Country = top_5.loc[:, 'country']
top_5_counts = top_5_Country.value_counts()

bottom_5 = f500.tail()
top_10 = f500.head(10)

countries_total = f500.loc[:, 'country']
#Israel = countries_total.loc[[:]['Israel']]


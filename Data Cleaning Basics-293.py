## 1. Reading CSV Files with Encodings ##

import pandas as pd

laptops = pd.read_csv('laptops.csv', encoding='Latin-1')


laptops.info()


## 2. Cleaning Column Names ##

new_columns = []

for c in laptops.columns:
    c = c.strip()
    new_columns.append(c)

laptops.columns = new_columns.copy()

## 3. Cleaning Column Names (Continued) ##

import pandas as pd

laptops = pd.read_csv('laptops.csv', encoding='Latin-1')

def clean(index):
    index = index.strip()
    index = index.replace(' ', '_')
    index = index.replace('(', '')
    index = index.replace(')','')
    index = index.lower()
    index = index.replace('operating_system', 'os')
    return index


new_columns = []
for index in laptops.columns:
    index = clean(index)
    new_columns.append(index)
    
laptops.columns = new_columns.copy()

## 4. Converting String Columns to Numeric ##

unique_ram = laptops['ram'].unique()


## 5. Removing Non-Digit Characters ##

laptops['ram'] = laptops['ram'].str.replace('GB','')

unique_ram = laptops['ram'].unique()
                                            

## 6. Converting Columns to Numeric dtypes ##

laptops["ram"] = laptops["ram"].str.replace('GB','')

laptops['ram'] = laptops['ram'].astype(int)

# Retornar o tipo das diferentes colunas do DF:
dtypes = laptops.dtypes


## 7. Renaming Columns ##

laptops["ram"] = laptops["ram"].str.replace('GB','').astype(int)

laptops = laptops.rename({'ram':'ram_gb'}, axis=1)
# OU (ao útilizar o inplace=True ele grava logo em cima do ficheiro do DF as alterações efetuadas:
laptops.rename(columns={'ram':'ram_gb'}, inplace=True)

ram_gb_desc = laptops['ram_gb'].describe()

## 8. Extracting Values from Strings ##

laptops["gpu_manufacturer"] = (laptops["gpu"]
                                       .str.split()
                                       .str[0]
                              )

laptops['cpu_manufacturer'] = laptops['cpu'].str.split().str[0]
cpu_manufacturer_counts = laptops['cpu_manufacturer'].value_counts()

gpu_manufacturer_counts = laptops['gpu_manufacturer'].value_counts()

## 9. Correcting Bad Values ##

mapping_dict = {
    'Android': 'Android',
    'Chrome OS': 'Chrome OS',
    'Linux': 'Linux',
    'Mac OS': 'macOS',
    'No OS': 'No OS',
    'Windows': 'Windows',
    'macOS': 'macOS'
}

laptops['os'] = laptops['os'].map(mapping_dict)

os_counts = laptops['os'].value_counts()

## 10. Dropping Missing Values ##

# Remover as linhas/colunas que não apresentam valores (NaN):

laptops_no_null_rows = laptops.dropna(axis=0)
laptops_no_null_cols = laptops.dropna(axis=1)

## 11. Filling Missing Values ##

value_counts_before = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()
laptops.loc[laptops["os"] == "macOS", "os_version"] = "X"

# Aqui fomos 1º a todas as linhas da coluna 'os' que têm lá 'No OS' e dp substituimos essas linhas, mas apenas para a coluna 'os_version' com a designação 'Version Unknown':
laptops.loc[laptops['os'] == 'No OS', 'os_version'] = 'Version Unknown'

value_counts_after = laptops.loc[laptops['os_version'].isnull(),'os'].value_counts()


# Convert the price_euros column to a numeric dtype.
#laptops['price_euros'] = laptops['price_euros'].str.replace(',','.').astype(float)
#print(laptops['price_euros'].dtype)
#print(laptops['price_euros'])

# Extract the screen resolution from the screen column.
#print(laptops['screen'])
#laptops['screen_resolution'] = laptops['screen'].str.split().str[-1]


# Extract the processor speed from the cpu column.
#print(laptops['cpu'])
#laptops['cpu_speed'] = laptops['cpu'].str.split().str[-1]


# Are laptops made by Apple more expensive than those made by other manufacturers?
#manufacturers = laptops['manufacturer'].value_counts()
#DELL
#manufacturer_Dell = laptops[laptops['manufacturer'] == 'Dell']
#manufacturer_Dell_avg_price = manufacturer_Dell['price_euros'].mean(axis=0)
#LENOVO
#manufacturer_Lenovo = laptops[laptops['manufacturer'] == 'Lenovo']
#manufacturer_Lenovo_avg_price = manufacturer_Lenovo['price_euros'].mean(axis=0)
#HP
#manufacturer_HP = laptops[laptops['manufacturer'] == 'HP']
#manufacturer_HP_avg_price = manufacturer_HP['price_euros'].mean(axis=0)
#Asus
#manufacturer_ASUS = laptops[laptops['manufacturer'] == 'Asus']
#manufacturer_ASUS_avg_price = manufacturer_ASUS['price_euros'].mean(axis=0)
#Accer
#manufacturer_Accer = laptops[laptops['manufacturer'] == 'Accer']
#manufacturer_Accer_avg_price = manufacturer_Accer['price_euros'].mean(axis=0)
#MSI
#manufacturer_MSI = laptops[laptops['manufacturer'] == 'MSI']
#manufacturer_MSI_avg_price = manufacturer_MSI['price_euros'].mean(axis=0)
#Toshiba
#manufacturer_Toshiba = laptops[laptops['manufacturer'] == 'Toshiba']
#manufacturer_Toshiba_avg_price = manufacturer_Toshiba['price_euros'].mean(axis=0)
#Apple
#manufacturer_Apple = laptops[laptops['manufacturer'] == 'Apple']
#manufacturer_Apple_avg_price = manufacturer_Apple['price_euros'].mean(axis=0)
                                  
# What is the best value laptop with a screen size of 15" or more?
#TOP_screen_size = laptops[laptops['screen_size_inches'] >= 15]
#TOP_screen_size_price = TOP_screen_size['price_euros'].min()
#TOP_screen_size_price_RESULT = laptops[laptops['price_euros'] == 199]
                                                           
# Which laptop has the most storage space?
storage_desc = laptops['storage'].describe()
price_euros = laptops['price_euros'].describe()
TOP_storage = laptops[laptops['storage'] == '256GB SSD'].iloc[:,:2]

#umsetequatro = laptops[laptops['price_euros'] == 174]
#umsetequatroZERO = laptops[laptops['price_euros'] == 174.0]



manufacturer_price = laptops[['manufacturer', 'price_euros']]

laptops_dif = pd.read_csv('laptops.csv', encoding='Latin-1', index_col=0)

Apple_HP = laptops_dif.loc[['Apple', 'HP'], ['Price (Euros)']]

## 12. Challenge: Clean a String Column ##

laptops['weight'] = laptops['weight'].str.replace('kg', '').str.replace('s','').astype(float)

laptops.rename(columns={'weight': 'weight_kg'}, inplace=True)

# Para salvar o ficheiro limpo para um novo ficheiro usamos o metodo to_csv(). Por defeito o pandas vai guardar as etiquetas dos indexes como uma coluna. No entanto, aqui n interessa, pq o nosso index é composto por integers, q n têm qq data/info. Por isso não salvamos(index=False):
laptops.to_csv('laptops_cleaned.csv', index=False)


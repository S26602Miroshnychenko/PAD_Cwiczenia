import pandas as pd

df = pd.read_csv('PAD_03_PD.csv', delimiter=';', index_col='ID')

# Zad 1
df['Country'].value_counts()

# Zad 2
df['owned_goods'] = df['owns_car']+df['owns_TV']+df['owns_house']+df['owns_Phone']

# Zad 3
men_mean = round(df[df['gender'] == "M"]['owned_goods'].mean(), 2)
women_mean = round(df[df['gender'] == "K"]['owned_goods'].mean(), 2)

#Zad 4
df2=df.dropna(how='all')
dfzad4 = round(df2.groupby(['Country'])[['owned_goods']].mean(), 2)
dfzad4['min_age'] = df2.groupby(['Country'])[['Age']].min()


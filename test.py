import pandas as pd
import numpy as np
from pickle import TRUE
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None

movies_df = pd.read_csv('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Documents/GitHub/CSW_WEEK8/CSW_WEEK8-1/rotten_tomatoes_movies.csv')


movies_df['Studio'] = movies_df['production_company'].str.split(' ').str[0]


count = movies_df['Studio'].value_counts()[:10]

top_Studio = list(count.index)

movie_Studio_df = movies_df[movies_df['Studio'].isin(top_Studio)]

plt.figure(figsize=(15, 10))

sns.set_style("whitegrid")
sns.boxplot(x='Studio', y='tomatometer_rating', data=movie_Studio_df)
plt.xlabel("Studio names",fontsize=10)
plt.ylabel("TomatoMeter Rating",fontsize=10)
plt.title("Boxplot of TomatoMeter rating per Studio ", fontsize=15)
plt.show()

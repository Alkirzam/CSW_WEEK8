import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

movies_df = pd.read_csv('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Documents/GitHub/Coursework/Coursework/data.csv')





def Distribution_of_Studio_names_BY_Ali():
 movies_df = pd.read_csv('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Documents/GitHub/Coursework/Coursework/data.csv')
 movies_df['Studio'] = movies_df['production_company'].str.split(' ').str[0]

 a = plt.cm.Wistia

 plt.figure(figsize=(10,5))
 count = movies_df['production_company'].value_counts()[:7]
 sns.barplot(count.values, count.index, palette=[a(0.1),a(0.2),a(0.3),a(0.4),a(0.5),a(0.6),a(0.7),a(0.8),a(0.9),a(0.99)])
 for i, v in enumerate(count.values):
     plt.text(10.0,i,v,color='k',fontsize=10)
 plt.xlabel('Count', fontsize=10)
 plt.ylabel('Studio name', fontsize=10)
 plt.title("Distribution of Studio names", fontsize=15)
 plt.show()
 
 
def TomatoMeter_rating_per_Studio_BY_Ali():
 movies_df = pd.read_csv('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Documents/GitHub/Coursework/Coursework/data.csv')
 movies_df['Studio'] = movies_df['production_company'].str.split(' ').str[0]
 
 count = movies_df['Studio'].value_counts()[:7]
 top_Studio = list(count.index)
 movie_Studio_df = movies_df[movies_df['Studio'].isin(top_Studio)]

 plt.figure(figsize=(15, 10))
 sns.set_style("whitegrid")
 sns.boxplot(x='Studio', y='tomatometer_rating', data=movie_Studio_df)
 plt.xlabel("Studio names",fontsize=10)
 plt.ylabel("TomatoMeter Rating",fontsize=10)
 plt.title("Boxplot of TomatoMeter rating per Studio ", fontsize=15)
 plt.show()
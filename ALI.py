import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


movies_df = pd.read_csv('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Documents/GitHub/Coursework/Coursework/data.csv')

movies_df.head(5)



def Distribution_of_Studio_names():
 movies_df = pd.read_csv('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Documents/GitHub/Coursework/Coursework/data.csv')

 a = plt.cm.Wistia

 plt.figure(figsize=(20,5))
 count = movies_df['production_company'].value_counts()[:10]
 sns.barplot(count.values, count.index, palette=[a(0.1),a(0.2),a(0.3),a(0.4),a(0.5),a(0.6),a(0.7),a(0.8),a(0.9),a(0.99)])
 for i, v in enumerate(count.values):
     plt.text(10.0,i,v,color='k',fontsize=10)
 plt.xlabel('Count Movies', fontsize=10)
 plt.ylabel('Studio name', fontsize=10)
 plt.title("Distribution of Studio names", fontsize=15)
 plt.show()
 
 
def Boxplot_of_TomatoMeter_rating_per_Studio():
 movies_df = pd.read_csv('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Documents/GitHub/Coursework/Coursework/data.csv')

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

 
def Movies_by_the_year():
 movies_df = pd.read_csv('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Documents/GitHub/Coursework/Coursework/data.csv')

    
 movies_df = movies_df[movies_df.original_release_date.notnull()]
 movies_df['original_release_date'] = pd.to_datetime(movies_df['original_release_date'])
 movies_df['movie_year'] = movies_df['original_release_date'].apply(lambda x: x.year)
 

 plt.figure(figsize=(10,5))
 plt.title('Movies by the year', size=20)
 sns.distplot(movies_df.movie_year, kde=False)
 plt.ylabel('Number of movies', size=15)
 plt.xlabel('Year of release',size=15)
 plt.axis([1920, 2019, 0, 1750])
 plt.xticks(np.arange(1920, 2018, step=5),rotation=45, ha='right')
 plt.show()
 
 
def Distribution_of_Studio_Genres():
 movies_df = pd.read_csv('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Documents/GitHub/Coursework/Coursework/data.csv')
 
 movies_df['first_genre'] = movies_df['genres'].str.split(',').str[0]

 a = plt.cm.cool

 plt.figure(figsize=(15,10))
 count = movies_df['first_genre'].value_counts()[:7]
 sns.barplot(count.values, count.index, palette=[a(0.1),a(0.2),a(0.3),a(0.4),a(0.5),a(0.6),a(0.7)])
 for i, v in enumerate(count.values):
    plt.text(0.8,i,v,color='k',fontsize=14)
 plt.xlabel('Count', fontsize=12)
 plt.ylabel('Genre name', fontsize=12)
 plt.title("Distribution of Genres", fontsize=16)
 plt.show()
 
 

print('Enter 1 for Distribution of Studio names')
print('Enter 2 Boxplot of TomatoMeter rating per Studio')

print('Enter 3 for Movies by the year')
print('Enter 4 for Distribution of Genres')

src= int(input('Select option'))


while src not in [1, 2, 3, 4] :
    src=int(input('Invalid option please enter another here: '))
    

if  src==1:
    Distribution_of_Studio_names()
elif src ==2:
    Boxplot_of_TomatoMeter_rating_per_Studio()
elif src==3:
    Movies_by_the_year()
elif src==4:
     Distribution_of_Studio_Genres()

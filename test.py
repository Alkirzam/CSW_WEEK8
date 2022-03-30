import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

movies_df = pd.read_csv('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Documents/GitHub/CSW_WEEK8/CSW_WEEK8-1/rotten_tomatoes_movies.csv')

<<<<<<< HEAD


def Audience_rating_per_Genre():
 movies_df = pd.read_csv('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Documents/GitHub/CSW_WEEK8/CSW_WEEK8-1/rotten_tomatoes_movies.csv')

    
 movies_df['Studio'] = movies_df['production_company'].str.split(' ').str[0]

 count = movies_df['Studio'].value_counts()[:10]
 top_Studio = list(count.index)
 movie_Studio_df = movies_df[movies_df['Studio'].isin(top_Studio)]

 plt.figure(figsize=(10, 5))
 sns.set_style("whitegrid")
 sns.boxplot(x='Studio', y='tomatometer_rating', data=movie_Studio_df)
 plt.xlabel("Studio names",fontsize=10)
 plt.ylabel("TomatoMeter Rating",fontsize=10)
 plt.title("Boxplot of TomatoMeter rating per Studio ", fontsize=15)
 plt.show()




def Distribution_of_Studio_names():
    
 movies_df = pd.read_csv('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Documents/GitHub/CSW_WEEK8/CSW_WEEK8-1/rotten_tomatoes_movies.csv')

 a = plt.cm.Wistia

 plt.figure(figsize=(10,5))
 
 count = movies_df['production_company'].value_counts()[:8]
 sns.barplot(count.values, count.index, palette=[a(0.1),a(0.2),a(0.3),a(0.4),a(0.5),a(0.6),a(0.7),a(0.8),a(0.9),a(0.99)])
 for i, v in enumerate(count.values):
     plt.text(10.0,i,v,color='k',fontsize=10)
 plt.xlabel('Count', fontsize=10)
 plt.ylabel('Studio name', fontsize=10)
 plt.title("Distribution of Studio names", fontsize=15)
 plt.show()
 
 
 
print('Enter 1 for Distribution of Studio names')
print('Enter 2 Boxplot of TomatoMeter rating per Studio')
src= int(input('Select option'))

while src not in [1, 2] :
    src=int(input('Invalid option please enter another here: '))

if  src==1:
    Distribution_of_Studio_names()

elif src==2:
    Audience_rating_per_Genre()
=======
movies_df['genre'] = movies_df['genres'].str.split(',').str[0]
count = movies_df['genre'].value_counts()[:7]



top_genres = list(count.index)
movie_genres_df = movies_df[movies_df['genre'].isin(top_genres)]
plt.figure(figsize=(15, 10))
sns.boxplot(x='genre', y='audience_rating', data=movie_genres_df)
plt.xlabel("Genre Name",fontsize=12)
plt.ylabel("Audience Rating",fontsize=12)
plt.title("Boxplot of Audience rating per Genre", fontsize=16)
plt.show()
>>>>>>> 7a5569d2d9eb4c1b1d6f3bfb0254ae62b1e366e3

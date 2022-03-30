import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

csv_df = pd.read_csv('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Documents/GitHub/CSW_WEEK8/CSW_WEEK8-1/rotten_tomatoes_movies.csv')



def Audience_rating_per_Genre():
 csv_df = pd.read_csv('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Documents/GitHub/CSW_WEEK8/CSW_WEEK8-1/rotten_tomatoes_movies.csv')

    
 csv_df['genre'] = csv_df['genres'].str.split(' ').str[0]

 count = csv_df['genre'].value_counts()[:8]
 top_genre = list(count.index)
 movie_genre_df = csv_df[csv_df['genre'].isin(top_genre)]

 plt.figure(figsize=(10, 5))
 sns.set_style("whitegrid")
 sns.boxplot(x='genre', y='tomatometer_rating', data=movie_genre_df)
 plt.xlabel("genre names",fontsize=10)
 plt.ylabel("TomatoMeter Rating",fontsize=10)
 plt.title("Boxplot of TomatoMeter rating per genre ", fontsize=15)
 plt.show()




def Distribution_of_Studio_names():
    
 movies_df = pd.read_csv('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Documents/GitHub/CSW_WEEK8/CSW_WEEK8-1/rotten_tomatoes_movies.csv')
 movies_df['genre'] = movies_df['genres'].str.split(' ').str[0]

 a = plt.cm.Wistia

 plt.figure(figsize=(10,5))
 
 count = movies_df['genre'].value_counts()[:10]
 sns.barplot(count.values, count.index, palette=[a(0.1),a(0.2),a(0.3),a(0.4),a(0.5),a(0.6),a(0.7),a(0.8),a(0.9),a(0.99)])
 for i, v in enumerate(count.values):
     plt.text(10.0,i,v,color='k',fontsize=10)
 plt.xlabel('Count', fontsize=10)
 plt.ylabel('genre name', fontsize=10)
 plt.title("Distribution of genre names", fontsize=15)
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
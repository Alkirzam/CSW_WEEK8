import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

movies_df = pd.read_csv('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Documents/GitHub/CSW_WEEK8/CSW_WEEK8-1/rotten_tomatoes_movies.csv')

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
import pandas as pd
import numpy as np
import seaborn as sns
import re
sns.set_theme(style="dark")
from plotly.offline import init_notebook_mode,iplot
import matplotlib as mpl
import matplotlib.pyplot as plt
from subprocess import check_output
from wordcloud import WordCloud, STOPWORDS
init_notebook_mode(connected=True)
pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None

movies_df = pd.read_csv('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Documents/GitHub/Coursework/Coursework/data.csv')

movies_df.head(5)

def Movies_by_the_year():
 movies_df = pd.read_csv('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Documents/GitHub/Coursework/Coursework/data.csv')

    
 movies_df = movies_df[movies_df.original_release_date.notnull()]
 movies_df['original_release_date'] = pd.to_datetime(movies_df['original_release_date'])
 movies_df['movie_year'] = movies_df['original_release_date'].apply(lambda x: x.year)
 
 sns.set(style="white")

 plt.figure(figsize=(10,5))
 plt.title('Movies by the year', size=20)
 sns.distplot(movies_df.movie_year, kde=False)
 plt.ylabel('Number of movies', size=15)
 plt.xlabel('Year of release',size=15)
 plt.axis([1920, 2019, 0, 1750])
 plt.xticks(np.arange(1920, 2018, step=5),rotation=45, ha='right')
 plt.show()
 

def Distribution_of_Studio_names():
 movies_df = pd.read_csv('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Documents/GitHub/Coursework/Coursework/data.csv')

 a = plt.cm.cool

 plt.figure(figsize=(10,5))
 count = movies_df['production_company'].value_counts()[:10]
 sns.barplot(count.values, count.index, palette=[a(0.1),a(0.2),a(0.3),a(0.4),a(0.5),a(0.6),a(0.7),a(0.8),a(0.9),a(0.99)])
 for i, v in enumerate(count.values):
     plt.text(0.8,i,v,color='k',fontsize=14)
 plt.xlabel('Count', fontsize=12)
 plt.ylabel('Studio name', fontsize=12)
 plt.title("Distribution of Studio names", fontsize=16)
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
 
 


print('Enter 1 for Movies by the year')
print('Enter 2 for Distribution of Studio_names')
print('Enter 3 for Distribution of Genres')


src=int(input('Enter here: '))

if src==1:
    Movies_by_the_year()
elif src==2:
    Distribution_of_Studio_names()
elif src==3:
     Distribution_of_Studio_Genres()

else:
    print('Sorry, invalid')
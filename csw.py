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

movies_df = pd.read_csv('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Documents/GitHub/CSW_WEEK8/CSW_WEEK8/rotten_tomatoes_movies.csv')
reviews_df = pd.read_csv('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Documents/GitHub/CSW_WEEK8/CSW_WEEK8/rotten_tomatoes_critic_reviews.csv')
movies_df.head(5)
reviews_df.head(5)


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


reviews_df = reviews_df[reviews_df.review_date.notnull()]
reviews_df['review_date'] = pd.to_datetime(reviews_df['review_date'])
reviews_df['review_year'] = reviews_df['review_date'].apply(lambda x: x.year)
reviews_df = reviews_df[reviews_df.review_year.astype(int) >= 2000]

plt.figure(figsize=(10,5))
plt.title('Reviews by the year', size=20)
sns.distplot(reviews_df.review_year, bins=20, kde=False)
plt.ylabel('Number of critic reviews', size=15)
plt.xlabel('Year of review posted',size=15)
plt.axis([2000, 2019, 0, 75000])
plt.xticks(np.arange(2000, 2019, step=1),rotation=45, ha='right')
plt.show()

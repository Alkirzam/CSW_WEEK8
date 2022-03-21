import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from subprocess import check_output
pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None


movies_df = pd.read_csv('data.csv')

movies_df = movies_df[movies_df.original_release_date.notnull()]
movies_df['original_release_date'] = pd.to_datetime(movies_df['original_release_date'])
movies_df['movie_year'] = movies_df['original_release_date'].apply(lambda x: x.year)

sns.set(style="white")

plt.figure(figsize=(15,10))
plt.title('Movies by the year', size=20)
sns.distplot(movies_df.movie_year, kde=False)
plt.ylabel('Number of movies', size=15)
plt.xlabel('Year of release',size=15)
plt.axis([1920, 2019, 0, 1750])
plt.xticks(np.arange(1920, 2018, step=5),rotation=45, ha='right')
plt.show()
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None

reviews_df = pd.read_csv('reviews.csv')


reviews_df = reviews_df[reviews_df.review_date.notnull()]
reviews_df['review_date'] = pd.to_datetime(reviews_df['review_date'])
reviews_df['review_year'] = reviews_df['review_date'].apply(lambda x: x.year)
reviews_df = reviews_df[reviews_df.review_year.astype(int) >= 2000]

plt.figure(figsize=(15,10))
plt.title('Reviews by the year', size=20)
sns.distplot(reviews_df.review_year, bins=20, kde=False)
plt.ylabel('Number of critic reviews', size=15)
plt.xlabel('Year of review posted',size=15)
plt.axis([2000, 2019, 0, 75000])
plt.xticks(np.arange(2000, 2019, step=1),rotation=45, ha='right')
plt.show()
plt.show()

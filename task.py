import csv
import pandas as pd

df = pd.read_csv('data2.csv', sep = '|')
#compare the average view count for 2 genres

#genre_1 =input('input 1st genre')
g1cf =df[(df['genres']=='Comedy')&(df['tomatometer_status']=='Certified-Fresh')]
g1cfl =len(g1cf)
g1 =df[(df['genres']=='Comedy')]
g1l =len(g1)
average =100*float(g1cfl)/float(g1l)
print('percentage of cf in comedy is: '& 100*float(g1cfl)/float(g1l))

#g1l =len(g1)
#g1vc = 


#genre_2 =input('input 2nd genre')
#day =df[(df['genre']==genre_2)]

#average_g1 =
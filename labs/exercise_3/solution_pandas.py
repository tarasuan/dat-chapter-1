import pandas as pd
movies_df = pd.read_csv('/Users/tarasuan/Desktop/rock.csv')

# print movies_df.dtypes
# print movies_df.head()

# Important: have not dealt with dupes

movies_by_year_df = movies_df[movies_df.ReleaseYear == "1981"]
print movies_by_year_df.count 

movies_by_playcount_df = movies_df.sort('PlayCount', ascending=False)
print movies_by_playcount_df.head(10)
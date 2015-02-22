import pandas as pd
movies = pd.read_csv('/Users/tarasuan/Desktop/rock.csv')

# Important: have not dealt with dupes
movies_1981 = movies[movies["Release Year"] == "1981"]

print movies_1981.count 

movies_by_playcount = movies.sort('PlayCount', ascending=False)
print movies_by_playcount.head(20)
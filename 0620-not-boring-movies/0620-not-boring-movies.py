import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
     cinema = cinema.sort_values('rating', ascending=False)
     return cinema[(cinema['id']%2!=0) & (cinema['description']!='boring')]
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views = views.rename(columns={'author_id':'id'})
    df=views[views['id']==views['viewer_id']]
    df = df.sort_values('id')
    return df[['id']].drop_duplicates(subset=['id'])
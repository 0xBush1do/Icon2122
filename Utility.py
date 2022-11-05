import pandas as pd
from fuzzywuzzy import process

def filter_by_category(df_m, category):
    category_list = process.extract(category, df_m['genres'].tolist())
    for c in category_list:
        df_m_filtered = df_m.query("genres == '"+c[0]+"'")
    return df_m_filtered

def filter_ratings(df_r, df_movie_c):
    return df_r.join(df_movie_c.set_index('movieId'), on='movieId').dropna().drop(['title', 'genres'], axis=1)

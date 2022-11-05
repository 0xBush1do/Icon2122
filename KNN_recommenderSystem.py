import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from surprise.model_selection import cross_validate
from surprise import KNNWithMeans
from surprise import Dataset, Reader

def showInfo(df, column):
    pd.set_option('display.float_format', lambda x: '%.3f' % x)
    print(df[column].describe())

def filterByThreshold(df, column, threshold):
    return df.query(column+" >= @threshold")

def preprocess_data(movies, ratings):
    print("<+> Effettuo il preprocessing dei dati <+>")
    df = pd.merge(ratings, movies, on='movieId')
    print("<+> Effettuato il merge dei dataframes: ratings e movies <+>")
    #print(df.head())
    #creazione di un dataframe che comprende tutte le recensioni degli utenti sui singoli film
    combine_m_r = df.dropna(axis=0, subset=['title'])
    movie_rCount = (combine_m_r.groupby(by=['title'])['rating'].count().reset_index().rename(columns={'rating': 'RatingCount'})[['title', 'RatingCount']])
    total_rCount = combine_m_r.merge(movie_rCount, left_on='title', right_on='title', how='left')
    #print("<+> Visualizzo il numero totale di recensioni per ogni film <+>")
    #print(total_rCount.head())
    popular_movies = filterByThreshold(total_rCount, 'RatingCount', 50)
    print("<+> Filtro i film in base al numero di recensioni per ottenere quelli più popolari <+>")
    #print(popular_movies.head())
    return popular_movies

def getMoviesFeatures(df, index, columns, values):
    return df.pivot_table(index=index, columns=columns, values=values).fillna(0)

def recommendMovie(movies, ratings, n_neigh):
    popular_movies = preprocess_data(movies, ratings)
    if len(popular_movies) > 0:
        popular_movies_features = getMoviesFeatures(popular_movies, index='title', columns='userId', values='rating')
        n_rows = popular_movies_features.shape[0]
        popular_movies_matrix = csr_matrix(popular_movies_features.values)
        knn = NearestNeighbors(metric='cosine', algorithm='auto', n_neighbors=20)
        knn.fit(popular_movies_matrix)
        #prendo l'indice di un film casuale
        idx = np.random.choice(popular_movies_features.shape[0])
        #effettuo la predizione
        if n_rows > n_neigh:
            distances, indices = knn.kneighbors(popular_movies_features.iloc[idx,:].values.reshape(1, -1), n_neighbors=n_neigh)
        else:
            distances, indices = knn.kneighbors(popular_movies_features.iloc[idx, :].values.reshape(1, -1), n_neighbors=n_rows-1)
    else:
        return [], [], []
    return indices, distances, popular_movies_features

def showResults(i, d, movie_f):
    for idx in range(0, len(d.flatten())):
        if idx != 0:
            print("{0}: {1}, con distanza: {2}".format(idx, movie_f.index[i.flatten()[idx]], d.flatten()[idx]))

def showMetricsAndBM(df):
    rdf = Reader(rating_scale=(0,5))
    data = Dataset.load_from_df(df, reader=rdf)
    options = {"name":"cosine", "user_based":False}
    algo = KNNWithMeans(k = 5, sim_options=options)
    cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
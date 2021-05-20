"""This module returns plot based recommendations."""
from load_data import metadata
import numpy as np
import pandas as pd


similarity_matrix = np.memmap("similarity_data.dat", dtype=np.float64, mode="r", shape=(45466, 45466))

indices = pd.Series(metadata.index, index=metadata["title"]).drop_duplicates()

def get_recommendations(title, cosine_sim=similarity_matrix):


    idx = indices[title]

    # List the pairwsie similarity scores
    similarity_scores = list(enumerate(cosine_sim[idx]))

    # Sort acccording to similarity scores
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # 10 the most similar movies
    similarity_scores = similarity_scores[1:11]
    
    # for el in similarity_scores:
    #    print(el)

    movie_indices = [i[0] for i in similarity_scores]

    return metadata["title"].iloc[movie_indices]
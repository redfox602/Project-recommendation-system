"""This is a module which create a similarity dataset base on plot"""
from load_data import metadata
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
import numpy as np


plot = metadata["overview"]

tfidf = TfidfVectorizer(stop_words="english")

plot = plot.fillna("")

tfidf_matrix = tfidf.fit_transform(plot)


similarity_data = np.memmap("similarity_data.dat", dtype=np.float64, 
                                mode="w+", shape=(tfidf_matrix.shape[0] , 
                                tfidf_matrix.shape[0]))

i = 0
while i < tfidf_matrix.shape[0]:
    j = (i + 500) % tfidf_matrix.shape[0]
    if j > tfidf_matrix.shape[0]:
        break
    else:
        print("Processed: ", i)
        similarity_data[i:j+i, i:j+i] = linear_kernel(tfidf_matrix[i:i+j], tfidf_matrix[i:i+j])
    i += 500



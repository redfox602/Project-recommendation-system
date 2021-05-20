"""This is a module which generate a easy/ basic system recommendations."""

from load_data import metadata
import numpy as np

#Calculate the mean votes acreoss all movies
C = metadata["vote_average"].mean()
#print(C)

#Calculate the minimum nuber of votes which get in
m = metadata["vote_count"].quantile(0.90)
#print(m)

#Filter out all movies which haven't more votes than at least 75%
movies = metadata.copy().loc[metadata["vote_count"] >= m]
#print(movies.shape)
#print(metadata.shape)

def weighted_rating(movie):
    """Return the weighted rating"""
    global C, m
    #Number of votes for the movie
    v = movie["vote_count"]
    #The average rating of the movie
    R = movie["vote_average"]
    return ((R * v + C * m) / (v + m))

#Define a new feature my_score which calculeted weighted rating
movies["my_score"] = movies.apply(weighted_rating, axis=1)

movies = movies.sort_values("my_score", ascending=False)

result = movies[["title", "vote_count", "vote_average", "my_score"]]

#print(result.head(20))

top = []
for el in result["title"]:
    top.append(str(el))
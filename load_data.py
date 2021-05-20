"""Load all nessecery data."""

import pandas as pd

metadata = pd.read_csv("data/movies_metadata.csv", low_memory=False)
# print(metadata.head(3))
#print("Load metadata\n")

#credits = pd.read_csv("data/credits.csv", low_memory=False)
# print(credits.head(3))
#print("Load credits\n")
#
#keywords = pd.read_csv("data/keywords.csv", low_memory=False)
# print(keywords.head(3))
#print("Load keywords\n")
#
#ratings_small = pd.read_csv("data/ratings_small.csv", low_memory=False)
# print(ratings_small.head(3))
#print("Load ratings_small\n")
#
#ratings = pd.read_csv("data/ratings.csv", low_memory=False)
# print(ratings.head(3))
#print("Load ratings\n")
#
#links = pd.read_csv("data/links.csv", low_memory=False)
# print(links.head(3))
#print("Load links\n")
#
#links_small = pd.read_csv("data/links_small.csv", low_memory=False)
# print(links_small.head(3))
#print("Load links_small\n")
#

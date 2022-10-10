# Run this script from the repository's root.

import os
import pandas as pd
top200_movies_file = os.path.join('src', 'data', 'Top_200_Movies.csv')

def get_movies_data():
    return pd.read_csv(top200_movies_file)

def get_movies_interval(y1, y2):
    if y2 < y1: raise ValueError
    data = get_movies_data()
    return data[(data['Year of Release'] >= y1) & (data['Year of Release'] <= y2)]['Title']

def get_rating_popularity_stats(index, type):
    if index != "Rating" and index != "Popularity Index": return "Invalid index or type" 
    data = get_movies_data()
    match type:
        case "count": #This case seems really useless?
            return "{0:.2f}".format(data[index].astype("string").str.replace(",","").astype("float").count())
        case "mean":
            return "{0:.2f}".format(data[index].astype("string").str.replace(",","").astype("float").mean())
        case "median":
            return "{0:.2f}".format(data[index].astype("string").str.replace(",","").astype("float").median())
        case "min":
            return "{0:.2f}".format(data[index].astype("string").str.replace(",","").astype("float").min())
        case "max": 
            return "{0:.2f}".format(data[index].astype("string").str.replace(",","").astype("float").max())
        case _:
            return "Invalid index or type" 

def get_actor_movies_release_year_range(actor, upper, lower=0):
    if upper < lower: raise ValueError
    if not isinstance(actor, str) or not isinstance(upper, int) or not isinstance(lower, int): raise TypeError
    if actor == "": raise ValueError
    data = get_movies_data()
    #First filters out movies in the year range
    data = data[(data['Year of Release'] >= lower) & (data['Year of Release'] <= upper)]
    #Then filters by actor name, selecting columns "Title" and "Year of Release". 
    #Sets the index to "Title", turns it into a Series and then clears Series names.
    return data[data["Movie Cast"].str.contains(actor,regex=False)][["Title", "Year of Release"]].set_index("Title").squeeze().rename_axis(None).rename(None)

def get_actor_median_rating(actor):
    if not isinstance(actor, str): raise TypeError
    if actor == "": raise ValueError
    data = get_movies_data()
    #If there are no True values in this df, return None
    if data["Movie Cast"].str.contains(actor, regex=False).sum() == 0: return None
    #Else return the median.
    return data[data["Movie Cast"].str.contains(actor, regex=False)]["Rating"].median()

def get_directors_median_reviews():
    data = get_movies_data()
    data2 = data[["Number of Reviews", "Director"]]
    #Parse the "Number of Reviews" column and change it to be in millions. 
    data2["Number of Reviews"] = data2["Number of Reviews"].transform(lambda x: x[0:-1] if x[-1] == "M" else str(float(x[0:-1])/1000))
    #Groupby "Director" and get median, squeeze to series, wipe column name.
    return data2.groupby("Director").median().squeeze().rename(None)


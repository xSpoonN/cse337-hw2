# Run this script from the repository's root.
from re import A
import numpy as np

def replaceMissingValues(x):
    return np.nan_to_num(x)

def countMissingValues(x, k=0):
    try:
        return np.sum(np.isnan(x),axis=k)
    except (np.AxisError, TypeError): raise ValueError

def exams_with_median_gt_K(x, k):
    if k < 0 or k > 100: raise ValueError
    if not isinstance(k, int): raise TypeError
    y = replaceMissingValues(x)
    if np.max(y) > 100 or np.min(y) < 0: raise ValueError
    return np.sum(np.median(y, axis=1) > k) #Sum of the number of rows that have median > k

def curve_low_scoring_exams(x, k):
    if k < 0 or k > 100: raise ValueError
    y = replaceMissingValues(x)
    if np.max(y) > 100 or np.min(y) < 0: raise ValueError
    if not isinstance(k, int): raise TypeError
    #(1) Replace NaN with 0s. (2) Take the max of each row. (3) Reshape it to (4,1). 
    #(4) Subtract it from 100 to get the weight points. (5) Multiply by the filter to zero out means >= k
    weight = np.reshape(np.mean(y,axis=1) < k,(4,1)) * np.reshape(100-np.max(y, axis=1), (4,1))
    #(6) Add it to the original array to get weighted scores.
    weightedScores = y+weight
    #(7) Sort by indices from calling argsort on the mean of the array. (8) Round to 1st decimal place.
    return np.round(weightedScores[np.argsort(np.mean(weightedScores,axis=1))],decimals=1)

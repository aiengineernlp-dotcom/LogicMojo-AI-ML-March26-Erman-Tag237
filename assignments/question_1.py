# Q1. Understanding Feature Distributions (Iris Dataset)

import seaborn as sns
import numpy as np
import pandas as pd

# print(data.head())
# print(type(data))
data = sns.load_dataset("iris")  # initial data iris
data_colums = data.columns

def extract_feature(data: pd.DataFrame) -> np.ndarray:
    """
    This function extract features matrix as numpy array.

    Args:
        - data : dataset Iris imported form seaborn

    Returns:
        - features converted to numpy array

    Errors:
        - Raise DataNotFoundError

    """
    if data is not None:
        try:
            data_arr = np.array(data)
            # mean = data.iloc[:,:-1].values
        except Exception as e:
            raise ValueError(f"Need data {e}")
    return data_arr


# TEST

r = extract_feature(data)
print(type(r))
print(r.shape)
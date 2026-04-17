# Q1. Understanding Feature Distributions (Iris Dataset)

import seaborn as sns
import numpy as np
import pandas as pd

# print(data.head())
# print(type(data))
data = sns.load_dataset("iris")  # initial data load from seaborn
data_colums = data.columns


def extract_features(data: pd.DataFrame) -> np.ndarray:
    """
    This function extract features matrix as numpy array.

    Args:
        - data : dataset Iris imported form seaborn

    Returns:
        - features converted to numpy array

    Errors:
        - Raise DataNotFoundError
        - ValueError

    """
    if data is not None:
        #
        try:
            data_arr = np.array(data)
        except Exception as e:
            raise ValueError(f"Need data for to convert matrix to numpy array {e}")

    # Computations
    numeric_data = data.select_dtypes(include=[
        np.number])  # je recupère uniquement les colonnes numeriques. ici "species" est eliminer directement du calcul
    numeric_data_cols = numeric_data.columns.tolist() # On récupère les noms des colonnes pour savoir ce qu'on manipule
    # mean
    mean_data_arr = np.mean(numeric_data, )
    # Median
    median_data_arr = np.median(numeric_data, )
    # Standarddeviation
    std_data_arr = np.std(
        numeric_data, )  # np.std(numeric_data).sum()  🚩 do we need separatly for each feature or sum() them ?
    # Variance
    var_data_arr = np.var(numeric_data, )
    # Convert one feature to shape (n,1)
    data_arr_sepal_width = data["sepal_width"].values.reshape(-1, 1)
    return data_arr, mean_data_arr, median_data_arr, std_data_arr, var_data_arr, data_arr_sepal_width

data_arr, mean_data_arr, median_data_arr, std_data_arr, var_data_arr, data_arr_sepal_width = extract_features(data)
print(f"{"█" * 70} TEST RESULTS {"█" * 55}")
print(data)
print(f" Extract feature matrix as NumPy array:")
print(f'{'-' * 50}')
print(f"{data_arr}\n")
# ====================
print(f" Computations:")
print(f'{'-' * 50}')
print(f" Mean:  {mean_data_arr:.2f}\n")
# ====================
print(f'{'-' * 50}')
print(f" MeDian:  {median_data_arr:.2f}\n")
# ====================
print(f'{'-' * 50}')
print(f" Standarddeviation:\n{std_data_arr}\n")
# ====================
print(f'{'-' * 50}')
print(f" Variance:\n{var_data_arr}")

print("\n========Curent type======")
# print(type(r))
print(type(data))
print(f"{"█" * 70} ANALYSIS {"█" * 60}")
print("Which feature has highest variability and why it matters in ML")
print(
    " ==>> Base on Standarddeviation and Variance,  sepal_length has the highest variability. It matters in ML because the help us to know if they are extremes values on our data. Also the model can thing that somme values are more importants than others just because of highs numbers ")
print("Convert any one feature into shape (n,1) and explain why ML models expect this format")
print(data_arr_sepal_width)


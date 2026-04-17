import numpy as np
import pandas as pd
import seaborn as sns

data = sns.load_dataset("iris")

def standardization(data:pd.DataFrame)->float:
    """
    this function standartuze the dataset iris
    Args:
        - data:  Full dataset iris
        -
    Returns:
        - float : the mean must be type of float since the matrix are float as weel
        - mean must be 0 or less
        - std for each feature  must be 1
    """
    if data is not None:
        try:
            matrix = np.array(data)
            col_numeric = data.select_dtypes(include=[np.number]) # I retrieve only numeric columns form my dataset
            num_data_columns = col_numeric.columns.to_list() # I list my columns in other to know who are they
        except Exception as e:
            raise ValueError("Need data to continue")
        #mean
        mean_matrix = np.mean(col_numeric)
        #std
        std_matrix = np.std(col_numeric)
        #normalization
        norm = (col_numeric -mean_matrix )/std_matrix
        norm_mean = norm.mean()
        norm_std = norm.std()

    return norm_mean,norm_std


norm_mean,norm_std= standardization(data)

print(f"{'▇' * 70} TEST RESULTS {'▇' * 55}")
print(f"Apply standardization: :\n{'-' * 50} \n", data)
print(f'{'=' * 50}')
print(f"{'▇' * 70} VERIFICATIONS {'▇' * 55}")
#====================
print(f"{'MEAN = 0 and STD for each feature = 1'}\n{'-' * 50}")
print(f"MEAN:'{round(norm_mean.sum(),4)}\n{'-'*50}")
print(f"Std:'\n{norm_std}\n{'-'*50}")
print(f'{'=' * 50}')


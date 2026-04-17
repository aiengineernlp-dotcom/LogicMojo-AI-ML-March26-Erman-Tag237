import pandas as pd
import numpy as np
import seaborn as sns

data = sns.load_dataset("titanic")


def datasetUnderstanding(data: pd.DataFrame) -> pd.DataFrame:
    #
    # """

    #--> to add here

    # :param data:
    # :return:
    # """
    # if:
    #     try:
    #     except:
    #         raise
    #
    dfr = pd.DataFrame(data)
    # 1- Display head(), tail(),info(), describe()
    dfr_h = dfr.head()
    dfr_t = dfr.tail()
    dfr_i = dfr.info()
    dfr_d = dfr.describe()
    # 2. Identify missing values per columns
    missing_col = dfr.isnull().sum()
    # Numerical vs categorical features
    numercial_features = data.select_dtypes(include=[np.number])
    categorical_features = data.select_dtypes(exclude=[np.number])
    return dfr_h, dfr_t, dfr_d, dfr_i, categorical_features, numercial_features, missing_col


dfr_h, dfr_t, dfr_d, dfr_i, categorical_features, numercial_features, missing_col = datasetUnderstanding(data)

print(f"{'▇' * 70} TEST RESULTS {'▇' * 55}")
print(f" dfr  head :\n{'-' * 50} \n", dfr_h)
print(f" dfr tail :\n{'-' * 50} \n", dfr_t)
print(f" dfr infos :\n{'-' * 50} \n", dfr_i)
print(f"  missing col :\n{'-' * 50} \n", missing_col)
print(f" dfr describe :\n{'-' * 50} \n", dfr_d)
print(f" numercial features :\n{'-' * 50} \n", numercial_features)
print(f" categorical features :\n{'-' * 50} \n", categorical_features)
print(f'{'=' * 50}')
print(f"{'▇' * 70} Explaination {'▇' * 55}")
# ====================
print(f"{'Why identifying feature types is important before modeling'}\n{'-' * 50}")
print(
    f"Because it helps us to know if they the model is going to predict a continuous or a categorical value. base on that we can select the model to use.")

print(f'{'=' * 50}')




import pandas as pd
import numpy as np
import seaborn as sns

data = sns.load_dataset('titanic')


def pipeline_preprocessing(data: pd.DataFrame) -> np.ndarray:
    """
    Use case:

    Args:
        -pd.DataFrame
        -
    Returns:
        - Final feature matrix ready for model training
        -
    Errors:
        -
        -
    """

    # 1. Load dataset
    if data is not None:
        try:
            df = pd.DataFrame(data)
        except Exception as e:
            raise ValueError(f"Must be a dataset {e}")

    # 2. Handle missing values
    df = df.dropna()
    # df= df.isnull().sum() # Verification of missing values operations done
    # 3. Encode categorical variables (sex, embarked)
    df = pd.get_dummies(df, columns=['sex', 'embarked'], drop_first=True)
    # Normalize numerical features
    num_col = df.select_dtypes(include=[np.number])  # extract num feature
    mean_num_col = num_col.mean()
    std_num_col = num_col.std()

    # Formule du Z-score : (x - µ) / σ
    normalize = (num_col - mean_num_col) / std_num_col
    # 5. Convert to NumPy array
    normalize_to_numpy = normalize.to_numpy()
    return normalize_to_numpy


r = pipeline_preprocessing(data)

print(r)
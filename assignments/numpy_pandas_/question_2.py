import pandas as pd
import numpy as np
import seaborn as sns

data = sns.load_dataset("iris")


# print(type(data))
def input_data_selection(data: pd.DataFrame) -> pd.DataFrame:
    """
    Args:
        - data : Full dataset iris uploaded from seaborn
        -
    Returns:
         - Selected Data form the Full dataset
         -
    Errors:
        -

    """
    if data is not None:
        try:
            df = pd.DataFrame(data)
            first_hund_samples = df.head(101)
            only_last_two_features = df.tail(2)

            # mean  of the dataset
            # extract numerical columns
            num_col = data.select_dtypes(include=[np.number])
            numeric_dataset_col = num_col.columns.tolist()  # recuperation of the  num_col
            #
            dataset_mean = np.mean(num_col)
            # samples where petal length is greater than dataset mean
            petal_length_greater = num_col[num_col > dataset_mean]
            #
            numbers_sample_selected = len(petal_length_greater)


        except Exception as e:
            raise ValueError(f"Need data before to start the process {e}")
    return petal_length_greater, numbers_sample_selected, first_hund_samples, only_last_two_features


petal_length_greater, numbers_sample_selected, first_hund_samples, only_last_two_features = input_data_selection(data)
print(f"{'▇' * 70} TEST RESULTS {'▇' * 55}")
print(f"Initial data :\n{'-' * 50} \n", data)
print(f'{'=' * 50}')
# =========================
print(f"{'First 100 samples'}\n{'-' * 50}")
print(first_hund_samples)
print(f'{'=' * 50}')

# =========================
print(f"{'Only last 2 features'}\n{'-' * 50}")
print(only_last_two_features)
print(f'{'=' * 50}')
# =========================
print(f"{'Select samples where petal length is greater than dataset mean'}\n{'-' * 50}")
print(petal_length_greater)
print(f'{'=' * 50}')
# =========================
print(f"{'Count selected samples'}\n{'-' * 50}")
print(numbers_sample_selected)
print(f'{'=' * 50}')
# =========================
print(f"{'▇' * 70} ANALYSIS {'▇' * 55}")
print(f"{'Explain how this relates to feature-based filtering in ML'}\n{'-' * 50}")
print(
    "This relate to feature-based filtering because he help us to see the NaN values so we can either replace them or remove so we can have a better accurate predictions ")








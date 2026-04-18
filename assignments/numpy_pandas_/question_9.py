import numpy as np
import pandas as pd
import seaborn as sns

data = sns.load_dataset('tips')


def filter_ubsetting_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Use Case: this function is for Filtering + Subsetting

    Args:
        - data : full dataset imported form seaborn
        -
    Returns
        -
        -
    Errors:
        -
        -
    """

    if data is not None:
        try:
            df = pd.DataFrame(data)
        except Exception as e:
            raise ValueError(fr"need a dataset to continue {e}")
    else:
        pass
    # total_bill > 20 AND tip < 3
    total_billgreat_tip_less = df[(df['total_bill'] > 20) & (df['tip'] < 3)]
    # total_bill column
    total_bill_column = df[df['total_bill'] > 20]
    # tip column
    tip_column = df[df['tip'] < 3]

    return total_billgreat_tip_less, total_bill_column, tip_column


total_billgreat_tip_less, total_bill_column, tip_column = filter_ubsetting_data(data)



print(f"{"█" * 70} TEST RESULTS {"█" * 55}")
print(data)
print(f" total_bill > 20 AND tip < 3:")
print(f'{'-' * 50}')
print(f"{total_billgreat_tip_less}\n")
# ====================
print(f" total_bill > 20 ")
print(f'{'-' * 50}')
print(f"{total_bill_column:}\n")
# ====================
print(f'{'-' * 50}')
print(f" tip < 3:")
print(f"{tip_column}\n")
# print(f"{tip_column.max()}\n")
# ====================
print(f'{'-' * 50}')
# ====================
print(f'{'-' * 50}')

print(f"{"█" * 70} ANALYSIS {"█" * 60}")
print("Is this segment under-tipping?")
print(
    " ==>>Base on the fact that tip < 3 displays less values, we can say that yes it under-tipping")

print(f"{"█" * 70} Explain {"█" * 60}")

print("How such filtering helps anomaly detection")
print(
    " ==>> its helps anomaly detection because it can help to know easily what is happening in some range of data ")


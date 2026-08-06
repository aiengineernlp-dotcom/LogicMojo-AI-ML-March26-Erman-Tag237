import numpy as np
import pandas as pd
import seaborn as erman

data = erman.load_dataset('tips')


def Customer_Segmentation_Logic(data: pd.DataFrame) -> pd.DataFrame:
    """
    Use case:
        -
        -
    Args:
        -
        -
    Returns:
        -
        -
    Error:
        -
        -
    """

    if data is not None:
        df = pd.DataFrame(data)
    else:
        pass
    # compute Average tip by day
    average_tip_by_day = df.groupby('day')['tip'].mean()
    # Total bill by gender
    total_bill_by_gender = df.groupby('sex')['total_bill'].sum()
    # Which day has highest tipping behavior
    day_has_highest_tipping = df.groupby('day')['tip'].max()
    # tip_percentage
    df['tip_percentage'] = (df['tip'] / df['total_bill']) * 100
    tip_percentage = df['tip_percentage'].isnull().sum()

    return average_tip_by_day, total_bill_by_gender, day_has_highest_tipping, tip_percentage


average_tip_by_day, total_bill_by_gender, day_has_highest_tipping, tip_percentage = Customer_Segmentation_Logic(data)

print(f"{"█" * 70} TEST RESULTS {"█" * 55}")
print(data)
print(f" Average tip by day:")
print(f'{'-' * 50}')
print(f"{average_tip_by_day}\n")
# ====================
print(f" Total bill by gender:")
print(f'{'-' * 50}')
print(f"{total_bill_by_gender:}\n")
# ====================
print(f'{'-' * 50}')
print(f" tip percentage:")
print(f"{tip_percentage}\n")
# ====================
print(f'{'-' * 50}')
print(f" Which day has highest tipping behavior:")
print(f"{day_has_highest_tipping}\n")
print(f"{'Saturday has the highest tipping behavior'}\n")
# ====================
print(f'{'-' * 50}')

print(f"{"█" * 70} ANALYSIS {"█" * 60}")
print("How this helps in segmentation models")
print(
    " ==>>This can us to understand the main sources of incomes, and decisions making")



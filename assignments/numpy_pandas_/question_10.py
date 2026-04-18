import numpy as np

arr = [[1, 2, 3], [4, 5, 6]] # -> shape (3,2)  so 3x2=6
matrix = [[10, 20, 30], [40, 50, 60]] # -> shape (3,2)  so 3x2=6


# arr = np.array(arr).reshape(3, 2)
def numpy_manipulation(n: np.ndarray, m: np.ndarray) -> np.ndarray:
    """

    """

    try:
        # Create two arrays of shape (3,2)
        arr1 = np.array(n).reshape(3, 2)
        arr2 = np.array(m).reshape(3, 2)

    except Exception as e:
        raise ValueError(f"This data must be an numpy array: {e}")
    # Vertical stacking
    vertical_stacking = np.vstack((n,m))
    # horizontal stacking
    horizontal_stacking = np.hstack((n,m))
    #Reshape into (2,6) ->  so 2x6=12
    reshape_into_2_6 = horizontal_stacking.shape

    return arr1,arr2,vertical_stacking,horizontal_stacking,reshape_into_2_6

arr1,arr2,vertical_stacking,horizontal_stacking,reshape_into_2_6 = numpy_manipulation(arr,matrix)

print(f"{"█" * 70} TEST RESULTS {"█" * 55}")
print(f" array 1:")
print(f'{'-' * 50}')
print(f"{arr1}\n")
# ====================
print(f"array 2 ")
print(f'{'-' * 50}')
print(f"{arr2:}\n")
# ====================
print(f'{'-' * 50}')
print(f" vertical stacking:")
print(f"{vertical_stacking}\n")
# ====================
print(f'{'-' * 50}')
print(f" horizontal stacking:")
print(f"{horizontal_stacking}\n")
# ====================
print(f'{'-' * 50}')
print(f" Reshape into (2,6) ->  so 2x6=12 ")
print(f"{reshape_into_2_6}\n")
print(f'{'-' * 50}')
# ====================
print(f'{'-' * 50}')

print(f"{"█" * 70} ANALYSIS {"█" * 60}")

print(f"{"█" * 70} Explain {"█" * 60}")

print("Why reshaping is required in ML pipelines")
print(
    " ==>> Reshaping is required because it helps us to work in the exact same dimenssion  ")


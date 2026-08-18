import numpy as np


def ErrorAnalysisSimulation(n=1000) -> np.ndarray:
    """

    """

    # 1. Generate 1000 random error values using NumPy
    errors = np.random.rand(n)
    # 2. Compute:
    # *Mean
    mean_ = np.mean(errors)
    # *Standard deviation
    std_ = np.std(errors)
    # 3. Identify outliers:
    outliers_posit = mean_ + (std_ * 2)
    outliers_negat = mean_ - (std_ * 2)

    return outliers_negat


re = ErrorAnalysisSimulation()
print(re)

print(f"{"█" * 70} ANALYSIS {"█" * 60}")

print(f"{"█" * 70} Explain {"█" * 60}")
print(f"What high variance means in model performance?")
print(
    f"Because I can make the model think that because the are high, there are most important. and the model predict wrongly according ")


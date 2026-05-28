import pandas as pd
import numpy as np
from sklearn.metrics import (
    mean_squared_error,
    r2_score
)

def evaluate_model(y_true, y_pred, model_name):

    rmse = np.sqrt(
        mean_squared_error(y_true, y_pred)
    )

    r2 = r2_score(y_true, y_pred)

    print(f"\n{model_name}")

    print(f"RMSE: {rmse:.2f}")

    print(f"R²: {r2:.4f}")
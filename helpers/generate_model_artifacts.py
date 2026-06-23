import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "processed" / "mumbai.csv"
MODEL_DIR = ROOT / "model"
DF_PATH = MODEL_DIR / "df.pkl"
PIPELINE_PATH = MODEL_DIR / "pipeline.pkl"


def build_artifacts() -> None:
    df = pd.read_csv(DATA_PATH)

    feature_cols = [
        "AREA",
        "BEDROOM_NUM",
        "BALCONY_NUM",
        "FLOOR_NUM",
        "FURNISH",
        "AGE",
        "FACING",
        "LOCALITY_NAME",
    ]

    working = df[feature_cols + ["PRICE"]].copy()

    numeric_cols = ["AREA", "BEDROOM_NUM", "BALCONY_NUM"]
    categorical_cols = ["FLOOR_NUM", "FURNISH", "AGE", "FACING", "LOCALITY_NAME"]

    # Normalize strings so app defaults like "dadar"/"mid rise" always exist.
    for col in categorical_cols:
        working[col] = working[col].astype(str).str.strip().str.lower()
        working.loc[working[col].isin(["nan", "none", ""]), col] = np.nan

    for col in numeric_cols:
        working[col] = pd.to_numeric(working[col], errors="coerce")
        working[col] = working[col].fillna(working[col].median())

    for col in categorical_cols:
        working[col] = working[col].fillna(working[col].mode(dropna=True).iloc[0])

    working["PRICE"] = pd.to_numeric(working["PRICE"], errors="coerce")
    working = working.dropna(subset=["PRICE"])

    X = working[feature_cols]
    y = np.log1p(working["PRICE"])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", "passthrough", numeric_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ]
    )

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", RandomForestRegressor(n_estimators=300, random_state=42, n_jobs=-1)),
        ]
    )

    pipeline.fit(X, y)

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    with DF_PATH.open("wb") as f:
        pickle.dump(X, f)
    with PIPELINE_PATH.open("wb") as f:
        pickle.dump(pipeline, f)

    print(f"Created {DF_PATH} and {PIPELINE_PATH}")


if __name__ == "__main__":
    build_artifacts()

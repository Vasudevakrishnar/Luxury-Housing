import pandas as pd
import numpy as np

def clean_data():
    df = pd.read_csv("data.csv")

    # Missing values
    df["area"].fillna(df["area"].median(), inplace=True)
    df["price"].fillna(df["price"].median(), inplace=True)
    df["location"].fillna(df["location"].mode()[0], inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Remove invalid data
    df = df[df["area"] > 200]
    df = df[df["price"] > 100000]

    # Outlier removal (IQR)
    q1 = df["price"].quantile(0.25)
    q3 = df["price"].quantile(0.75)
    iqr = q3 - q1

    df = df[(df["price"] >= q1 - 1.5*iqr) & (df["price"] <= q3 + 1.5*iqr)]

    # Feature engineering
    df["price_per_sqft"] = df["price"] / df["area"]
    df["house_age"] = 2026 - df["year_built"]

    df.to_csv("processed_data.csv", index=False)

    return df
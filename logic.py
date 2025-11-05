import pandas as pd


def mean_fare(df: pd.DataFrame, embarked: str, survived: bool) -> float:

    data = df[df["Survived"] == int(survived)]
    return data[data["Embarked"] == embarked]["Fare"].mean()

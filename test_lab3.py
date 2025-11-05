import pytest
import pandas as pd
import numpy as np
import logic as l


@pytest.fixture
def titanic_df():
    data = {
        "Survived": [1, 0, 1, 0, 1, 0],
        "Embarked": ["S", "S", "C", "C", "Q", "Q"],
        "Fare": [10, 20, 30, 40, 50, 60]
    }
    return pd.DataFrame(data)


def test_mean_fare_survived_S(titanic_df):
    result = l.mean_fare(titanic_df, "S", True)
    assert result == 10


def test_mean_fare_dead_S(titanic_df):
    result = l.mean_fare(titanic_df, "S", False)
    assert result == 20


def test_mean_fare_survived_C(titanic_df):
    result = l.mean_fare(titanic_df, "C", True)
    assert result == 30


def test_mean_fare_dead_Q(titanic_df):
    result = l.mean_fare(titanic_df, "Q", False)
    assert result == 60


def test_mean_fare_nan(titanic_df):
    s = l.mean_fare(titanic_df, "X", True)
    d = l.mean_fare(titanic_df, "X", False)
    assert np.isnan(s)
    assert np.isnan(d)
    
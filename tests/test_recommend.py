import pytest
import numpy as np
import pandas as pd
from datetime import datetime
from app.recommend import (
    recommend_monuments,
    norm_distance,
    type_match,
    final_weight_sum,
)


@pytest.fixture
def sample_monuments_df():
    """Create a sample dataframe with test monument data"""
    return pd.DataFrame(
        [
            {
                "id": 1,
                "name": "Pashupatinath Temple",
                "latitude": 27.7104,
                "longitude": 85.3487,
                "type": "Hindu Temple",
                "popularity": 0.95,
                "indoor": False,
                "description": "Famous temple",
                "location": "Kathmandu",
            },
            {
                "id": 2,
                "name": "Boudhanath Stupa",
                "latitude": 27.7139,
                "longitude": 85.3600,
                "type": "Buddhist Temple",
                "popularity": 0.92,
                "indoor": False,
                "description": "Large stupa",
                "location": "Kathmandu",
            },
            {
                "id": 3,
                "name": "Garden of Dreams",
                "latitude": 27.7170,
                "longitude": 85.2920,
                "type": "Garden",
                "popularity": 0.75,
                "indoor": False,
                "description": "Beautiful garden",
                "location": "Kathmandu",
            },
        ]
    )


@pytest.fixture
def sample_events_df():
    """Create a sample dataframe with test event data"""
    return pd.DataFrame(
        [
            {
                "name": "Dashain Festival",
                "start_date": "2025-10-10",
                "end_date": "2025-10-24",
                "related_type": "Hindu Temple",
                "monument_id": 1,
            },
            {
                "name": "Buddha Jayanti",
                "start_date": "2025-05-15",
                "end_date": "2025-05-20",
                "related_type": "Buddhist Temple",
                "monument_id": 2,
            },
        ]
    )


def test_norm_distance(sample_monuments_df):
    """Test the normalized distance calculation function"""
    # Test with coordinates matching Pashupatinath Temple
    distances = norm_distance(27.7104, 85.3487, sample_monuments_df)

    # The first monument should have distance 0 (normalized to 1.0)
    assert distances[0] > 0.99

    # All distances should be between 0 and 1
    assert all(0 <= d <= 1 for d in distances)


def test_type_match(sample_monuments_df):
    """Test the type matching function"""
    # Test with Hindu Temple preference
    matches = type_match("Hindu Temple", sample_monuments_df)

    # First monument should match (1), others should not match (0)
    assert matches[0] == 1
    assert matches[1] == 0
    assert matches[2] == 0


def test_recommend_monuments():
    """Test the main recommendation function"""
    # Simple test to check if the function runs without errors
    results = recommend_monuments(27.7104, 85.3487, "Hindu Temple")

    # We should get a list of recommendations
    assert isinstance(results, list)

    # The first recommendation should be a dictionary with monument info
    if results:
        assert isinstance(results[0], dict)
        assert "name" in results[0]
        assert "type" in results[0]

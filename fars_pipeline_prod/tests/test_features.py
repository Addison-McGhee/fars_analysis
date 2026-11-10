import pandas as pd
import pytest
from fars_pipeline_prod.src.features import clean_and_transform_accidents

def test_clean_and_transform_accidents():
    # Create sample raw data frame
    raw_df = pd.DataFrame({
        "STATE": [6, 12],
        "ST_CASE": [2024001, 2024002]
    })
    
    cleaned_df = clean_and_transform_accidents(raw_df)
    
    # Assertions
    assert "state" in cleaned_df.columns or "state" in [c.lower() for c in cleaned_df.columns]
    assert len(cleaned_df) == 2
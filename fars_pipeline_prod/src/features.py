import pandas as pd
import numpy as np

def clean_and_transform_accidents(df: pd.DataFrame) -> pd.DataFrame:
    """Applies baseline data cleaning and feature engineering to accident datasets."""
    df_clean = df.copy()
    
    # Example standardization: ensure standard column naming conventions if needed
    df_clean.columns = [col.lower() for col in df_clean.columns]
    
    # Drop rows with critical missing spatial or temporal identifiers if applicable
    if "st_case" in df_clean.columns:
        df_clean = df_clean.dropna(subset=["st_case"])
        
    return df_clean
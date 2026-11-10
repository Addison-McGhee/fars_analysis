import pandas as pd
from pathlib import Path

def load_accident_data(base_path: str = ".") -> pd.DataFrame:
    """Loads and merges main FARS accident data with its auxiliary counterpart."""
    path = Path(base_path)
    accident_path = path / "FARS2024NationalCSV" / "accident.csv"
    acc_aux_path = path / "FARS2024NationalAuxiliaryCSV" / "ACC_AUX.CSV"
    
    if not accident_path.exists():
        raise FileNotFoundError(f"Accident file not found at {accident_path}")
        
    accident = pd.read_csv(accident_path, low_memory=False)
    
    if acc_aux_path.exists():
        acc_aux = pd.read_csv(acc_aux_path, low_memory=False)
        accident = pd.merge(accident, acc_aux, on=["STATE", "ST_CASE"], how="inner")
        
    return accident

def load_person_modeling_data(base_path: str = ".") -> pd.DataFrame:
    """Loads person-level data merged with vehicle context for predictive modeling."""
    path = Path(base_path)
    person_path = path / "FARS2024NationalCSV" / "person.csv"
    vehicle_path = path / "FARS2024NationalCSV" / "vehicle.csv"
    
    if not person_path.exists():
        raise FileNotFoundError(f"Person file not found at {person_path}")
    if not vehicle_path.exists():
        raise FileNotFoundError(f"Vehicle file not found at {vehicle_path}")
        
    person = pd.read_csv(person_path, low_memory=False)
    vehicle = pd.read_csv(vehicle_path, low_memory=False)
    
    # Merge person with vehicle context matching your notebook logic
    merged_df = person.merge(
        vehicle[['ST_CASE', 'VEH_NO', 'BODY_TYP', 'MOD_YEAR', 'TRAV_SP']], 
        on=['ST_CASE', 'VEH_NO'], 
        how='left'
    )
    return merged_df
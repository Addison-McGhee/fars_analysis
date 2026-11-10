import sys
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, classification_report

# Add src directory to python path
sys.path.append(str(Path(__file__).resolve().parent))

from data_loader import load_person_modeling_data

def main():
    print("Initializing FARS pipeline workflow...")
    
    # 1. Load person-level modeling data
    try:
        df = load_person_modeling_data(base_path="..") 
    except FileNotFoundError:
        df = load_person_modeling_data(base_path=".")
        
    print(f"Successfully loaded person modeling dataset. Shape: {df.shape}")
    
    # 2. Standardize column names to lowercase
    df.columns = [col.lower() for col in df.columns]
    
    # 3. Define target: 1 if fatal injury (inj_sev == 4), 0 otherwise
    if 'inj_sev' in df.columns:
        df['target'] = (df['inj_sev'] == 4).astype(int)
    else:
        raise ValueError("Critical column 'inj_sev' not found in dataset.")
        
    # Clean continuous fields
    df['age_clean'] = df['age'].where(df['age'] < 99, pd.NA).fillna(df['age'].median())
    
    # Select features
    feature_cols = ['age_clean', 'sex', 'seat_pos', 'rest_use', 'air_bag']
    available_features = [col for col in feature_cols if col in df.columns]
    
    print(f"Using features for modeling: {available_features}")
    
    X = pd.get_dummies(df[available_features], drop_first=True).fillna(0)
    y = df['target']
    
    # 4. Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # 5. Model Training (Random Forest)
    print("Training Random Forest Classifier on Injury Severity...")
    rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)
    
    # 6. Evaluation
    y_proba = rf.predict_proba(X_test)[:, 1]
    auc_roc = roc_auc_score(y_test, y_proba)
    
    print(f"--- Model Evaluation ---")
    print(f"ROC-AUC Score: {auc_roc:.4f}")
    print(classification_report(y_test, (y_proba >= 0.5).astype(int)))
    print("Pipeline execution and model training completed successfully!")

if __name__ == "__main__":
    main()
"""
Validates the processed dataset according to data contract. Ensures column names, data types, and ranges are correct.
"""

import pandas as pd

PROCESSED_PATH = 'data/processed.csv'
df = pd.read_csv(PROCESSED_PATH )

def validate_anemia_dataset(df):
    errors = [] # all found errors will be appended here
    
    # check for missing critical values:
    critical_cols = ['number', 'sex', 'hb', 'anemic']
    for col in critical_cols:
        if df[col].isnull().any(): # checks if critical column contains any missing values
            errors.append(f"Missing values found in column: {col}") 
            
    # validate data types
    if not pd.api.types.is_integer_dtype(df['number']): # checks if 'number' column is NOT of integer dtype
        errors.append("Column 'number' should be integer")
        
    if not pd.api.types.is_numeric_dtype(df['hb']): # checks if 'hb' column is NOT of a numeric dtype
        errors.append("Column 'hb' should be numeric")
    
        
    if not pd.api.types.is_integer_dtype(df['anemic']): # checks if 'anemic' column is NOT of an integer type
        errors.append("Column 'anemic' should be integer")
    
    # validates data range 
    for col in ['pct_red_pixel', 'pct_green_pixel', 'pct_blue_pixel']:
        if not df[col].between(0, 100).all(): # checks if all values in each %pixel columns are within 0, 100 range
            errors.append(f"Invalid values in {col}: should be 0-100")
            
    if not df['hb'].between(1, 25).all(): # checks if all values in 'hb' column are within 1, 25 range
        errors.append("Invalid values in 'hb': should be 1-25")
        
    # validates labels
    valid_sex = {"Male", "Female"} # defines valid sex labels
    if not set(df['sex'].unique()).issubset(valid_sex): # creates set from unique values in 'sex' column, then checks if set contains values other than "Male" or "Female"
        errors.append(f"Invalid values in 'sex': found {set(df['sex'].unique()) - valid_sex}")
    
    valid_anemic = {0, 1} # defines valid anemic values
    if not set(df['anemic'].unique()).issubset(valid_anemic): # creates set from unique values 'anemic' column, then checks if set contains values other than 0 or 1
        errors.append(f"Invalid values in 'anemic': found {set(df['anemic'].unique()) - valid_anemic}") 
    
    # summary
    if errors:
        print("Data validation failed with the following issues:")
        for e in errors:
            print("-", e)
        return False
    else:
        print("Data validation successful.")
        return True
    
validate_anemia_dataset(df)
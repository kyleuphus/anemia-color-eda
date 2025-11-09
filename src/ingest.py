"""
Reads the raw dataset, cleans and standardizes column names, types, and values according to data contract, 
then writes data/processed.csv
"""
import pandas as pd

RAW_PATH = 'data/raw.csv'
PROCESSED_PATH = 'data/processed.csv'

df = pd.read_csv(RAW_PATH)

df.columns = (
    df.columns
        .str.strip()
        .str.lower()
        .str.replace('%', 'pct ')
        .str.replace(' ', '_')
        .str.replace('anaemic', 'anemic') # changes to American spelling
)
df.head()

# column 1 (number)
if "number" in df.columns:
    df["number"] = pd.to_numeric(df["number"], errors="coerce") # converts non-numeric rows to NaN
    df = df.dropna(subset=["number"])# drops rows where number is NaN
    df["number"] = df["number"].astype(int) # converts all to int
    
df["number"] = df["number"].astype(int) # converts to type int
    
# column 2 (sex)
if "sex" in df.columns:
    df["sex"] = (
        df["sex"].astype(str) # converts all to str
        .str.strip() # strips whitespace
        .str.title() # capitalizes first letter
    )
    df = df[df["sex"].isin(["M", "F"])] # removes non "M" or "F" rows
    df["sex"] = df["sex"].replace({"M": "Male", "F": "Female"}) # converts "M" to "Male" and "F" to "Female"
    
# columns 3-5 (pixel values)
for col in ["pct_red_pixel", "pct_green_pixel", "pct_blue_pixel"]:
    df[col] = (
        df[col]
        .astype(str) # converts all to string
        .str.strip() # strips whitespace
    )
    df[col] = pd.to_numeric(df[col], errors="coerce") # safely converts back to numeric
    df = df[df[col].between(0, 100)] # keeps valid percentages
    df[col] = df[col].astype(float) # converts to float
    
# column 6 (hb)
df["hb"] = pd.to_numeric(df["hb"], errors="coerce") # converts non-numeric rows to NaN
df = df[df["hb"].between(1, 25)] # removes rows outside of valid range

# column 7 (anemic)
if "anemic" in df.columns:
    df["anemic"] = (
        df["anemic"]
           .astype(str)
           .str.lower()
          .replace({"yes": 1, "no": 0, "true": 1, "false": 0}) # converts str labels to 0 (non-anemic) and 1 (anemic))   
    )
    df["anemic"] = pd.to_numeric(df["anemic"], errors="coerce").fillna(0).astype(int) # converts to numeric, replaces non-numeric 
                                                                                    # with NaN, replaces NaN with 0, converts to int

# QC
print("Final shape:", df.shape)
print(df.head())
print(df.dtypes)

# writing processed csv
df.to_csv(PROCESSED_PATH, index=False)
print(f'Clean data written to {PROCESSED_PATH}')

import pandas as pd
import numpy as np

PROCESSED_PATH = 'data/processed.csv'
FEATURES_PATH = 'data/features.csv'

df = pd.read_csv(PROCESSED_PATH)

# finding red ratio (how dominant the red pixel count is)
df["red_ratio"] = df['pct_red_pixel'] / (df["pct_red_pixel"]+df["pct_green_pixel"] + df["pct_blue_pixel"])

# finding blue ratio 
df["blue_ratio"] = df['pct_blue_pixel'] / (df["pct_red_pixel"]+df["pct_green_pixel"] + df["pct_blue_pixel"])

# finding red/blue ratio
df["red_blue_ratio"] = df["pct_red_pixel"] / df["pct_blue_pixel"]

# log transformed Hb
df["hb_log"] = np.log1p(df["hb"]) # takes natual log of (1 + Hb)

# saving feature-engineered dataset
df.to_csv(FEATURES_PATH, index=False)


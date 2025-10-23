# Anemia Color Exploratory Data Analysis

Exploratory data analysis of image-derived red, green, and blue pixel counts and hemoglobin levels with patient sex and anaemic status. Began as final project for Intro to Python for Data Science class, but I decided to flesh it out for a larger-scale project.


## Data background:
Higher red pixel intensity is associated with higher hemoglobin (Hb) levels and lower likelihood of anemia, while higher green pixel intensity is associated with lower Hb levels and a higher likelihood, and blue pixel intensity has little to no correlation. 

### Data Contract
| Column          | Type  | Allowed / Range | Units | Notes |
|-----------------|-------|-----------------|-------|-------|
| `Number`        | int   | ≥ 0             | —     | No duplicates |
| `Sex`           | str   | `Male`,`Female` | —     | Normalized case |
| `%Red Pixel`    | float | 0–100           | %     | Must be numeric (float) and within range |
| `%Green pixel`  | float | 0–100           | %     | Must be numeric (float) and within range |
| `%Blue pixel`   | float | 0–100           | %     | Must be numeric (float) and within range |
| `Hb`            | float | 1–25            | g/dL  | Implemented bounds for QC |
| `Anaemic`       | int   | {0,1}           | —     | Normalized from labels |

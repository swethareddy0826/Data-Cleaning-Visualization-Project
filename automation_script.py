import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("Superstore.csv", encoding='latin1')

print("Original Data Shape:", df.shape)

# -----------------------------
# DATA CLEANING
# -----------------------------

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df.fillna(method='ffill', inplace=True)

# Remove outliers using IQR method
numeric_columns = df.select_dtypes(include=np.number).columns

for col in numeric_columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df = df[(df[col] >= lower) & (df[col] <= upper)]

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("Cleaned Data Saved Successfully")

# -----------------------------
# SUMMARY REPORT
# -----------------------------

report = f"""
DATA CLEANING SUMMARY
---------------------
Original Rows: {len(pd.read_csv('Superstore.csv', encoding='latin1'))}
Cleaned Rows: {len(df)}

Missing values handled
Duplicates removed
Outliers removed
"""

with open("summary_report.txt", "w") as file:
    file.write(report)

print("Summary Report Generated")

# -----------------------------
# VISUALIZATION
# -----------------------------

plt.figure(figsize=(10,6))

if 'Sales' in df.columns and 'Category' in df.columns:
    sns.barplot(x='Category', y='Sales', data=df)

    plt.title("Sales by Category")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig("sales_chart.png")

    print("Chart Saved Successfully")

print("Automation Completed Successfully")
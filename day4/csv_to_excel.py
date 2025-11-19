import pandas as pd

# Read the CSV file created by Selenium
df = pd.read_csv("laptops.csv")

# Convert to Excel
df.to_excel("laptops.xlsx", index=False)

print("✅ Conversion complete! 'laptops.xlsx' created successfully.")

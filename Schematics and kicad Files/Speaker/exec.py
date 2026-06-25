import pandas as pd

# Load the CSV file (Use raw string or double backslashes for Windows paths)
df = pd.read_csv(r"C:\Users\Iliya\OneDrive\Desktop\Училище\12 клас\Дипломен проект\Diploma\DIplomaV1\Final Diploma\Speaker\BOM.csv")

# Save as Excel file
df.to_excel(r"C:\Users\Iliya\OneDrive\Desktop\BOM.xlsx", index=False)  # Saves without index column

print("Excel file saved successfully!")

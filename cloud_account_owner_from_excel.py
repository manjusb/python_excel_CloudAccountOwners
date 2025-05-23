import pandas as pd

# Load the Excel file
excel_file = "your_excel_file.xlsx"  # Replace with your actual Excel file
df = pd.read_excel(excel_file, engine="openpyxl")

# Load the list of names from the CSV file
names_file = "owner_names.csv"
names_df = pd.read_csv(names_file)
target_names = names_df['Name'].tolist()

# Find the column whose header starts with "Cloud account owners"
matching_columns = [col for col in df.columns if str(col).strip().lower().startswith("cloud account owners")]

if not matching_columns:
    raise ValueError("No column found that starts with 'Cloud account owners'.")

# Assuming there's only one matching column
target_column = matching_columns[0]

# Filter the rows where the target column matches any of the names
filtered_df = df[df[target_column].isin(target_names)]

# Save results to a new Excel file
filtered_df.to_excel("filtered_results.xlsx", index=False)

print(f"Filtered {len(filtered_df)} rows using column '{target_column}' with {len(target_names)} names.")

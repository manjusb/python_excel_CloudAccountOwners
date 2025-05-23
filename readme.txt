Excel Row Filter Based on Owner Names
This project provides a Python script that reads an Excel file with 30+ columns and thousands of rows and filters rows based on a list of owner names provided in a separate CSV file. It dynamically locates the column that starts with "Cloud account owners" and extracts matching entries.

📁 Project Structure
bash
Copy
Edit
project-folder/
│
├── your_excel_file.xlsx         # Input Excel file with all data
├── owner_names.csv              # CSV file containing list of owner names
├── filter_by_owner.py           # Python script to filter data
└── filtered_results.xlsx        # Output Excel file (generated)
✅ Features
Automatically identifies the column with a header starting with "Cloud account owners".

Matches entries based on exact name from a list.

Handles large files efficiently using pandas.

Saves filtered results to a new Excel file.

📦 Requirements
Python 3.7+

Required libraries:

bash
Copy
Edit
pip install pandas openpyxl
📄 Input Files
1. your_excel_file.xlsx
An Excel file with one of the columns starting with "Cloud account owners", for example:

Cloud account owners	Account ID	Region	Service
John Doe	1234567890	us-east-1	EC2

2. owner_names.csv
A CSV file containing the list of owner names under a column called "Name":

csv
Copy
Edit
Name
John Doe
Jane Smith
🚀 Usage
Run the script:

bash
Copy
Edit
python filter_by_owner.py
The script will:

Read the input Excel file.

Load the names from owner_names.csv.

Identify the column starting with "Cloud account owners".

Filter rows that match names in the list.

Write the filtered results to filtered_results.xlsx.

🛠 Configuration
To use different file names, simply update the variables at the top of the script:

python
Copy
Edit
excel_file = "your_excel_file.xlsx"
names_file = "owner_names.csv"
📤 Output
filtered_results.xlsx will contain all rows from the Excel file where the owner matches any name from the CSV.

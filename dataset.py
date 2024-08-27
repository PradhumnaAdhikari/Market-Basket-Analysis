# import pandas as pd

# # Define the dataset
# data = {
#     'TransactionID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
#                       11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
#     'Items': [
#         'Milk,Bread,Eggs', 'Bread,Butter', 'Milk,Bread,Butter,Eggs', 
#         'Bread', 'Butter,Eggs', 'Milk,Eggs', 'Bread,Butter,Eggs', 
#         'Milk,Bread,Butter', 'Milk,Bread', 'Bread,Eggs', 
#         'Milk,Butter', 'Eggs', 'Milk,Bread,Butter,Eggs', 
#         'Bread,Butter', 'Milk,Eggs', 'Bread,Eggs', 
#         'Milk,Butter,Eggs', 'Bread,Butter,Eggs', 'Milk,Bread', 
#         'Butter,Eggs'
#     ]
# }

# # Create a DataFrame
# df = pd.DataFrame(data)

# # Save to a CSV file
# df.to_csv('transactions.csv', index=False)

# print("Dataset saved as 'transactions.csv'")
import pandas as pd

try:
    excel_file_path = 'Assignment-1_Data.xlsx'
    df = pd.read_excel(excel_file_path)
except FileNotFoundError:
    print("Error: 'Assignment-1_Data.xlsx' file not found.")
    exit()
except pd.errors.EmptyDataError:
    print("Error: No data found in 'Assignment-1_Data.xlsx'.")
    exit()
except pd.errors.ParserError:
    print("Error: Parsing error. Check the Excel format.")
    exit()
csv_file_path = 'transactions.csv'
try:
    df.to_csv(csv_file_path, index=False)
    print(f"Dataset saved as '{csv_file_path}'")
except Exception as e:
    print(f"An error occurred while saving the CSV file: {e}")

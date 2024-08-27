# import pandas as pd
# df = pd.read_csv('transactions.csv')

# transactions = df.groupby('TransactionID')['Items'].apply(list).values.tolist()


import pandas as pd

try:
    df = pd.read_csv('transactions.csv')
except FileNotFoundError:
    print("Error: 'transactions.csv' file not found.")
    exit()
except pd.errors.EmptyDataError:
    print("Error: No data found in 'transactions.csv'.")
    exit()
except pd.errors.ParserError:
    print("Error: Parsing error. Check the CSV format.")
    exit()

if 'TransactionID' not in df.columns or 'Items' not in df.columns:
    print("Error: 'TransactionID' or 'Items' column missing in the CSV.")
    exit()

transactions = df.groupby('TransactionID')['Items'].apply(list).values.tolist()

print(transactions)

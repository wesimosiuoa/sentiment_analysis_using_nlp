import pandas as pd

def read_and_convert():
    try:
        # Attempt to read the file
        data = pd.read_excel('sentimentdataset.xlsx', engine='openpyxl')
        # print(f"Social Media Data\n{data.head()}")

        # Convert to CSV
        data.to_csv('sentimentdataset.csv', index=False)
        print("File converted to CSV.")
        df =  pd.read_csv('sentimentdataset.csv')
        print (df.head())
    except Exception as e:
        print(f"An error occurred: {e}")

read_and_convert()

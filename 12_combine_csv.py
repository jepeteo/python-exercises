import pandas as pd

def merge_csv(file1, file2, output_file):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    all_columns = set(df1.columns).union(set(df2.columns))
    
    # ensure both have the same columns
    df1 = df1.reindex(columns=all_columns)
    df2 = df2.reindex(columns=all_columns)    
    
    # concatenate
    merged_df = pd.concat([df1, df2], ignore_index=True)
    
    # write to file
    merged_df.to_csv(output_file, index=False)
    
file1 = "MOCK_DATA.csv"
file2 = "MOCK_DATA_1.csv"
output_file = "merged_MOCK_DATA.csv"

merge_csv(file1, file2, output_file)
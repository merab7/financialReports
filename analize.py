import pandas as pd

def make_table(data):
    
    df = pd.DataFrame.from_dict(data)
    
    # Check if all columns are completely NaN
    if df.isna().all().all():
        return None  # or you could use 'return' to simply exit the function without returning anything
    
    return df
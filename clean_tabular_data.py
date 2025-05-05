import pandas as pd

def clean_product_data(df:pd.DataFrame):
    df['price'] = df['price'].replace({'£':'', ',':''}, regex=True)
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df = df.dropna()
    return df






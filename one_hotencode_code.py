import numpy as np
import pandas as pd

data = {
    'Devil_class': ['low', 'medium', 'high', 'low', 'medium', 'satan', 'super', 'transcendent', 'low','medium','transcendent'],
    'numeric_value': [1, 2, 3, 4, 5, 6, 7, 8,9,10,11]
}
df = pd.DataFrame(data)
ds= pd.Series(data)
print(df)
print("\n\n\n")
print(ds)

def one_hotencode_myfunc(df, str):
    different_values = sorted(df[str].unique())
    for val in different_values:
        col_name = f"{str}_{val}"  # column name create karte isse
        df[col_name] = (df[str] == val).astype(int)  # astype(int) se hum data column ke andar ko 0 ya 1 me convert karte
    df = df.drop(str, axis=1)  # oriiginal column (axis =1)/y axis ko drop karte isse
    return df

df_one_hot = one_hotencode_myfunc(df.copy(), 'Devil_class')# func implement karte

print("The DataFrame before :")
print(df)
print("\nDataFrame after One Hot Encoding:")
print(df_one_hot)
    

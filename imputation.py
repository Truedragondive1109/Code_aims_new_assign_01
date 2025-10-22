import numpy as np
import pandas as pd
data = {
    'Devil_class': ['low', np.nan, 'high', 'low', 'medium', 'satan', 'super', 'transcendent', 'low','medium','transcendent'],
    'numeric_value': [1, 2, 3, 4, 5, 6, np.nan, 8,9,10,11]
}

df=pd.DataFrame(data)

df_before=df.copy()

#pehle missing numerical values ko impute karenge baaki jo bache number h unke mean se
#yha define karke nhi kar rha kyuki this is easier to understand

non_missing_num = df['numeric_value'][~df['numeric_value'].isna()]
if len(non_missing_num) > 0:
    mean_val = non_missing_num.mean()
    df['numeric_value'] = np.where(df['numeric_value'].isna(), mean_val, df['numeric_value'])

#uske baad missing categori/yaha Devil_class isse karenge iske mode se jo kaafi accha useful rhega
non_missing_cat = df['Devil_class'][~df['Devil_class'].isna()]
if len(non_missing_cat) > 0:
    mode_val = non_missing_cat.mode()[0]

df['Devil_class'] = np.where(df['Devil_class'].isna(), mode_val, df['Devil_class'])



print("Original DataFrame:")
print(df_before)
print("\nDataFrame after Imputation:")
print(df)




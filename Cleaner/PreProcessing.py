import pandas as pd
import numpy as np


def read(path, missing_na=['NA', 'NaN']):
    df = pd.read_csv(path, na_values=missing_na, )
    df.drop_duplicates(inplace=True)
    count_na = df.isna().sum()
    print(df)
    print(count_na)
    return df


def noisy_replace(data_frame, obj,  col):
    cnt = 0
    print(data_frame.iloc[:, col])
    for row in data_frame[data_frame.columns.values[col]]:
        try:
            int(row)
            if obj is 'int':
                data_frame.iloc[cnt, col] = np.nan
            elif obj is 'str':
                pass
        except ValueError:
            if obj is 'int':
                pass
            elif obj is 'str':
                data_frame.iloc[cnt, col] = np.nan
        cnt += 1
    print(data_frame.iloc[:, col])



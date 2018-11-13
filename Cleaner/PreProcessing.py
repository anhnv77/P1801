import pandas as pd
import numpy as np


def read(path, missing_na=['NA', 'NaN']):
    df = pd.read_csv(path, na_values=missing_na, )
    df.drop_duplicates(inplace=True)
    count_na = df.isna().sum()
    print(df)
    print("\nNaN in columns: ")
    print(count_na, '\n')
    return df


def noisy(data_frame, obj,  col):
    """
    :param data_frame: Data frame
    :param obj: int or str
    :param col: column to handle noisy data
    :return: None
    """
    cnt = 0
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

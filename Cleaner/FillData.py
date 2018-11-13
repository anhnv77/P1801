def dropna(data_frame, thresh=None, inplace=False):
    """
    :param data_frame: Data frame
    :param thresh: Numbers of values non NaN
    :param inplace: replace in file
    :return: None
    """
    if not thresh:
        thresh = data_frame.columns.size

    df = data_frame.dropna(thresh=thresh, inplace=inplace)
    return df;


def basic_fill(data_frame, col, fill_value, inplace=False):
    """
    :param data_frame: Data frame
    :param col: column to fill
    :param fill_value:
        bfill: fill backward
        ffill: fill forward
        mean: fill by mean
    :param inplace: replace in file
    :return: None
    """
    df = data_frame

    if fill_value == 'back':
        df.iloc[:, col] = data_frame.iloc[:, col].fillna(method='bfill', inplace=inplace)
    elif fill_value == 'forward':
        df.iloc[:, col] = data_frame.iloc[:, col].fillna(method='ffill', inplace=inplace)
    elif fill_value == 'mean':
        df.iloc[:, col] = data_frame.iloc[:, col].fillna(data_frame.iloc[:, col].mean(), inplace=inplace)
    else:
        df.iloc[:, col] = data_frame.iloc[:, col].fillna(fill_value, inplace=inplace)
    return df

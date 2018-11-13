import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_rows = 10


#   Describe file
def visualizer(path):
    """
        :param path: Path to your file
        :return: A data frame of your file
    """
    df = pd.read_csv(path)

    print(df)
    print('-' * 50)
    print(df.describe())
    return df


#   Draw bar plot
def draw_bar(data_frame, rows, cols, stacked=False, horizontal=False):
    """
        :param data_frame: The data frame of your file
        :param rows: Rows will be shown:
                           + pass a num to display one row
                           + pass an array [num1, num2, num3, ...] to display rows you want
                           + pass a range(start, end) for multiple rows
        :param cols: Cols will be shown:
                           + similar to the rows
        :param stacked: Your bar chart is stacked or not
        :param horizontal: Display horizontal bar
        :return: None
    """
    df = data_frame.iloc[rows, cols]
    if horizontal:
        df.plot.barh(stacked=stacked, alpha=0.5, rot=0)
    else:
        df.plot.bar(stacked=stacked, alpha=0.5, rot=0)
    plt.show()


#   Draw line plot
def draw_line(data_frame, rows, cols):
    """

        :param data_frame: The data frame of your file
        :param rows: Rows will be shown:
                           + pass a num to display one row
                           + pass an array [num1, num2, num3, ...] to display rows you want
                           + pass a range(start, end) for multiple rows
        :param cols: Cols will be shown:
                           + similar to the rows
        :return: None
    """
    df = data_frame.iloc[rows, cols]
    df.plot(alpha=0.5, rot=0)
    plt.show()


#   Draw histogram plot
def draw_hist(data_frame, cols, bins=50):
    """
        :param data_frame: The data_frame of your file
        :param cols: Cols will be shown:
                           + pass a num to display one col
                           + pass an array [num1, num2, num3, ...] to display cols you want
                           + pass a range(start, end) for multiple cols
        :param bins: Number of the bars in the histogram plot
        :return: None
    """
    df = data_frame.iloc[:, cols]
    df.plot.hist(bins=bins, rot=0, alpha=0.5)
    plt.show()


#   Draw pie plot
def draw_pie(data_frame, row, cols):
    """
        :param data_frame: The data_frame of your file
        :param rows: Rows will be shown:
                           + pass a num to display one row
                           + pass an array [num1, num2, num3, ...] to display rows you want
                           + pass a range(start, end) for multiple rows
        :param cols: Cols will be shown:
                           + similar to the rows
        :param row: A int showing the row will be drawn
        :return: None
    """
    df = data_frame.iloc[row, cols]
    df.plot.pie(rot=0)
    plt.show()


#   Draw stem plot
def draw_stem(data_frame, rows, cols, linefmt='-.'):
    """
        :param data_frame: The data_frame of your file
        :param rows: Rows will be shown:
                           + pass a num to display one row
                           + pass an array [num1, num2, num3, ...] to display rows you want
                           + pass a range(start, end) for multiple rows
        :param cols: Cols will be shown:
                           + similar to the rows
        :param cols: A int or array showing the column will be drawn
        :param linefmt: A string defining the properties of the vertical lines
        :return: None
    """
    df = data_frame.iloc[rows, cols]
    plt.stem(df, bottom=0, linefmt=linefmt)
    plt.show()


#   Draw box plot
def draw_box(data_frame, rows, cols):
    """
        :param data_frame: The data_frame of your file
        :param rows: Rows will be shown:
                           + pass a num to display one row
                           + pass an array [num1, num2, num3, ...] to display rows you want
                           + pass a range(start, end) for multiple rows
        :param cols: Cols will be shown:
                           + similar to the rows
        :param vert: Horizontal or not
        :return: None
    """
    df = data_frame.iloc[rows, cols]
    plt.boxplot(df, vert=False)
    plt.show()


#   Draw violin plot
def draw_violin(data_frame, cols):
    """
        :param data_frame: The data_frame of your file
        :param cols: Cols will be shown:
                           + pass a num to display one col
                           + pass an array [num1, num2, num3, ...] to display cols you want
                           + pass a range(start, end) for multiple cols
        :return: None
    """
    df = data_frame.iloc[:, cols]
    plt.violinplot(df, vert=False, showmedians=True)
    plt.show()


# Parallel_coordinate
def parallel_coordinate(df,label):
    """
    :param df: Data frame
    :param label: Label
    :return: None
    """
    from pandas.plotting import parallel_coordinates
    parallel_coordinates(df,label)
    plt.show()


# Heatmap
def heatmap(df):
    """
    Show heatmap
    :param df:  dataframe
    :return: None
    """
    from pandas import DataFrame
    corr = DataFrame(df.corr())
    print(corr)
    plt.pcolor(corr)
    plt.show()

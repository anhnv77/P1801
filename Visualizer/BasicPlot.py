import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_rows = 10

def fileVisualizer(path):
    '''
        Describe file
        :param path: Path to your file
        :return: A Data Frame of your file
    '''
    df = pd.read_csv(path)

    print(df)
    print('-' * 50)
    print(df.describe())
    return df

def drawBar(dataFrame, rows, cols, stacked=False, horizontal=False):
    '''
        Draw bar plot
        :param dataFrame: The DataFrame of your file
        :param rows: Rows will be shown:
                           + pass a num to display one row
                           + pass an array [num1, num2, num3, ...] to display rows you want
                           + pass a range(start, end) for multiple rows
        :param cols: Cols will be shown:
                           + similar to the rows
        :param stacked: Your bar chart is stacked or not
        :param horizontal: Display horizontal bar
        :return: Void
    '''
    df = dataFrame.iloc[rows, cols]
    if horizontal:
        df.plot.barh(stacked=stacked, alpha=0.5, rot=0)
    else:
        df.plot.bar(stacked=stacked, alpha=0.5, rot=0)
    plt.show()

def drawLine(dataFrame, rows, cols):
    '''
        Draw line plot
        :param dataFrame: The DataFrame of your file
        :param rows: Rows will be shown:
                           + pass a num to display one row
                           + pass an array [num1, num2, num3, ...] to display rows you want
                           + pass a range(start, end) for multiple rows
        :param cols: Cols will be shown:
                           + similar to the rows
        :return: Void
    '''
    df = dataFrame.iloc[rows, cols]
    df.plot(alpha=0.5, rot=0)
    plt.show()

def drawHistogram(dataFrame, cols, bins=50):
    '''
        Draw histogram plot
        :param dataFrame: The DataFrame of your file
        :param cols: Cols will be shown:
                           + pass a num to display one col
                           + pass an array [num1, num2, num3, ...] to display cols you want
                           + pass a range(start, end) for multiple cols
        :param bins: Number of the bars in the histogram plot
        :return: Void
    '''
    df = dataFrame.iloc[:, cols]
    df.plot.hist(bins=bins, rot=0, alpha=0.5)
    plt.show()

def drawPie(dataFrame, row, cols):
    '''
        Draw pie plot
        :param dataFrame: The DataFrame of your file
        :param rows: Rows will be shown:
                           + pass a num to display one row
                           + pass an array [num1, num2, num3, ...] to display rows you want
                           + pass a range(start, end) for multiple rows
        :param cols: Cols will be shown:
                           + similar to the rows
        :param row: A int showing the row will be drawn
        :return: Void
    '''
    df = dataFrame.iloc[row, cols]
    df.plot.pie(rot=0)
    plt.show()

def drawStem(dataFrame, rows, cols, linefmt='-.'):
    '''
        Draw stem plot
        :param dataFrame: The DataFrame of your file
        :param rows: Rows will be shown:
                           + pass a num to display one row
                           + pass an array [num1, num2, num3, ...] to display rows you want
                           + pass a range(start, end) for multiple rows
        :param cols: Cols will be shown:
                           + similar to the rows
        :param cols: A int or array showing the column will be drawn
        :param linefmt: A string defining the properties of the vertical lines
        :return: Void
    '''
    df = dataFrame.iloc[rows, cols]
    plt.stem(df, bottom=0, linefmt=linefmt)
    plt.show()

def drawBox(dataFrame, rows, cols):
    '''
        Draw box plot
        :param dataFrame: The DataFrame of your file
        :param rows: Rows will be shown:
                           + pass a num to display one row
                           + pass an array [num1, num2, num3, ...] to display rows you want
                           + pass a range(start, end) for multiple rows
        :param cols: Cols will be shown:
                           + similar to the rows
        :param vert: Horizontal or not
        :return: Void
    '''
    df = dataFrame.iloc[rows, cols]
    plt.boxplot(df, vert=False)
    plt.show()

def drawViolin(dataFrame, cols):
    '''
        Draw violin plot
        :param dataFrame: The DataFrame of your file
        :param cols: Cols will be shown:
                           + pass a num to display one col
                           + pass an array [num1, num2, num3, ...] to display cols you want
                           + pass a range(start, end) for multiple cols
        :return: Void
    '''
    df = dataFrame.iloc[:, cols]
    plt.violinplot(df, vert=False, showmedians=True)
    plt.show()
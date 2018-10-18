import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_rows = 10

def fileVisualizer(path):
    '''
        :param path: Path to your file
        :return: a DataFrame of your file
    '''
    df = pd.read_csv(path)

    print(df)
    print('-' * 50)
    print(df.describe())
    return df

def drawBar(dataFrame, rowsIndex, colsIndex, stacked=False, horizontal=False, alpha=0.5, rot=0):
    '''
        :param dataFrame: the DataFrame of your file
        :param rowsIndex: rows you want to display in your chart:
                           + pass a num to display one row
                           + pass an array [num1, num2, num3, ...] to display rows you want
                           + pass a range(start, end) for multiple rows
        :param colsIndex: cols you want to display in your chart:
                           + similar to the rows
        :param stacked: your bar chart is stacked or not
        :param horizontal: display horizontal bar
        :param alpha: the opacity of the chart
        :param rot: rotation of the xlabel
        :return: void
    '''

    df = dataFrame.iloc[rowsIndex, colsIndex]
    if horizontal:
        plt.show(df.plot.barh(stacked=stacked, alpha=alpha, rot=rot))
    else:
        plt.show(df.plot.bar(stacked=stacked, alpha=alpha, rot=rot))

def drawLine(dataFrame, rowsIndex, colsIndex, alpha=0.5, rot=0):
    '''
        :param dataFrame: the DataFrame of your file
        :param rowsIndex: rows you want to display in your chart:
                           + pass a num to display one row
                           + pass an array [num1, num2, num3, ...] to display rows you want
                           + pass a range(start, end) for multiple rows
        :param colsIndex: cols you want to display in your chart:
                           + similar to the rows
        :param alpha: the opacity of the chart
        :param rot: rotation of the xlabel
        :return: void
    '''
    df = dataFrame.iloc[rowsIndex, colsIndex]
    plt.show(df.plot(alpha=alpha, rot=rot))

def drawHistogram(dataFrame, rowsIndex, colsIndex, bins=50, alpha=0.5, rot=0):
    '''
        :param dataFrame: the DataFrame of your file
        :param rowsIndex: rows you want to display in your chart:
                           + pass a num to display one row
                           + pass an array [num1, num2, num3, ...] to display rows you want
                           + pass a range(start, end) for multiple rows
        :param colsIndex: cols you want to display in your chart:
                           + similar to the rows
        :param bins: number of the bar in the histogram
        :param alpha: the opacity of the chart
        :param rot: rotation of the xlabel
        :return: void
    '''
    df = dataFrame.iloc[rowsIndex, colsIndex]
    plt.show(df.plot.hist(bins=bins, rot=rot, alpha=alpha))
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.display.max_rows = 10

def fileVisualizer(path):
    df = pd.read_csv(path)

    print(df)

    print("Num cols: ", len(df.columns))
    print("Num rows: ", len(df.index))
    print("Labels: ")
    print(df.columns.values)
    return df

def drawBar(dataFrame, cols, start=0, end=10, stacked=False, horizontal=False, alpha=0.5, rot=0):
    df = dataFrame[cols][start:end]
    if horizontal:
        plt.show(df.plot.barh(stacked=stacked, alpha=alpha, rot=rot))
    else:
        plt.show(df.plot.bar(stacked=stacked, alpha=alpha, rot=rot))

def drawLine(dataFrame, cols, start=0, end=10, alpha=0.5, rot=0):
    df = dataFrame[cols][start:end]
    plt.show(df.plot(alpha=alpha, rot=rot))

def drawHistogram(dataFrame, cols, start=0, end=10, bins=50, alpha=0.5, rot=0):
    df = dataFrame[cols][start:end]
    plt.show(df.plot.hist(bins=50, rot=rot, alpha=alpha))
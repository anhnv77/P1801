import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from pandas.plotting import scatter_matrix
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


#   Draw 2D scatter
def scatter_2d(data_frame, col_x, col_y):
    """
        :param data_frame: The data frame of your file
        :param col_x: The first column signed as Ox line
        :param col_y: The second column signed as Oy line
    """

    Ox = data_frame.iloc[:, col_x]
    Oy = data_frame.iloc[:, col_y]
    plt.scatter(Ox, Oy, marker='x', color='r', alpha=0.5)

    # Get names of columns
    label = list(data_frame)

    plt.xlabel(label[col_x])
    plt.ylabel(label[col_y])
    plt.show()


#   Draw 3D scatter
def scatter_3d(data_frame, col_x, col_y, col_z):
    """
        :param data_frame: The data_frame of your file
        :param col_x: the first column signed as Ox line
        :param col_y: the second column signed as Oy line
        :param col_z: the third column signed as Oz line
    """

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    Ox = data_frame.iloc[:, col_x]
    Oy = data_frame.iloc[:, col_y]
    Oz = data_frame.iloc[:, col_z]

    ax.scatter(Ox, Oy, Oz, marker='x', alpha=0.5, color='r')

    # Get names of columns
    label = list(data_frame)

    ax.set_xlabel(label[col_x])
    ax.set_ylabel(label[col_y])
    ax.set_zlabel(label[col_z])
    plt.show()


#	Draw x*y plot in one figure, contain scatter plots and histogram plots (if col_x and col_y are the same)
def scatter_matrix(data_frame, cols_x, cols_y, kind='reg', diag_kind='hist', hue=None):
    """
        :param data_frame: The data frame of your file
        :param cols_x: cols you want to display in your chart by label x_vars:
            + The row of the figure
        :param cols_y: cols you want to display in your chart by label y_vars:
            + The column of the figure
        :param kind: Kind of plot for the non-identity relationships
            + Can pass one of {‘scatter’ |‘reg’}, if pass 'reg' it will add a line represent for linear relationship
        :param diag_kind: Kind of plot for the diagonal subplots
            + Can pass one of {‘auto’ | ‘hist’ | ‘kde’}
        :param hue: Variable in data to map plot aspects to different colors.
        + cols you want to distinguish by colors
    """
    head = data_frame.columns.values
    sb.set()
    sb.pairplot(data_frame, hue=hue, x_vars=head[cols_x], y_vars=head[cols_y],
                kind=kind, diag_kind=diag_kind, markers='x')
    plt.show()


#   A map draws different Frequency areas, are separated by border lines
def frequency_map(data_frame, col_x, col_y, kind="kde"):
    """
        :param data_frame: The data frame of your file
        :param col_x: col you want to display in your chart by label x:
        :param col_y: col you want to display in your chart by label y:
        :param kind: Kind of plot for the diagonal subplots
                + Can pass one of { “scatter” | “reg” | “resid” | “kde” | “hex” }
                +  if pass "reg" it will add a line represent for linear relationship
    """
    head = data_frame.columns.values
    sb.set()
    sb.jointplot(data=data_frame, x=head[col_x], y=head[col_y], kind=kind)
    plt.show()


# A scatter plot with a curly line represent for linear relationship between cols_x and cols_y
def curly_line(data_frame, col_x, col_y, hue=None):
    """
        :param data_frame: The data frame of your file
        :param col_x: col you want to display in your chart by label x:
        :param col_y: col you want to display in your chart by label y:
        :param hue: Variable in data to map plot aspects to different colors.
            + cols you want to distinguish by colors
    """
    head = data_frame.columns.values
    sb.set()
    sb.lmplot(data=data_frame, x=head[col_x], y=head[col_y], hue=hue, order=2)
    plt.show()

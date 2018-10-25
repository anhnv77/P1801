import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pandas.plotting import scatter_matrix


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


def Scatter_2D(dataFrame, _1st_index, _2nd_index):

    '''
    :param dataFrame: all the data you want to visualize
    :param _1st_index: the first attribute signed as Ox line
    :param _2nd_index: the second attribute signed as Oy line
    '''

    color = np.random.rand(3)
    area = 10 ** 2
    plt.scatter(dataFrame.iloc[:,0:_1st_index+1], dataFrame.iloc[:,1:_2nd_index+1], s=area, marker='x',alpha=0.5)

    # get names of attributes
    attributeName = list(dataFrame)

    plt.xlabel(attributeName[_1st_index])
    plt.ylabel(attributeName[_2nd_index])
    plt.show()

def Scatter_3D(dataFrame, _1st_index, _2nd_index, _3rd_index):

    '''
    :param dataFrame: all the data you want to visualize
    :param _1st_index: the first attribute signed as Ox line
    :param _2nd_index: the second attribute signed as Oy line
    :param _3rd_index: the third attribute signed as Oz line
    '''

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    color = np.random.rand(3)
    area = 10 ** 2

    ax.scatter(dataFrame.iloc[:,0:_1st_index+1], dataFrame.iloc[:,1:_2nd_index+1], dataFrame.iloc[:,2:_3rd_index+1],
               s=area, marker='x',alpha=0.5)

    # get names of attributes
    attributeName = list(dataFrame)

    ax.set_xlabel(attributeName[_1st_index])
    ax.set_ylabel(attributeName[_2nd_index])
    ax.set_zlabel(attributeName[_3rd_index])
    plt.show()

def Scatter_Matrix(dataFrame):
    scatter_matrix(dataFrame, alpha=0.2, figsize=(6, 6), diagonal='kde')
    plt.show()



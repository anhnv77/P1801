import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix

def Scatter_2D(dataFrame, _1st_index, _2nd_index):
    '''
    :param dataFrame: All the data you want to visualize
    :param _1st_index: The first attribute signed as Ox line
    :param _2nd_index: The second attribute signed as Oy line
    '''

    area = 10 ** 2
    Ox = dataFrame.iloc[:,0:_1st_index+1]
    Oy = dataFrame.iloc[:,1:_2nd_index+1]
    plt.scatter(Ox, Oy, s=area, marker='x', color = 'r', alpha=0.5)

    # Get names of attributes
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
    area = 10 ** 2
    Ox = dataFrame.iloc[:, 0:_1st_index+1]
    Oy = dataFrame.iloc[:, 1:_2nd_index+1]
    Oz = dataFrame.iloc[:, 2:_3rd_index+1]

    ax.scatter(Ox, Oy, Oz,
               s=area, marker='x', alpha=0.5, color='r')

    # Get names of attributes
    attributeName = list(dataFrame)

    ax.set_xlabel(attributeName[_1st_index])
    ax.set_ylabel(attributeName[_2nd_index])
    ax.set_zlabel(attributeName[_3rd_index])
    plt.show()

	
#	draw x*y plot in one figure, contain scatter plots and histogram plots (if col_x == col_y)
def multiScatter(dataFrame, rows, cols_x, cols_y, kind='reg', diag_kind='hist', hue=None):
	'''
		:param dataFrame: The DataFrame need ploting
		:param rows: Rows you want to display in your chart:
			+ Pass a num: <row> to display one row
			+ Pass an array: <[num1, num2, num3, ...]> to display rows you want
			+ Pass: <range(start, end)>, for multiple rows
		:param Cols_x: cols you want to display in your chart by layber x_vars:
			+ The row of the figure
		:param Cols_y: cols you want to display in your chart by layber y_vars:
			+ The colume of the figure
		:param Kind: Kind of plot for the non-identity relationships
			+ Can pass one of {‘scatter’ |‘reg’}, if pass 'reg' it will add a line represent for linear relationship
		:param Diag_kind: Kind of plot for the diagonal subplots
			+ Can pass one of {‘auto’ | ‘hist’ | ‘kde’}
		:param hue: Variable in data to map plot aspects to different colors.
			+ cols you want to distinguish by colors
	'''

	head = dataFrame.columns.values
	sb.set()
	plt.show(sb.pairplot(dataFrame.iloc[rows,:],hue=hue,x_vars=head[cols_x],y_vars=head[cols_y],kind=kind,diag_kind=diag_kind))

	
#	a map draws different Frequency areas, are separated by border lines
def FrequencyMap(dataFrame, rows, cols_x, cols_y, kind="kde"):
	'''
	:param dataFrame: The DataFrame need ploting
	:param rows: Rows you want to display in your chart:
			+ Pass a num: <row> to display one row
			+ Pass an array: <[num1, num2, num3, ...]> to display rows you want
			+ Pass: <range(start, end)>, for multiple rows
	:param cols_x: cols you want to display in your chart by layber x:
	:param cols_y: cols you want to display in your chart by layber y:
		<<the cols_x size have equal cols_y size>>
	:param kind: Kind of plot for the diagonal subplots
			+ Can pass one of { “scatter” | “reg” | “resid” | “kde” | “hex” }
			+  if pass "reg" it will add a line represent for linear relationship
	'''
	head = dataFrame.columns.values
	sb.set()
	plt.show(sb.jointplot(x=head[cols_x],y=head[cols_y],data=dataFrame.iloc[rows,:],kind=kind))
	
	
#	a scatter plot with a curly line represent for linear relationship between cols_x and cols_y
def linearLine(dataFrame, rows, cols_x, cols_y, hue=None):
	'''
	:param dataFrame: The DataFrame need ploting
	:param rows: Rows you want to display in your chart:
		+ Pass a num: <row> to display one row
		+ Pass an array: <[num1, num2, num3, ...]> to display rows you want
		+ Pass: <range(start, end)>, for multiple rows
	:param cols_x: cols you want to display in your chart by layber x:
	:param cols_y: cols you want to display in your chart by layber y:
		<<the cols_x size have equal cols_y size>>
	:param hue: Variable in data to map plot aspects to different colors.
		+ cols you want to distinguish by colors
	'''
	head = dataFrame.columns.values
	sb.set()
	plt.show(sb.lmplot(x=head[cols_x], y=head[cols_y], data=dataFrame.iloc[rows,:], hue=hue, order=2))

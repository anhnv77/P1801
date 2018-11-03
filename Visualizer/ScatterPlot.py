import matplotlib.pyplot as plt
import seaborn as sb
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

def Scatter_2D(dataFrame, col_x, col_y):
    '''
        Draw 2D scatter
        :param dataFrame: The DataFrame of your file
        :param col_x: The first column signed as Ox line
        :param col_y: The second column signed as Oy line
    '''

    Ox = dataFrame.iloc[:, col_x]
    Oy = dataFrame.iloc[:, col_y]
    plt.scatter(Ox, Oy, marker='x', color = 'r', alpha=0.5)

    # Get names of columns
    columnName = list(dataFrame)

    plt.xlabel(columnName[col_x])
    plt.ylabel(columnName[col_y])
    plt.show()

def Scatter_3D(dataFrame, col_x, col_y, col_z):
    '''
        Draw 3D scatter
        :param dataFrame: The DataFrame of your file
        :param col_x: The first column signed as Ox line
        :param col_y: The second column signed as Oy line
        :param col_z: the third column signed as Oz line
    '''

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    Ox = dataFrame.iloc[:, col_x]
    Oy = dataFrame.iloc[:, col_y]
    Oz = dataFrame.iloc[:, col_z]

    ax.scatter(Ox, Oy, Oz, marker='x', alpha=0.5, color='r')

    # Get names of columns
    columnName = list(dataFrame)

    ax.set_xlabel(columnName[col_x])
    ax.set_ylabel(columnName[col_y])
    ax.set_zlabel(columnName[col_z])
    plt.show()

def Scatter_Matrix(dataFrame, rows, cols_x, cols_y, kind='reg', diag_kind='hist', hue=None):
	'''
		:param rows: Rows you want to display in your chart:
			+ Pass a num: <row> to display one row
			+ Pass an array: <[num1, num2, num3, ...]> to display rows you want
			+ Pass: <range(start, end)>, for multiple rows
		:param cols_x: cols you want to display in your chart by layber x_vars:
			+ The row of the figure
		:param cols_y: cols you want to display in your chart by layber y_vars:
			+ The column of the figure
		:param Kind: Kind of plot for the non-identity relationships
			+ Can pass one of {‘scatter’ |‘reg’}, if pass 'reg' it will add a line represent for linear relationship
		:param Diag_kind: Kind of plot for the diagonal subplots
			+ Can pass one of {‘auto’ | ‘hist’ | ‘kde’}
		:param hue: Variable in data to map plot aspects to different colors.
			+ cols you want to distinguish by colors
		:return: seaborn.axisgrid
	'''

	head = dataFrame.columns.values
	sb.set()
	plt.show(sb.pairplot(dataFrame.iloc[rows,:],hue=hue,x_vars=head[cols_x],y_vars=head[cols_y],kind=kind,diag_kind=diag_kind))
	return sb.pairplot(dataFrame.iloc[rows,:],hue=hue,x_vars=head[cols_x],y_vars=head[cols_y],kind=kind,diag_kind=diag_kind)

def jointplot(dataFrame, rows, cols_x, cols_y, kind="kde"):
	'''
	:param dataFrame: The DataFrame need ploting
	:param rows: Rows you want to display in your chart:
			+ Pass a num: <row> to display one row
			+ Pass an array: <[num1, num2, num3, ...]> to display rows you want
			+ Pass: <range(start, end)>, for multiple rows
	:param cols_x: cols you want to display in your chart by layber x:
			+ The row of the figure
	:param cols_y: cols you want to display in your chart by layber y:
			+ The colume of the figure
	:param kind: Kind of plot for the diagonal subplots
			+ Can pass one of { “scatter” | “reg” | “resid” | “kde” | “hex” }
			+  if pass "reg" it will add a line represent for linear relationship
	:return: seaborn.axisgrid
	'''
	head = dataFrame.columns.values
	sb.set()
	plt.show(sb.jointplot(x=head[cols_x],y=head[cols_y],data=dataFrame.iloc[rows,:],kind=kind))
	return sb.jointplot(x=head[cols_x],y=head[cols_y],data=dataFrame.iloc[rows,:],kind=kind)

def lmplot(dataFrame, rows, cols_x, cols_y, hue=None):
	'''
		:param dataFrame: The DataFrame need ploting
		:param rows: Rows you want to display in your chart:
			+ Pass a num: <row> to display one row
			+ Pass an array: <[num1, num2, num3, ...]> to display rows you want
			+ Pass: <range(start, end)>, for multiple rows
		:param cols_x: cols you want to display in your chart by layber x_vars:
			+ The row of the figure
		:param cols_y: cols you want to display in your chart by layber y_vars:
			+ The colume of the figure
		:param hue: Variable in data to map plot aspects to different colors.
			+ cols you want to distinguish by colors
		:return: seaborn.axisgrid
	'''
	head = dataFrame.columns.values
	sb.set()
	plt.show(sb.lmplot(x=head[cols_x], y=head[cols_y], data=dataFrame.iloc[rows,:], hue=hue, order=2))
	return sb.lmplot(x=head[cols_x], y=head[cols_y], data=dataFrame.iloc[rows,:], hue=hue, order=2)

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def pairplot(dataFrame, rowsIndex = np.arange(50), colsIndex_x=None,
			 colsIndex_y=None, height=2.5, aspect=1, kind='reg', diag_kind='hist', dropna=True):
	'''
        :param dataFrame: the DataFrame need ploting
        :param rowsIndex: rows you want to display in your chart:
			+ pass a num: <row> to display one row
            + pass an array: <[num1, num2, num3, ...]> to display rows you want
			+ pass: <range(start, end)>, for multiple rows
			+ default = arange(0,50), The first 50 rows from 0 to 49
        :param colsIndex_x: cols you want to display in your chart by layber x_vars:
			+ the row of the figure
			+ default = all the cols in dataframe
        :param colsIndex_y: cols you want to display in your chart by layber x_vars:
			+ the row of the figure
			+ default = all the cols in dataframe
		:param height: a num which is height of each facet
		:param aspect: a num, (Aspect * height) gives the width of each facet
		:param kind: Kind of plot for the non-identity relationships
			+ can pass one of {‘scatter’, ‘reg’}, if pass 'reg' it will add a line represent for linear relationship
		:param diag_kind : Kind of plot for the diagonal subplots
						+ can pass one of {‘auto’, ‘hist’, ‘kde’}, 'auto' and 'hist' is the same
		:param dropna : boolean type, drop missing values from the data before plotting.
						+ True for drop missing values from the data before plotting.
						+ default: True
        :return: void
    '''
	head = dataFrame.columns.values
	if colsIndex_x==None:
		colsIndex_x = np.arange(len(head))
	if colsIndex_y==None:
		colsIndex_y = np.arange(len(head))
	sns.pairplot(dataFrame.iloc[rowsIndex,:],x_vars=head[colsIndex_x], y_vars=head[colsIndex_y],height=height,aspect=aspect,kind=kind,diag_kind=diag_kind,dropna=dropna)
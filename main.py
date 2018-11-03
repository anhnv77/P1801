import Visualizer.BasicPlot as vsl
import Visualizer.ScatterPlot as sct
import numpy as np

df = vsl.fileVisualizer('data/housing.csv')

cols = range(3)
rows = range(10)

'''Draw barh chart plot with cols=cols, rows=rows and stacked'''
#vsl.drawBar(df, rows, cols, True, True)

'''Draw line chart plot with cols=cols and rows=rows'''
#vsl.drawLine(df, rows, cols)

'''Draw histogram chart plot with cols[0] and rows[0:max]'''
#vsl.drawHistogram(df, cols, 50)

'''Draw pie plot with cols=cols and row[1]'''
#vsl.drawPie(df, 1, cols)

'''Draw stem plot with col[0] and rows=rows'''
#vsl.drawStem(df, rows, 0)

'''Draw box plot with col[0] and rows=rows'''
#vsl.drawBox(df, rows, 0)

'''Draw violin plot with col[0] and rows[0:max]'''
#vsl.drawViolin(df, 0)

'''Draw 2D scatter plot with Ox:col[0] and Oy:col[1]'''
#sct.Scatter_2D(df, 0, 1)

'''Draw 3D scatter plot with Ox:col[0], Oy:col[1] and Oz:col[2]'''
#sct.Scatter_3D(df, 0, 1, 2)

'''Draw multi scatter in a figure with rows=[:50] Ox:cols[0,1,2], Oy:cols[0,1,2]'''
#sct.Multi_Scatter(df, np.arange(50), [0,1,2], [0,1,2])

'''Draw frequency map with rows=[:50] Ox:col[0], Oy:cols[1]'''
#sct.Frequency_Map(df, np.arange(50), 0, 1)

'''Draw scatter with curly linear line with rows=[:50] Ox:col[0], Oy:cols[3]'''
#sct.Curly_Linear_Line(df, np.arange(50), 0, 3)

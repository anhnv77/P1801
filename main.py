import Visualizer.BasicPlot as vsl
import Visualizer.ScatterPlot as sct

df = vsl.visualizer('data/housing.csv')

cols = range(3)
rows = range(20)

'''Draw horizontal bar chart plot with cols=cols, rows=rows and stacked'''
# vsl.draw_bar(df, rows, cols, True, True)

'''Draw line chart plot with cols=cols and rows=rows'''
# vsl.draw_line(df, rows, cols)

'''Draw histogram chart plot with cols'''
# vsl.draw_hist(df, cols, 50)

'''Draw pie plot with cols=cols and row[1]'''
# vsl.draw_pie(df, 1, cols)

'''Draw stem plot with col[0] and rows=rows'''
# vsl.draw_stem(df, rows, 0)

'''Draw box plot with col[0] and rows=rows'''
# vsl.draw_box(df, rows, 0)

'''Draw violin plot with col[0]'''
# vsl.draw_violin(df, 0)

'''Draw 2D scatter plot with Ox:col[0] and Oy:col[1]'''
# sct.scatter_2d(df, 0, 1)

'''Draw 3D scatter plot with Ox:col[0], Oy:col[1] and Oz:col[2]'''
# sct.scatter_3d(df, 0, 1, 2)

'''Draw matrix scatter with Ox:cols, Oy:cols'''
# sct.scatter_matrix(df, cols, cols)

'''Draw frequency map with Ox:col[0], Oy:cols[1]'''
# sct.frequency_map(df, 0, 1)

'''Draw scatter with curly linear line with Ox:col[0], Oy:cols[3]'''
# sct.curly_line(df, 0, 3)

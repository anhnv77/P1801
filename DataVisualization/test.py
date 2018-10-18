import DataVisualization.DrawChart as vsl #visualizer

df = vsl.fileVisualizer("data/housing.csv")

#Draw barh chart plot with cols[0:3], rows[0:10] and stacked
#vsl.drawBar(df, range(10), range(3), True, True)

#Draw line chart plot with cols[0:3] and rows[0:10]
#vsl.drawLine(df, range(10), range(3))

#Draw histogram chart plot with cols[0] and rows[0:max]
vsl.drawHistogram(df, range(len(df.index)), 0, 50)  
import DataVisualization.DrawChart as draw

df = draw.fileVisualizer("data/housing.csv")

#Draw barh chart plot with cols[0:3], rows[0:10] and stacked
#draw.drawBar(df, range(10), range(3), True, True)

#Draw line chart plot with cols[0:3] and rows[0:10]
#draw.drawLine(df, range(10), range(3))

#Draw histogram chart plot with cols[0] and rows[0:max]
draw.drawHistogram(df, range(len(df.index)), 0, 50)
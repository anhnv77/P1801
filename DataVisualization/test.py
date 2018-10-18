import DataVisualization.DrawChart

df = DataVisualization.DrawChart.fileVisualizer("data/housing.csv")
#DataVisualization.DrawChart.drawBar(df, ['RM', 'LSTAT', 'PTRATIO'], 0, 9, True, True)
#DataVisualization.DrawChart.drawLine(df, ['RM', 'LSTAT', 'PTRATIO'])
DataVisualization.DrawChart.drawHistogram(df, 'MEDV', 0, 489)
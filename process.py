import pandas as pd 
import matplotlib.pyplot as plt 

def plotAll(df):
	df.plot()
	plt.title('Rainfall and Departure Percentage:NE-INDIA,1901-2016')
	# plt.legend(bbox_to_anchor=(1.05, 1.0, 0.3, 0.2), loc='upper left')
	plt.show()

def plotRecent10Years(df):
	df = df.tail(10)
	df.plot()
	plt.title('Rainfall and Departure Percentage:NE-INDIA,2007-2016')
	plt.show()

def plotSpecificYears(df):
	yStart = int(input('Enter the start year:'))
	yEnd = int(input('Enter the end year:'))
	df = df.loc[yStart:yEnd, ['Actual Rainfall: JUN', 'Actual Rainfall: JUL', 'Actual Rainfall: AUG', 'Actual Rainfall: SEPT', 'Actual Rainfall: JUN-SEPT']]
	df.plot()
	plt.title(f"Rainfall for: {yStart}-{yEnd}")
	plt.show()


if __name__=='__main__':
	rainfallDf = pd.read_csv('D:\\Python\\matplotlib\\Rainfall\\ne-India_rainfall_act_dep_1901_2016.csv', index_col=0)
	plotAll(rainfallDf)
	plotRecent10Years(rainfallDf)
	plotSpecificYears(rainfallDf)
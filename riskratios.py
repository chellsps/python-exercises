import pandas as pd
import numpy as np
import pandas_datareader.data as web
from datetime import date

class RiskRatios:
	
	def __init__(self, symbol):
		self.symbol = symbol
		self.start = date(2017,1,1)
		self.stop = date.today()
		self.data = self.get_data()
		self.returns = self.calculate_returns()
		self.covariance = self.calculate_covariance()
		self.beta = self.calculate_beta()
		self.alpha = self.calculate_alpha()
		# self.r_squared = calculate_r_squared()

	def get_data(self):
		portfolio = ['SPY', self.symbol]
		raw_data = pd.DataFrame()
		for s in portfolio:
			raw_data[s] = web.DataReader(s, 'google', self.start, self.stop)['Close']
		# print(raw_data.head())
		return raw_data

	def calculate_returns(self):
		returns = np.log(self.data/self.data.shift(1))
		returns = returns.dropna() # Dropna is a specific function for pandas library to remove NA values
		# print(returns.head())
		return returns

	def calculate_covariance(self):
		covariance = np.cov(self.returns.SPY, self.returns[self.symbol])
		return covariance

	def calculate_beta(self):
		beta = self.covariance[0,1]/np.var(self.returns.SPY)
		return beta

	def calculate_alpha(self):
		alpha = np.mean(self.returns[self.symbol]) - (self.beta * np.mean(self.returns.SPY))
		return alpha

	def calculate_r_squared(self):
		corr_coefficient = self.alpha + (self.beta * self.returns.SPY)
		square_correlation = np.sum(np.power(corr_coefficient - self.returns.SPY, 2))
		sum_of_squares = self.covariance[0,0] * (len(self.returns)-1)
		r_squared = 1 - square_correlation/sum_of_squares
		return r_squared

def main():
	TMPL = '''
	STOCK: %s
	BETA: %s
	ALPHA: %s
	R SQUARED: %s
	'''

	stock_symbol = input("Please enter a stock symbol: ")
	b = RiskRatios(stock_symbol)
	alpha = (b.calculate_alpha())*252
	print(TMPL % (stock_symbol, b.calculate_beta(), alpha, b.calculate_r_squared()))


if __name__ == '__main__':
	main()
	# b.get_data()
	# b.calculate_returns()
	# b.calculate_r_squared()
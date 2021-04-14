from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

x = np.array([1,2,3,4,5,6], dtype = np.float64)
y = np.array([5,4,6,5,6,7], dtype = np.float64)

def slope_and_y_intercept(x,y):
	m = ((mean(x) * mean(y)) - mean(x*y)) / ((mean(x) * mean(x)) - (mean(x*x)))
	y_intercept = mean(y) - m*(mean(x))
	return m, y_intercept

m, b = slope_and_y_intercept(x,y)

def squared_error(y_original, y_line):
	#squared error is the differece between original y value and the value of y we got through the regression
	return sum((y_original - y_line) ** 2)


def coefficient_of_determination(y_original, y_line):
	y_mean_line = [mean(y_original) for y in y_original]
	squared_error_regression = squared_error(y_original,y_line)
	squared_error_mean = squared_error(y_original,y_mean_line)
	return 1 - (squared_error_regression/squared_error_mean)

regression_line = [(m*xvalue) + b for xvalue in x]


r_squared = coefficient_of_determination(y,regression_line)

print(r_squared)

plt.scatter(x,y)
plt.plot(x, regression_line)
plt.show()

#the next problem to think of is how accurate our regression is
'''
coefficient of determination:
r*r = 1 - (SE(y-hat) / SE(mean(y)))

the more the value of r*r, the more accurate it is


'''
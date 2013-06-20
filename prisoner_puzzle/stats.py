from prisoner_puzzle import monte_carlo
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def example_stats():
  number_of_experiments = 500
  number_of_prisoners = 50
  results = monte_carlo(number_of_experiments, number_of_prisoners)
  #Calculate some statistics:
  minimum = min(results)
  maximum = max(results)
  median = (maximum - minimum)/2.0 + minimum
  mean = np.mean(results)

  string = "The simulation with {} results took an average of {} days  \
    or {} months or {} years to finish."
  print(string.format(number_of_experiments, mean, mean/12, mean/365.0))

  #what's the spread?
  print "max:", maximum
  print "min:", minimum

  #where does the mean fall within that spread?
  print "mean:", mean
  print "median:", median
  print "distance from mean to median:", mean - median

  #how broad is the peak?
  standard_deviation = np.std(results)

  print "standard deviation:", standard_deviation

  #Plot a histogram
  histogram_data = plt.hist(results, bins=30)
  plt.vlines(
    median, 
    0, 
    max(histogram_data[0]), 
    linestyles='dashed', 
    lw = 4, 
    label = "median", 
    color='red')
  plt.vlines(
    mean, 
    0, 
    max(histogram_data[0]), 
    linestyles='dashed', 
    lw = 4, 
    label = "mean", 
    color='orange')
  plt.title("Prisoner Escape Riddle Historgram, n={}".format(number_of_experiments))
  plt.xlabel("Number of days to escape")
  plt.ylabel("Frequency")
  plt.legend()
  plt.show()

#How quickly does the mean converge as number_of_experiments increases?
x_values = [] # number_of_experiments
y_values = [] # average value at each number_of_experiments
number_of_prisoners = 50
for n in range(1,51):
  print n
  x_values.append(n)
  mean = np.mean(monte_carlo(n, number_of_prisoners))
  y_values.append(mean)

plt.scatter(x_values, y_values)
plt.title("Convergence of Mean Value, number_of_prisoners = {}".format(number_of_prisoners))
plt.xlabel("Number of experiments")
plt.ylabel("Days to prisoner release")
#plt.savefig("convergence.png")

def line(slope, intercept, x):
  a = intercept
  b = slope
  y = a + b * x
  return y
slope, intercept, r_value, p_value, std_err = stats.linregress(x_values,y_values)
x_line_points = np.arange(1,51,1)
y_line_points = []
for x in x_line_points:
  y_line_points.append(line(slope, intercept, x))
y_line_points = np.array(y_line_points)
y_values = np.array(y_values)
plt.plot(x_line_points, y_line_points)
plt.vlines(x_values, y_line_points, y_values)
sum_of_distances = sum(abs(y_values - y_line_points))
plt.suptitle("Sum of distances: {}".format(sum_of_distances))
plt.show()
  
'''
#if we increase the number of prisoners, does the mean increase linearly?
for number_of_prisoners in range(1,51):
  print(
    "Prisoners:", number_of_prisoners, 
    "Mean:", mean(monte_carlo(500,number_of_prisoners)))
'''

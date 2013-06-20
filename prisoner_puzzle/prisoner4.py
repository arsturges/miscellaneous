# Iteration 4: Monte Carlo simulator to method; parameterize no. of prisoners 
# and no. of runs; prettify output
from numpy import array, mean
import random

def run_simulation(number_of_prisoners):
  counter = 0
  day_number = 0
  prisoner_chief = 1
  lever_position = 'down'
  prisoners_who_have_operated_lever = []

  while counter < number_of_prisoners:
    prisoner_number = random.randint(1,number_of_prisoners) # Select a prisoner
    if not prisoner_number in prisoners_who_have_operated_lever:
      if lever_position == 'down':
        prisoners_who_have_operated_lever.append(prisoner_number)
        lever_position = 'up'
    if prisoner_number == prisoner_chief:
      if lever_position == 'up':
          lever_position = 'down'
          counter += 1
    day_number += 1
  return day_number 

def monte_carlo(number_of_experiments, prisoner_count):
  simulation_results = []
  simulations = 0
  while simulations < number_of_experiments:
    simulation_results.append(run_simulation(prisoner_count))
    simulations += 1
  simulation_results = array(simulation_results) #convert to numpy array
  return simulation_results

monte_500 = monte_carlo(500,50)
average = mean(monte_500)
print("The simulation with {} results took an average of {} days or {} months or {} years to finish.".format(500, average, average/12, average/365.0))

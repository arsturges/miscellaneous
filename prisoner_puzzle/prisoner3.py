#Iteration 3: Loop it to run 1000 times
import random
import numpy

def run_simulation():
  counter = 0
  day_number = 0
  prisoner_chief = 1
  lever_position = 'down'
  prisoners_who_have_operated_lever = []

  while counter < 50:
    prisoner_number = random.randint(1,50) # Select a prisoner
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

simulation_results = []
simulations = 0
while simulations < 1000:
  simulation_results.append(run_simulation())
  simulations += 1
simulation_results = numpy.array(simulation_results)
print numpy.mean(simulation_results)

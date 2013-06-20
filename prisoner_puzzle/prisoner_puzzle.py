#The Riddle:
''' There are 50 prisoners, and one prison keeper. 
The prisoners will be placed in separate cells, never able to communicate.
Once per day, the prison keeper will randomly select one prisoner and take 
him into a room with two levers.
The levers have two positions each: Up, and down.
The prisoner may operate the levers however he wishes,
then he must return to his cell.
The prisoners have one chance to indicate to the prison keeper whether
all the prisoners have been in the lever-room.
If they indicate too early, they will never be released.
If they're correct (even if they're late), they will be released immediately.
The prisoners get one chance to meet prior to imprisonment, to discuss strategy.
How can they ensure their release?
'''

#The Answer:
'''Elect one prisoner to be a 'counter.' 
When a prisoner enters the lever room and the lever is in the 'down' 
position and he has never moved the lever, then and only then will he move
the lever to the 'up' position.
Only the 'counter' prisoner may return the lever to the 'down' position,
and each time he does so he increments a counter. 
When the counter reaches 50, he knows that all prisoners have been into
the lever room at least once. He can then inform the prison guard,
and all the prisoners will be released.'''

#The challenge:
''' Do a Monte Carlo simulation to find out how long it would take, on average, 
for the prisoners to get released. '''

import numpy
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
    if simulations % 500 == 0:
        pass#print simulations
    simulation_results.append(run_simulation(prisoner_count))
    simulations += 1
  simulation_results = numpy.array(simulation_results) #convert to numpy array
  return simulation_results

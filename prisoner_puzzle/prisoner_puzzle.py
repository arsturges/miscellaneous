'''
50 prisoners, one prison keeper. 
The prisoners get once chance to meet prior to imprisonment. 
They are placed in separate cells, never again being able to communicate.
Once per day, the prison keeper randomly selects one prisoner and takes 
him into a room with two levers.
The levers have two positions each: Up, and down.
The prisoner may operate the levers however he wishes. 
Then he must return to his cell.
The prisoners have one chance to indicate to the prison keeper whether 
all the prisoners have been in the lever-room.
If they indicate too early, they're never released. 
If they're correct (including late), they will be released.

Do a Monte Carlo to simulate how long it would take, on average, to get released.
'''

from numpy import array, std
import random
def run_simulation():
	counter = 0
	day_number = 0
	prisoner_chief = 1
	lever_position = 'down'
	prisoners_who_have_operated_lever = []

	while counter < 50:
		day_number += 1
		prisoner_number = random.randint(1,50) # Select a prisoner
		if not prisoner_number in prisoners_who_have_operated_lever:
			if lever_position == 'down':
				prisoners_who_have_operated_lever.append(prisoner_number)
				lever_position = 'up'
		if prisoner_number == prisoner_chief:
			if lever_position == 'up':
					lever_position = 'down'
					counter += 1
	return day_number 

simulation_results = []
simulations = 0
number_of_experiments = 500
while simulations < number_of_experiments:
	simulation_results.append(run_simulation())
	simulations += 1

nparray = array(simulation_results)
print "max:", max(simulation_results)
print "min:", min(simulation_results)
average = sum(simulation_results)/len(simulation_results)
print "The simulation with {} results took an average of {} days or {} months or {} years to finish.".format(number_of_experiments, average, average/12, average/365.0)
print "standard deviation:", std(nparray)

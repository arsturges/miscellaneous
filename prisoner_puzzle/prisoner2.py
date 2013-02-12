#Iteration 2: Wrapping the simulation in a function
import random

def run_simulation():
  day_number = 0
  prisoner_designee = 1 # chosen by prisoners to be the official counter
  counter = 0 # as tracked by the prisoner_designee
  lever_position = 'down' # starting position of the lever
  prisoners_who_have_operated_lever = []

  while counter < 50:
    prisoner_number = random.randint(1,50)    # Select a prisoner
    if not prisoner_number in prisoners_who_have_operated_lever:
      if lever_position == 'down':
        prisoners_who_have_operated_lever.append(prisoner_number)
        lever_position = 'up'
    if prisoner_number == prisoner_designee:  # If it's the designee...
      if lever_position == 'up':              # ...and the lever is up...
          lever_position = 'down'             # ...put the lever back down...
          counter += 1                        # ...and increment the counter.
    day_number += 1
  return day_number

print run_simulation()

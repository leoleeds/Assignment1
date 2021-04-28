"""Import Libraries and Frameworks"""

import random # import the random library
import operator # import the operator package
import matplotlib.pyplot # import the Matplotlib library
import agentframework # import the agent framework
import time # import the time library

"""Initial Setup"""

start = time.time() # start time counter

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5 # continuing the above

num_of_agents = 10 # this limits the number of agents
num_of_iterations = 100
agents = [] # this creates an empty list

"""Make the Agents"""

for i in range(num_of_agents): # this fills the list of agents
    agents.append(agentframework.Agent()) # based on the agentframework.py

"""Move the Agents"""

for j in range (num_of_iterations):
    for i in range (num_of_agents):
         agents[i].move()

"""Generate Scatter Graph"""

matplotlib.pyplot.ylim(0, 99) # define the axes for the scatter plot
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y) # add each agent
matplotlib.pyplot.show() # display the scatter plot

"""Distance Between Agents"""

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b) 
        
"""Verify that agentframework imported correctly"""

a = agentframework.Agent() 
print(a.y, a.x) # show original agents
a.move()
print(a.y, a.x) # show moved agents

"""Check Timing"""

end = time.time() # end time counter
print(end - start) # processing time in seconds
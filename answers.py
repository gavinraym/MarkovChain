import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from MarkovChain import MarkovChain 

##### 1. Find the state of land use in 2009 and 2014,
##### assuming that the transition probabilities
##### for 5-year intervals are given by the matrix
##### A and remain practically the same over the 
##### time considered.

A = np.array([
    [.7,.1,0],
    [.2,.9,.2],
    [.1,0,.8]
])

starting_state = np.array([.25,.2,.55])

#mc = MarkovChain(A, starting_state)

##### year 2009 and 2014 will print to terminal 
##### at the 1 and 2 indexes

#print(mc)

##### 2. Suppose that all of the land in the city
#####  starts as residential. Use the transition
#####  matrix to plot how the usage of the other 
##### three land types evolves over time.

#mc.start_state = np.array([0,0,1])
#plt.show(mc.plot()) 

##### 3. Do the same as above for both an all 
##### industrial and an all commercial starting 
##### point. How does the long term makeup of the
##### city differ for different starting points?

#res = MarkovChain(A, np.array([0,0,1]), links=15)
#ind = MarkovChain(A, np.array([0,1,0]), links=15)
#com = MarkovChain(A, np.array([1,0,0]), links=15)

#print(f'\n' 
#    f'Residential only:\n{res.df().tail(1)}\n\n'
#    f'Industrial only:\n{ind.df().tail(1)}\n\n'
#    f'Commercial only:\n{com.df().tail(1)}\n\n'
#)

#res.plot()
#ind.plot()
#com.plot()
#plt.show()








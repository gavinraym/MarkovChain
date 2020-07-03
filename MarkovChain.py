import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class MarkovChain(object):
    '''Create a Markov Chain object for simple Markov Chain analysis.
    Initialize with np.arrays for rules and state.'''
    def __init__(self, probabilistic_rules, start_state, links=5, deci=2,
                group_label=[]):
        # Each chain is created with a set of rules that 
        # represent how each category changes over a period 
        # of time. This should not be changed once the chain 
        # is created. If a chain with different rules is desired,
        # a new chain shoud be made with those rules.
        self._prob = probabilistic_rules
        # [starting_state] refers to the state of the chain at 
        # the starting point. i.e. where is each category at 
        # year zero. This can be changed to allow for better
        # exploration of data.
        self.start_state = start_state
        # [steps] allows user to change number of links in chain.
        # Data returned will include original state + steps
        # i.e, default steps=5 will return 6 states.
        self.links = links
        # [round] sets how many decimal places to use when rounding
        self.deci = deci
        # [group_label] accepts a list for labeling each probabilistic
        # group. Will add default 'Group#' label for unnamed groups.
        self.group_label = group_label
        while len(self.group_label) < len(probabilistic_rules):
            self.group_label.append(f'Group{str(len(group_label)+1)}')

    def __str__(self):
        '''Prints to terminal'''
        print('---------------------------------------------------')
        print(self._states())
        return '---------------------------------------------------'

    def _states(self):
        ''' Returns pd.DataFrame representing states of chain.'''
        # Data is made into a list of lists first to allow for clean
        # insert into the pd.DataFrame
        data = [self.start_state.tolist()]
        for _ in range(self.links):
            # Find new state
            new_state = np.dot(self._prob, data[-1])
            # Round each value and add to data set
            data.append([round(_, self.deci) for _ in new_state.tolist()])
        return pd.DataFrame(data, columns=self.group_label)

    def plot(self):
        '''Uses .plt to create graph. Graph is returned.'''
        plt.style.use('seaborn-darkgrid')
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(self._states())
        ax.set_ylabel('Scope of Study (%)')
        ax.set_xlabel('The passage of time...')
        ax.set_yticks([])
        ax.legend(self.group_label)
        # Figure is returned, not displayed. This is to allow the user
        # to make personalized changes to the graph before displaying.
        return fig

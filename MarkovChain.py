import numpy as np

class MarkovChain(object):
    def __init__(self, state, start_perc):
        self._state = state
        self._start_perc = start_perc

    @property
    def state(self):
        

    def data(self, i=1):
        perc = self._start_perc
        data = [perc.tolist()]
        for _ in range(i):
            perc = np.dot(self._state, perc)
            data.append([round(_, 5) for _ in perc.tolist()])
        return data

if __name__ == '__main__':

    transition_probability = np.array([[.7,.1,0],
                                        [.2,.9,.2],
                                        [.1,0,.8]])
    
    starting_percent = np.array([.25, .2, .55])

    markov_chain = MarkovChain(transition_probability, starting_percent)
    print(markov_chain.data(5))

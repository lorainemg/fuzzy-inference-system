import matplotlib.pyplot as plt

class Adjective:
    """Describes a variable with memebership functions"""
    def __init__(self, name:str, membership_func):
        self.name = name
        self.func = membership_func

    def __str__(self):
        return self.name

class Variable:
    """Linguistic var has underlying fuzzy sets / membership funcs associated
    with it."""
    def __init__(self, name:str, *adjectives):
        self.adjectives = adjectives
        self.name = name
        self.value = None

    def __str__(self):
        return self.name

    def type(self, value):
        'Given a value, returns the adjective that best represent it'
        max_value = -1
        ajective = None
        for adj in self.adjectives:
            x = adj.func(value)
            if x > max_value:
                max_value = x
                adjective = adj
        return adjective
    
    def plot(self, sample):
        'Plot the adjective functions'
        fig = plt.figure()
        for adj in self.adjectives:
            y = [adj.func(x) for x in sample]
            plt.plot(sample, y)
        plt.legend([adj.name for adj in self.adjectives])
        fig.savefig(f'img/{self.name}')
        plt.close(fig)
import numpy as np

class Mamdani:
    def __init__(self, rules, variables, adjectives, domain, precision):
        for rule in rules:
            rule.parse(variables, adjectives)
        self.rules = rules
        self.start, self.end = domain
        self.precision = precision

    def evaluate(self, values):
        results = [rule.evaluate(values) for rule in self.rules]
    
        sample = []
        membership = []
        for x in np.arange(self.start, self.end, self.precision):
            sample.append(x)
            y = 0
            for rule, result in zip(self.rules, results):
                y = max(y, min(rule.consequent.func(x), result))
            membership.append(y)
        return sample, membership


class Larsen:
    def __init__(self, rules, variables, adjectives, domain, precision):
        for rule in rules:
            rule.parse(variables, adjectives)
        self.rules = rules
        self.start, self.end = domain
        self.precision = precision

    def evaluate(self, values):
        results = [rule.evaluate(values) for rule in self.rules]
        
        sample = []
        membership = []
        for rule, result in zip(self.rules, results):
            for x in np.arange(self.start, self.end, self.precision):
                y = rule.consequent.func(x) * result
                if not x in sample:
                    sample.append(x)
                    membership.append(y)
                else:
                    i_x = sample.index(x)
                    membership[i_x] = max(membership[i_x], y)
        return sample, membership

class TSK:
    def __init__(self, rules, variables, adjectives, domain, precision):
        for rule in rules:
            rule.parse(variables, adjectives)
        self.rules = rules
        self.start, self.end = domain
        self.precision = precision

    def evaluate(self, values):
        results = [rule.evaluate(values) for rule in self.rules]

        sample = []
        membership = []
        for rule, result in zip(self.rules, results):
            for x in np.arange(self.start, self.end, self.precision):
                for y in np.arange(self.start, self.end, self.precision):
                    numerator += result*rule.consequent.func(x, y)
                    denominator += result
        return numerator / denominator
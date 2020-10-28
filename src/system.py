from aggregation import Mamdani, Larsen
from defuzzification import *
from linguistic_var import Adjective, Variable
import numpy as np

class FuzzyInferenceSystem:
    aggr_methods = {
        'mamdani': Mamdani,
        'larsen': Larsen
    }
    defuz_methods = {
        'mean_of_max': mean_of_max,
        'left_of_max': left_of_max,
        'right_of_max': right_of_max,
        'median_of_max': median_of_max,
        'centroid': centroid,
        'bisector': bisector_of_area
    }

    def __init__(self, aggr_mth:str, defuz_mth:str):
        self.aggr_mth = self.aggr_methods[aggr_mth.lower()]
        self.defuz_mth = self.defuz_methods[defuz_mth.lower()]

    def infer(self, rules, variables, adjectives, domain, precision):
        self.variables = variables
        self.start, self.end = domain
        self.precision = precision
        self.rules = rules
        self.aggregation = self.aggr_mth(rules, variables, adjectives, domain, precision)
    
    def evaluate(self, inputs):
        inputs = self._process_inputs(inputs)
        sample, membership = self.aggregation.evaluate(inputs)
        return self.defuz_mth(sample, membership), sample, membership

    def _process_inputs(self, inputs):
        results = {}
        for var_name, var_value in inputs.items():
            name = var_name.name if isinstance(var_name, Variable) else var_name
            if isinstance(var_value, Adjective):
                # Finds the maximum value of that adjective function
                sample = np.arange(self.start, self.end, self.precision)
                y = map(var_value.func, sample)
                max_tuple = max(zip(sample, y), key=lambda x: x[1])
                value = max_tuple[0]
            else:
                value = var_value
            results[name] = value
        return results
            
                
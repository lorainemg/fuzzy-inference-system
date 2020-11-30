from aggregation import Mamdani, Larsen
from defuzzification import *
from linguistic_var import Adjective, Variable
from rule import Rule
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
        self.adjectives = adjectives
        self.start, self.end = domain
        self.precision = precision
        blocks_rules = self.separate_rules(rules)
        self.aggregations = []
        for out_put_var, rules in blocks_rules.items():
            self.aggregations.append(self.aggr_mth(rules, variables, adjectives, domain, precision, out_put_var))
    
    def separate_rules(self, rules):
        blocks = {}
        for rule in rules:
            consequents = rule.consequent_str.split('and')
            for consequent in consequents:
                rule = Rule(rule.antecedent_str + 'then' + consequent)
                rule.parse(self.variables, self.adjectives)
                try: 
                    blocks[rule.consequent.variable.name].append(rule)
                except:
                    blocks[rule.consequent.variable.name] = [rule]
        return blocks

    def evaluate(self, inputs):
        inputs = self._process_inputs(inputs)
        outputs = {}
        for aggr in self.aggregations:
            sample, membership = aggr.evaluate(inputs)
            value = self.defuz_mth(sample, membership) 
            outputs[aggr.out_var] = {
                'value': value, 
                'sample': sample, 
                'membership': membership}
        return outputs

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
            
                
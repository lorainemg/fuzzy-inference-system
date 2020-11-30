from system import FuzzyInferenceSystem
from membership import Triangular, Trapezoidal, Singleton
from rule import Antecedent, Consequent, Rule
from linguistic_var import Adjective, Variable
import matplotlib.pyplot as plt


near = Adjective('near', Trapezoidal(-1, 0, 1, 10))
medium = Adjective('medium', Triangular(1, 10, 40))
far = Adjective('far', Trapezoidal(10, 40, 50, 60))

left = Variable('left', near, medium, far)
right = Variable('right', near, medium, far)
center = Variable('center', near, medium, far)

low = Adjective('low', Trapezoidal(0, 0.10, 0.30, 0.40))
normal = Adjective('normal', Triangular(0.30, 0.40, 0.60))
high = Adjective('high', Triangular(0.50, 0.80, 0.90))
very_high = Adjective('very_high', Trapezoidal(0.60, 0.80, 1, 1.2))

plausibility_left = Variable('pl', low, medium, high, very_high)
plausibility_right = Variable('pr', low, medium, high, very_high)
plausibility_center = Variable('pc', low, medium, high, very_high)

adjectives = {value.name: value for var_name, value in locals().items() if isinstance(value, Adjective)}
variables = {value.name: value for var_name, value in locals().items() if isinstance(value, Variable)}


rule1 = Rule('if left is near then '
            'pl is normal')
rule2 = Rule('if left is medium then '
            'pl is high')
rule3 = Rule('if left is far then '
            'pl is low')
rule4 = Rule('if left is near and center is near then '
            'pl is low')
rule5 = Rule('if left is medium and center is medium then '
            'pl is low')
ruleBlock1 = [rule1, rule2, rule3, rule4, rule5]


rule6 = Rule('if center is near then '
            'pc is normal')
rule7 = Rule('if left is near and center is near and right is near then '
            'pc is high')
rule8 = Rule('if center is far then '
            'pc is low')
rule9 = Rule('if left is far and center is far then '
            'pc is high')
rule10 = Rule('if left is medium then '
            'pc is high')
rule11 = Rule('if left is medium and center is far then '
            'pc is low')
rule12 = Rule('if right is medium and center is far then '
            'pc is low')
rule13 = Rule('if left is medium and center is medium and right is medium then '
            'pc is very_high')
ruleBlock2 = [rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13]


rule14 = Rule('if right is near then '
            'pr is normal')
rule15 = Rule('if right is medium then '
            'pr is high')
rule16 = Rule('if right is far then'
            'pr is low')  
rule17 = Rule('if right is near and center is near then'
            'pr is low') 
rule18 = Rule('if right is medium and center is medium then'
            'pr is low')  
ruleBlock3 = [rule14, rule15, rule16, rule17, rule18]

rules = ruleBlock1 + ruleBlock2 + ruleBlock3

inputs = {
    'left': 40,
    'right': 10,
    'center': 10
}

def evaluate(fuzzy_sistem, rules, inputs):
    fuzzy_system.infer(rules, variables, adjectives, (0, 1), 0.01)
    return fuzzy_system.evaluate(inputs)

    
def plot_result(sample, membership, name):
    fig = plt.figure()
    plt.plot(sample, membership)
    fig.savefig(f'img/{name}.png')
    plt.close(fig)
    

if __name__ == "__main__":
    left = int(input('Left distance: '))
    right = int(input('Right distance: '))
    center = int(input('Center ditance: '))
    agg_mth = input('Please specify aggregation method [mamdani, larsen]:\n> ')
    defuzz_mth = input('Please specify defuzzification method [mean_of_max, left_of_max, right_of_max, median_of_max, centroid, bisector]:\n> ')
    fuzzy_system = FuzzyInferenceSystem(agg_mth, defuzz_mth)
    inputs = {'left': left, 'right': right, 'center': center}
    
    result = evaluate(fuzzy_system, rules, inputs)
    for var, output in result.items():
        value = output['value']
        print(f'The result of the variable corresponding to {var} is', value)
        sample = output['sample']
        plot_result(sample, output['membership'], 'ruleblock' + var)

    for var in variables.values():
        var.plot(sample)

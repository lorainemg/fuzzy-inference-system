from system import FuzzyInferenceSystem
from membership import Triangular, Trapezoidal
from rule import Antecedent, Consequent, Rule
from linguistic_var import Adjective, Variable
import matplotlib.pyplot as pl


litle = Adjective('litle', Trapezoidal(0, 5, 25, 30))
regular = Adjective('regular', Triangular(25, 40, 55))
much = Adjective('much', Triangular(50, 60, 80))
full = Adjective('full', Trapezoidal(75, 85, 90, 100))

amount = Variable('amount', litle, regular, much, full)

white_c = Adjective('white_cotton', Trapezoidal(-2, 0, 5, 17))
color_c = Adjective('color_cotton', Triangular(15, 25, 32))
white_d = Adjective('white_delicate', Trapezoidal(30, 37, 40, 47))
color_d = Adjective('color_delicate', Triangular(45, 53, 62))
white_s = Adjective('white_synthetic', Trapezoidal(55, 62, 75, 80))
color_s = Adjective('color_synthetic', Triangular(75, 82, 100))

type = Variable('type', white_c, color_c, white_d, color_d, white_s, color_s)

very_small = Adjective('very_small', Triangular(0, 13, 25))
small = Adjective('small', Triangular(20, 32, 45))
medium = Adjective('medium', Triangular(40, 50, 60))
big = Adjective('big', Triangular(55, 67, 80))
very_big = Adjective('very_big', Triangular(75, 80, 100))

agua_level = Variable('agua_level', very_small, small, medium, big, very_big)

adjectives = {value.name: value for var_name, value in locals().items() if isinstance(value, Adjective)}
variables = {value.name: value for var_name, value in locals().items() if isinstance(value, Variable)}

rule1 = Rule('if amount is litle and type is white_synthetic then '
            'agua_level is very_small')
rule2 = Rule('if amount is litle and type is color_synthetic then '
            'agua_level is very_small')
rule3 = Rule('if amount is litle and type is white_delicate then '
            'agua_level is small')
rule4 = Rule('if amount is litle and type is color_delicate then '
            'agua_level is small')
rule5 = Rule('if amount is litle and type is white_cotton then '
            'agua_level is medium')
rule6 = Rule('if amount is litle and type is color_cotton then '
            'agua_level is big')
rule7 = Rule('if amount is regular and type is white_synthetic then '
            'agua_level is small')
rule8 = Rule('if amount is regular and type is color_synthetic then '
            'agua_level is medium')
rule9 = Rule('if amount is regular and type is white_delicate then '
            'agua_level is medium')
rule10 = Rule('if amount is regular and type is color_delicate then '
            'agua_level is big')
rule11 = Rule('if amount is regular and type is white_cotton then '
            'agua_level is big')
rule12 = Rule('if amount is regular and type is color_cotton then '
            'agua_level is very_big')

rule13 = Rule('if amount is much and type is white_synthetic then '
            'nivel_ague is small')
rule14 = Rule('if amount is much and type is color_synthetic then '
            'agua_level is medium')
rule15 = Rule('if amount is much and type is white_delicate then '
            'agua_level is big')
rule16 = Rule('if amount is much and type is color_delicate then'
            'agua_level is big')  
rule17 = Rule('if amount is much and type is white_cotton then'
            'agua_level is big') 
rule18 = Rule('if amount is much and type is color_cotton then'
            'agua_level is very_big')  
 
rule13 = Rule('if amount is full and type is white_synthetic then '
            'nivel_ague is medium')
rule14 = Rule('if amount is full and type is color_synthetic then '
            'agua_level is big')
rule15 = Rule('if amount is full and type is white_delicate then '
            'agua_level is big')
rule16 = Rule('if amount is full and type is color_delicate then'
            'agua_level is big')  
rule17 = Rule('if amount is full and type is white_cotton then'
            'agua_level is very_big') 
rule18 = Rule('if amount is full and type is color_cotton then'
            'agua_level is very_big')  


rules = [value for var_name, value in locals().items() if isinstance(value, Rule)]

fuzzy_system = FuzzyInferenceSystem('mandami', 'mean_of_max')
fuzzy_system.infer(rules, variables, adjectives, (0, 100), 1)

inputs = {
    'amount': 80,
    'type': 10,
}

result, sample, membership = fuzzy_system.evaluate(inputs)
print(result)
pl.plot(sample, membership)
pl.savefig('img/result.png')
pl.show()

for var in variables.values():
    var.plot(sample)

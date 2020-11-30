from operators import logical_and, logical_not, logical_or

class Antecedent:
    ''' 
    Antecedents are of the form: variables1 is adjective1 [op] variable2 is adjective2 
    '''
    def __init__(self, sentence:str, variables, adjectives):
        self.parse(sentence, variables, adjectives)

    def parse(self, sentence, variables, adjectives):
        words = sentence.split()
        self.variables = []
        self.adjectives = []
        self.operators = []

        i = 1
        lastOp = False
        while i < len(words):
            if words[i] == 'not' or words[i] == '!':
                self.operators.append(logical_not)
                i += 1
            self.variables.append(variables[words[i]])
            self.adjectives.append(adjectives[words[i+2]])
            lastOp = False
            i += 2
            if i + 1 < len(words):
                lastOp = True
                self.operators.append(self._get_operator(words[i+1])) 
                i += 1
            i += 1

    def evaluate(self, values:dict):
        for i in range(len(self.variables)):
            self.variables[i].value = values.get(self.variables[i].name)
        i = 0
        result = self.adjectives[i].func(self.variables[i].value)
        for var, adj in zip(self.variables[1:], self.adjectives[1:]):
            value = adj.func(var.value)
            if self.operators[i] == logical_not:
                value = logical_not(value)
                i += 1
            else:
                result = self.operators[i](result, value)
                i += 1
        return result

    def _get_operator(self, word):
        if word == 'and' or '&&' or '&':
            return logical_and
        if word == 'or' or '||' or '|':
            return logical_or
        if word == 'not' or '!':
            return logical_not


class Consequent:
    '''
    Consequents are of the form: [variable] is [adjective] 
    '''
    def __init__(self, sentence:str, variables, adjectives): 
        self.parse(sentence, variables, adjectives)

    def parse(self, sentence:str, variables, adjectives):
        words = sentence.split()
        assert len(words) == 3, 'Consequent syntax is [variable] is [adjective]'
        self.variable = variables.get(words[0])
        self.adjective = adjectives.get(words[2]) # TODO: Change consequent structure if there is a function instead of a function

    @property
    def func(self):
        return self.adjective.func

class Rule:
    def __init__(self, sentence:str):
        self.antecedent_str, self.consequent_str = sentence.split('then')
        self.antecedent = None
        self.consequent = None

    def parse(self, variables, adjectives): 
        self.antecedent:Antecedent = Antecedent(self.antecedent_str, variables, adjectives)
        self.consequent:Consequent = Consequent(self.consequent_str, variables, adjectives) 

    def evaluate(self, values):
        'Evaluates the rule were all the values correspond to the variables values'
        return self.antecedent.evaluate(values)
    
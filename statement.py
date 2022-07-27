from state import State


class Statement:
    def execute(self, state : State):
        pass

class Program(Statement):
    def __init__(self, contents : list[Statement]) -> None:
        super().__init__()
        self.contents = contents
    
    def execute(self, state: State):
        for statement in self.contents:
            statement.execute(state)

class Declaration(Statement):
    def __init__(self, name, type) -> None:
        super().__init__()
        self.name = name
        self.type = type
    
    def execute(self, state : State):
        if self.type == 'numbah':
            state.variables[self.name] = 0

class Input(Statement):
    def __init__(self) -> None:
        super().__init__()
    
    def execute(self, state: State):
        txt = input('What are the mandems sayin right now')

        try:
            state.variables['word'] = int(txt)
        except ValueError:
            state.variables['word'] = txt

class Output(Statement):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
    
    def execute(self, state: State):
        print(state.variables[self.name])

class Increment(Statement):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
    
    def execute(self, state: State):
        state.variables[self.name] += 1

class Loop(Statement):
    def __init__(self, times_variable, statement : Statement) -> None:
        super().__init__()
        self.times_variable = times_variable
        self.statement = statement
    
    def execute(self, state: State):
        for i in range(state.variables[self.times_variable]):
            self.statement.execute(state)
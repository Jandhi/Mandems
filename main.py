
from state import State
from statement import Declaration, Increment, Input, Loop, Output, Program, Statement


program = Program([])
context = [program]

def interpret_file(path):
    with open(path) as file:
        for line in file:
            statement = interpret_line(line)
            
            if statement is not None:
                context[-1].contents.append(statement)

def interpret_line(line : str) -> Statement:
    line = line.rstrip().lstrip()

    if line.endswith('ting'):
        parts = line.split(' ')
        name = parts[0]
        type = parts[3]
        return Declaration(name, type)
    if line == 'what are the mandems sayin right now':
        return Input()
    if line.startswith('bless'):
        name = line.split(' ')[1]
        return Increment(name)
    if line.startswith('run that'):
        name = line.split(' ')[2]
        loop_program = Program([])
        context.append(loop_program)
        context[-2].contents.append(Loop(name, loop_program))
    if line == 'breeze':
        context.pop()
    if line.startswith('wagwan'):
        name = line.split(' ')[1]
        return Output(name)

interpret_file('fibonacci.6ix')
program.execute(State())
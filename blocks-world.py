'''
The main runner for blocks world project.
Uses Clingo API.

Author: Brandon Huyck, bhuyck@zagmail.gonzaga.edu
Date: Spring, 2024
Course: Answer Set Programming, CompSci Individual Study, Dr. Shawn Bowers,
	School for Engineering and Applied Scieces, Gonzaga University,
	Spokane, WA 99258

References include bramucas/clingo_python_basics; Answer Set Programming
(Draft) Vladimir Lifschitz University of Texas at Austin April 5, 2019
'''

import clingo
from sys import argv

if __name__=='__main__':
    with open(argv[1], 'r') as f:
        ASP_PROGRAM = f.read()

    with open(argv[2], 'r') as f:
        INPUT_PROGRAM = f.read()

    ctrl = clingo.Control(
        # arguments=['-n', '0'],
    )

    ctrl.add("base", [], ASP_PROGRAM)
    ctrl.add("input", [], INPUT_PROGRAM)
    ctrl.ground([("base", []), ("input", [])])

    with ctrl.solve(yield_=True) as solution_iterator:
        nanswer=1
        for model in solution_iterator:
            print(f'Answer {nanswer}')
            print(model)
            # for atom in model.symbols(atoms=True):  
            #     # atoms=True for ignoring #show statements, otherwise symbols will retrieve only shown atoms.
            #     if atom.name == 'block' and len(atom.arguments) == 1:  # We check if atom is block/1.
            #         print(f'Block is {atom.arguments[0]}')  # Arguments can be retrieved from atom.arguments
            nanswer+=1

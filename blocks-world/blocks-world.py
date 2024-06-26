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
from clingo.symbol import *
from sys import argv

if __name__=='__main__':
    with open(argv[1], 'r') as f:
        ASP_PROGRAM = f.read()

    with open(argv[2], 'r') as f:
        INPUT_PROGRAM = f.read()

    ctrl = clingo.Control(
        arguments=['-n', '0'],
    )

    ctrl.add("base", [], ASP_PROGRAM)
    ctrl.add("input", [], INPUT_PROGRAM)
    ctrl.ground([("base", []), ("input", [])])

    with ctrl.solve(yield_=True) as solution_iterator:
        nanswer=0
        atom_count = {}

        for model in solution_iterator:
            nanswer+=1
            if nanswer%10000==0:
                print(f'Answer {nanswer}')
            # print(model)

            for atom in model.symbols(atoms=True):  
                # atoms=True for ignoring #show statements, otherwise symbols will retrieve only shown atoms.
                if atom.name == 'occurs' and len(atom.arguments) == 2:  # We check if atom is occurs/2.
                    # print(f'Block is {atom.arguments[0]}')  # Arguments can be retrieved from atom.arguments
                    if str(atom) in atom_count:
                        atom_count[str(atom)] += 1
                    else:
                        atom_count[str(atom)] = 1
    
    print("What's true for all models:")
    print([i[0] for i in atom_count.items() if i[1] == nanswer], sep='\n')
    print()
    
    print("Percentage of models that atom holds true in:")
    percentage = sorted(atom_count.items(), key=lambda x: x[1], reverse=True)
    percentage = [(i[0], round(i[1]/nanswer, 3)) for i in percentage]
    print(percentage)

    ###
    
    ctrl_ = clingo.Control(
        arguments=['-n', '0'],
    )
    ctrl_.add("in_world", ["old", "number"], "in_world(old, number).")
    with ctrl.solve(yield_=True) as solution_iterator:
        nanswer=0
        for model in solution_iterator:
            nanswer+=1
            if nanswer%10000==0:
                print(f'Answer {nanswer}')
            for atom in model.symbols(atoms=True):  
                if atom.name == 'occurs' and len(atom.arguments) == 2:  # We check if atom is occurs/2.
                    ctrl_.ground([("in_world", [String(str(atom)), Number(nanswer)])])
    print(ctrl_.solve(on_model=print))
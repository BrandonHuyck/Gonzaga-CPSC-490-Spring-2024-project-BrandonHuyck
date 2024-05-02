import clingo
from clingo.symbol import *

if __name__ == '__main__':
    with open("shapley.lp", 'r') as f:
        ASP_PROGRAM = f.read()

    with open("shapley.inp", 'r') as f:
        INPUT_PROGRAM = f.read()

    ctrl = clingo.Control(
        arguments=['-n', '0'],
    )

    ctrl.add("base", [], ASP_PROGRAM)
    ctrl.add("input", [], INPUT_PROGRAM)
    ctrl.ground([("base", []), ("input", [])])

    with open("shapley-2.inp", 'w') as outf:
        with ctrl.solve(yield_=True) as solution_iterator:
            n = 0
            for model in solution_iterator:
                n += 1
                for atom in model.symbols(atoms=True):  
                    if atom.name == 'shapley' and len(atom.arguments) == 3:
                        outf.write(str(atom)[:8] + "world(" + str(n) + ")," + str(atom)[8:]+'.\n')

    with open("shapley-2.lp", 'r') as f:
        ASP_PROGRAM = f.read()

    with open("shapley-2.inp", 'r') as f:
        INPUT_PROGRAM = f.read()

    ctrl_ = clingo.Control(
        arguments=['-n', '0'],
    )
    # ctrl_.add("base", [], ASP_PROGRAM)
    # ctrl_.add("input", [], INPUT_PROGRAM)
    # ctrl_.ground([("base", []), ("input", [])])




    # ctrl_.add("shapley", ["world", "flight", "cardinality", "value"], "shapley(world, flight, cardinality, value).")
    # ctrl_.add("in_world", ["old", "number"], "in_world(old, number).")
    # ctrl_.ground([("in_world", [String(str(atom)), Number(nanswer)])])


    # with ctrl.solve(yield_=True) as solution_iterator:
    #     n = 0
    #     for model in solution_iterator:
    #         n += 1
    #         for atom in model.symbols(atoms=True):  
    #             # atoms=True for ignoring #show statements, otherwise symbols will retrieve only shown atoms.
    #             if atom.name == 'shapley' and len(atom.arguments) == 3:  # We check if atom is shapley/3.
    #                 # print(f'Block is {atom.arguments[0]}')  # Arguments can be retrieved from atom.arguments
    #                 ctrl_.ground([("in_world", [Number(n), String(str(atom)), asdf, asdf])])
from constraint import *
def sum(args):
    total = 0
    for index in range(len(args)):
        total += args[index] * pow(10, len(args) - index - 1)
    return total

def totalSum(*args):
    sum1 = sum((args[0], args[1], args[2], args[3]))
    sum2 = sum((args[4], args[5], args[6], args[1]))
    final = sum((args[4], args[5], args[2], args[1], args[7]))
    return sum1 + sum2 == final
if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    word1 = ()
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(AllDifferentConstraint(), variables)
    problem.addConstraint(totalSum, variables)
    # ----------------------------------------------------

    print(problem.getSolution())
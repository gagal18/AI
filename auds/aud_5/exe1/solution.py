from constraint import *

if __name__ == '__main__':
    problem = Problem()

    variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    domains = ["R", "G", "B"]
    problem.addVariables(variables, domains)
    pairs = [("WA", "NT"), ("WA", "SA"), ("SA", "NT"), ("SA", "NSW"), ("SA", "Q"), ("SA", "V"), ("NT", "Q"), ("Q", "NSW"), ("NSW", "V")]
    for pair in pairs:
        problem.addConstraint(lambda a, b: a != b, pair)
        
    print(problem.getSolution())

    res_iter = problem.getSolutionIter()
    for i in range(5):
        print(next(res_iter))
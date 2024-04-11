import itertools
from constraint import *

def ML_TIME(*ALL_ML):
    hours = {d.split("_")[1] for d in ALL_ML}
    return len(hours) == len(ALL_ML)

def TIME_GAP(a, b):
    d1, t1 = a.split("_")
    d2, t2 = b.split("_")
    return d1 != d2 or abs(int(t1) - int(t2)) > 1

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = input()
    casovi_ML = input()
    casovi_R = input()
    casovi_BI = input()
    
    
    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13","Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12", "Wed_13","Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13","Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]
    
    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]
    
    PREDAVANJE_DOMAINS = {
        "AI_cas": AI_predavanja_domain,
        "ML_cas": ML_predavanja_domain,
        "BI_cas": BI_predavanja_domain,
        "R_cas": R_predavanja_domain
    }
    VEZBI_DOMAINS = {
        "AI_vezbi": AI_vezbi_domain,
        "ML_vezbi": ML_vezbi_domain,
        "BI_vezbi": BI_vezbi_domain
    }
    
    classesDict = {
        "ML":  int(casovi_ML),
        "AI":  int(casovi_AI),
        "R":  int(casovi_R),
        "BI":  int(casovi_BI),
    }
    
    variables = []
    MLVars = []
    for keys in classesDict.keys():
        count = classesDict[keys]
        for i in range(count):
            variables.append(f"{keys}_cas_{i+1}")
            if keys == "ML":
                MLVars.append(f"{keys}_cas_{i+1}")
        if keys != "R":
            variables.append(f"{keys}_vezbi")
            if keys == "ML":
                MLVars.append(f"{keys}_vezbi")
    # ---Tuka dodadete gi promenlivite--------------------
    for variable in variables:
        checkType = len(variable.split("_"))
        if(checkType == 2):
            problem.addVariable(variable, VEZBI_DOMAINS[variable])
        else:
            class_domain = "_".join(variable.split("_")[:2])
            problem.addVariable(variable, PREDAVANJE_DOMAINS[class_domain])
            
        
        
    
    # ---Tuka dodadete gi ogranichuvanjata----------------
    
    for var1, var2 in itertools.combinations(variables, 2):
        problem.addConstraint(TIME_GAP, (var1, var2))
    problem.addConstraint(AllDifferentConstraint(), variables)
    problem.addConstraint(ML_TIME, MLVars)
    # ----------------------------------------------------
    solution = problem.getSolution()
    
    print(solution)
from constraint import *
def max4(*terms):
    count_dict = {}
    for term in terms:
        if term in count_dict:
            count_dict[term] += 1
        else:
            count_dict[term] = 1
    return all(count <= 4 for count in count_dict.values())


if __name__ == '__main__':
    num = int(input())
    
    papers = dict()
    
    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()
    
    # Tuka definirajte gi promenlivite
    domain = [f'T{i + 1}' for i in range(num)]
    variables = [f"{key} ({val})" for key, val in papers.items()]
    problem = Problem(BacktrackingSolver())
    
    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)
    
    # Tuka dodadete gi ogranichuvanjata
    by_course = {}
    
    for var in variables:
        course = var.split(" ")[1]
        if by_course.__contains__(course):
            by_course[course].append(var)
        else:
            by_course[course] = []
            by_course[course].append(var)
            
            
    for value in by_course.values():
        if len(value) <= 4:
            problem.addConstraint(AllEqualConstraint(), value)
            
    problem.addConstraint(max4, variables)

    result = problem.getSolution()
    
    # Tuka dodadete go kodot za pechatenje
    result = problem.getSolution()

    # Tuka dodadete go kodot za pechatenje
    for var in variables:
        print(f"{var}: {result[var]}")

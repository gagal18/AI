from constraint import *
def time_match(simona, marija, petar, time):
    SIMONA_SLOT = (13,14,16,19)
    MARIJA_SLOT = (14,15,18)
    PETAR_SLOT = (12,13,16,17,18,19)

    if time not in SIMONA_SLOT or simona == 0:
        return False
    
    if marija == 1 and time not in MARIJA_SLOT:
        return False
    if petar == 1 and time not in PETAR_SLOT:
        return False

    if marija + petar < 1:
        return False
    
    return True
    
    
if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    # Симона слободни термини: 13:00-15:00, 16:00-17:00, 19:00-20:00
    # Марија слободни термини: 14:00-16:00, 18:00-19:00
    # Петар слободни термини: 12:00-14:00, 16:00-20:00
    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Simona_prisustvo", [0,1])
    problem.addVariable("Marija_prisustvo", [0,1])
    problem.addVariable("Petar_prisustvo", [0,1])
    problem.addVariable("vreme_sostanok", range(12,20))
    # ----------------------------------------------------
    
    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(time_match,  ("Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"))
    # ----------------------------------------------------
    
    solutions = problem.getSolutions()

    for solution in solutions:
        sol_remap = {'Simona_prisustvo': solution['Simona_prisustvo'],'Marija_prisustvo': solution['Marija_prisustvo'],'Petar_prisustvo': solution['Petar_prisustvo'],'vreme_sostanok': solution['vreme_sostanok']}
        print(sol_remap)
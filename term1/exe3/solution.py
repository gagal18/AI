### PATH CONFIGURATION FOR IMPORTING MODULES FROM ROOT DIR
import sys
from os.path import dirname
from pathlib import Path
p = Path(__file__).parents[1]
sys.path.append(dirname(p))
from searching_framework.uninformed_search import breadth_first_graph_search, breadth_first_tree_search
from searching_framework.utils import Problem
from utils.input_tuple_int import parse_tuple_int
### PATH CONFIGURATION FOR IMPORTING MODULES FROM ROOT DIR
EMPTY_PILLAR = 1000
class Pillars(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.visited_states = [] 
    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal


    def successor(self, state):
        succ = {}
        n = len(state)

        for i in range(0, n):
            for j in range(0, n):
                pillars = [list(el) for el in state]
                if i == j or pillars[i][0] == EMPTY_PILLAR:
                    continue
                if pillars[j][-1] >= pillars[i][-1]:

                    ring = pillars[i].pop()
                    if len(pillars[i]) == 0:
                        pillars[i].append(EMPTY_PILLAR)
                    pillars[j].append(ring)
                    pillars[j] = [ring for ring in pillars[j] if ring != EMPTY_PILLAR]

                    pillars = [tuple(d) for d in pillars]
                    new_state = tuple(pillars)
                    if list(new_state) not in self.visited_states:
                        succ[f"MOVE TOP BLOCK FROM PILLAR {i+1} TO PILLAR {j+1}"] = new_state
                        self.visited_states.append(new_state)
                    
        return succ

def parse_string(listStr):
    return_state = []
    for l in listStr:
        if l != '':
            tmp = tuple(map(int, l.split(',')))
            return_state.append(tmp)
        else:
            tmp = (EMPTY_PILLAR,)
            return_state.append(tmp)
            
    return tuple(return_state)


if __name__ == "__main__":
    init_state = parse_string(input().split(";"))
    goal_state = parse_string(input().split(";"))
    problem = Pillars(init_state, goal_state)
    res = breadth_first_graph_search(problem)
    if res is not None:
        print("Number of action", len(res.solution()))
        print(res.solution())
    else:
        print("No solution found")

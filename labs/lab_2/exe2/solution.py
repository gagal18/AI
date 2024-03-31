### PATH CONFIGURATION FOR IMPORTING MODULES FROM ROOT DIR
import sys
from os.path import dirname
from pathlib import Path
p = Path(__file__).parents[2]
sys.path.append(dirname(p))
from searching_framework.informed_search import astar_search
from searching_framework.utils import Problem
from utils.input_tuple_int import parse_tuple_int
### PATH CONFIGURATION FOR IMPORTING MODULES FROM ROOT DIR

def parse_tuple_int(str, delimiter):
    return tuple(map(int, str.split(delimiter)))

def inputInt(str):
    return int(str.strip())

class StickManExplorer(Problem):      
    def __init__(self, initial, obstacles, size, goal = None):
        self.grid = [size, size]
        self.obstacles = obstacles
        super().__init__(initial, goal)
        
    def successor(self, state):
        successors = dict()
        
        return successors

        
    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == state[1]
    
    def h(self, node):
        manX, manY = node.state[0]
        houseX, houseY = node.state[1]
        return abs(manX - houseX) + abs(manY - houseY)
    
    
if __name__ == '__main__':
    size = inputInt(input())
    obsCount = inputInt(input())
    obstacles = []
    for i in range(obsCount):
        obs = parse_tuple_int(input(), ",")
        obstacles.append(obs)
    man = parse_tuple_int(input(), ",")
    house = parse_tuple_int(input(), ",")
    print((man, house), obstacles, size)
    manInHouse = StickManExplorer((man, house), obstacles, size)
    result = astar_search(manInHouse)
    
    print(result.solution())

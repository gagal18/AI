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

def house_direction(str):
    if str == "desno":
        return 1
    else:
        return -1
    
def change_direction(dir):
    return dir * -1

def moveHouse(house, grid, dir):
    tempHouseX = house[0]
    tempHouseX = tempHouseX + dir
    if is_in_grid(house, grid):
        return (tempHouseX, house[1])
    else:
        tempHouseX = tempHouseX + change_direction(dir)
        return (tempHouseX, house[1])
    
def is_in_grid(prop, grid):
    gridX, gridY = grid
    propX, propY = prop
    return 0 <= propX < gridX and 0 <= propY < gridY

man_directions = {
    "Gore 1": (0, 1),
    "Gore 2": (0, 2),
    "Gore-desno 1": (1, 1),
    "Gore-desno 2": (1, 2),
    "Gore-levo 2": (-1, 1),
    "Gore-levo 2": (-1, 2),
}

class ManInHouse(Problem):
    def __init__(self, initial, allowed, direction, goal = None):
        self.grid = [5,9]
        self.allowed = allowed
        self.direction = direction
        super().__init__(initial, goal)
        
    def successor(self, state):
        successors = dict()
        
        manX, manY = state[0]
        allowed = self.allowed
        grid = self.grid
        dir = self.direction

        
        for direction, (dx, dy) in man_directions.items():
            new_manX = manX + dx
            new_manY = manY + dy
            
            
            if (new_manX, new_manY) in allowed:
                newMan = (new_manY, new_manY)
                newHouse = moveHouse(state[1], grid, dir)
                
                state_new = (newMan, newHouse)

                if(is_in_grid(newMan, grid)):
                    print("new state")
                    print(state_new)
                    successors[direction] = state_new

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
    allowed = [(1,0), (2,0), (3,0), (1,1), (2,1), (0,2), (2,2), (4,2), (1,3), (3,3), (4,3), (0,4), (2,4), (2,5), (3,5), (0,6), (2,6), (1,7), (3,7)]
    man = parse_tuple_int(input(), ",")
    house = parse_tuple_int(input(), ",")
    direction = house_direction(input())
    print(man, house, direction)
    
    manInHouse = ManInHouse((man, house), allowed, direction)
    result = astar_search(manInHouse)
    
    print(result.solution())

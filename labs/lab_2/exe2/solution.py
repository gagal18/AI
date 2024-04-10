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

def inputInt(str):
    return int(str.strip())

def is_in_grid(prop, grid):
    gridX, gridY = grid
    propX, propY = prop
    return 0 <= propX < gridX and 0 <= propY < gridY


man_directions = {
    "Gore": (0, 1),
    "Dolu": (0, -1),
    "Levo": (-1, 0),
    "Desno 2": (2, 0),
    "Desno 3": (3, 0),

}

class StickManExplorer(Problem):
    def __init__(self, initial, obstacles, size, goal=None):
        self.grid = [size, size]
        self.obstacles = obstacles
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()

        manX, manY = state[0]
        obstacles = self.obstacles
        grid = self.grid
        for direction, (dx, dy) in man_directions.items():
            new_manX = manX + dx
            new_manY = manY + dy

            newMan = (new_manX, new_manY)

            if newMan not in obstacles:
                if (is_in_grid(newMan, grid)):
                    state_new = (newMan, state[1])
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
        dx = abs(manY - houseY)
        dy = abs(manX - houseX) 
        return (dx + dy) // 3


if __name__ == '__main__':
    size = inputInt(input())
    obsCount = inputInt(input())
    obstacles = []
    for i in range(obsCount):
        obs = parse_tuple_int(input(), ",")
        obstacles.append(obs)
    man = parse_tuple_int(input(), ",")
    house = parse_tuple_int(input(), ",")
    manInHouse = StickManExplorer((man, house), obstacles, size)
    result = astar_search(manInHouse)
    if result:
        print(result.solution())
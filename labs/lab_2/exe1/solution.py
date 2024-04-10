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
from searching_framework import Problem, astar_search
def house_direction(str):
    if str == "desno":
        return 1
    else:
        return -1


def change_direction(dir):
    return dir * -1


def moveHouse(house, dir):
    tempHouseX = house[0]
    tempHouseX = tempHouseX + dir
    return (tempHouseX, house[1])


def is_in_grid(prop, grid):
    gridX, gridY = grid
    propX, propY = prop
    return 0 <= propX < gridX and 0 <= propY < gridY


man_directions = {
    "Stoj": (0, 0),
    "Gore 1": (0, 1),
    "Gore 2": (0, 2),
    "Gore-desno 1": (1, 1),
    "Gore-desno 2": (2, 2),
    "Gore-levo 1": (-1, 1),
    "Gore-levo 2": (-2, 2),
}


class ManInHouse(Problem):
    def __init__(self, initial, allowed, goal=None):
        self.grid = [5, 9]
        self.allowed = allowed
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()

        manX, manY = state[0]
        allowed = self.allowed
        grid = self.grid
        houseDir = state[2]
        for direction, (dx, dy) in man_directions.items():
            new_manX = manX + dx
            new_manY = manY + dy

            newMan = (new_manX, new_manY)

            newHouse = moveHouse(state[1], houseDir)
            if (not is_in_grid(newHouse, grid)):
                houseDir = change_direction(houseDir)
                newHouse = (newHouse[0] + 2 * houseDir, newHouse[1])
            if newMan in allowed or newMan == newHouse:

                if (is_in_grid(newMan, grid) and is_in_grid(newHouse, grid)):
                    state_new = (newMan, newHouse, houseDir)
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
        return abs(manY - houseY) // 2


if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]
    man = parse_tuple_int(input(), ",")
    house = parse_tuple_int(input(), ",")
    direction = house_direction(input())

    manInHouse = ManInHouse((man, house, direction), allowed)
    result = astar_search(manInHouse)
    if result:
        print(result.solution())
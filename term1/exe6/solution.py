### PATH CONFIGURATION FOR IMPORTING MODULES FROM ROOT DIR
import sys
from os.path import dirname
from pathlib import Path
p = Path(__file__).parents[1]
sys.path.append(dirname(p))
from searching_framework.uninformed_search import breadth_first_graph_search
from searching_framework.utils import Problem
### PATH CONFIGURATION FOR IMPORTING MODULES FROM ROOT DIR

square_dir = {
    "gore": (0, 1),
    "dolu": (0, -1),
    "levo": (-1, 0),
    "desno": (+1, 0),
}

# FOR SOME FCKING REASON IF THIS SQUARE_DIR
# IS LIKE THIS, NOT ALL TEST CASES Pass (WHYYYYYYY!!!!!!!!!!!!!!!!!)
# square_dir = {
    # "levo": (-1, 0),
    # "desno": (+1, 0),
    # "gore": (0, 1),
    # "dolu": (0, -1),
# }
class Squares(Problem):
    def __init__(self, initial, house):
        super().__init__(initial, house)

    def goal_test(self, state):
        return state == self.goal

    @staticmethod
    def check_valid(state):
        for x, y in state:
            if x < 0 or x > 4 or y < 0 or y > 4:
                return False
        return True
    
    def successor(self, state):
        succ = {}
        squares = state
        count = 0
        for (sX, sY) in squares:
            for direction, (dx, dy) in square_dir.items():
                squareX = sX + dx
                squareY = sY + dy
                newSquare = (squareX, squareY)
                state_new = list(squares)
                state_new[count] = newSquare
                if self.check_valid(state_new):
                    succ[f"Pomesti kvadratche {count + 1} {direction}"] = tuple(state_new)
            count+=1
        return succ

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    # ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5))
    initial_state = tuple()
    for _ in range(5):
        initial_state += (tuple(map(int, input().split(','))), )

    goal_state = ((0, 4), (1, 3), (2, 2), (3, 1), (4, 0))

    squares = Squares(initial_state, goal_state)
    result = breadth_first_graph_search(squares)
    if result is not None:
        print(result.solution())
    else:
        print("No solution found")
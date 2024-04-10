### PATH CONFIGURATION FOR IMPORTING MODULES FROM ROOT DIR
import sys
from os.path import dirname
from pathlib import Path
p = Path(__file__).parents[1]
sys.path.append(dirname(p))
from searching_framework.informed_search import astar_search
from searching_framework.utils import Problem
### PATH CONFIGURATION FOR IMPORTING MODULES FROM ROOT DIR


def is_in_grid(prop, grid):
    gridX, gridY = grid
    propX, propY = prop
    return 0 <= propX < gridX and 0 <= propY < gridY

ghost_dir = {
    "Gore 1": (0, 1),
    "Gore 2": (0, 2),
    "Gore 3": (0, 3),
    "Desno 1": (1, 0),
    "Desno 2": (2, 0),
    "Desno 3": (3, 0),
}

class GhostOnSkates(Problem):
    def __init__(self, initial, walls, n, goal=None):
        super().__init__(initial, goal)
        self.walls = walls
        self.n = n
        self.grid = [n,n]

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

    def successor(self, state):
        successors = dict()
        ghostX, ghostY = state
        walls = self.walls
        grid = self.grid
        for direction, (dx, dy) in ghost_dir.items():
            new_ghostDirX = ghostX + dx
            new_ghostDirY = ghostY + dy

            newGhost = (new_ghostDirX, new_ghostDirY)
            
            if newGhost not in walls and is_in_grid(newGhost, grid):
                state_new = newGhost
                successors[direction] = state_new
        return successors

    def h(self, node):
        ghostX, ghostY = node.state
        size = self.n
        dx = abs(ghostX - size)
        dy = abs(ghostY - size) 
        return (dx + dy) / 3


if __name__ == '__main__':
    n = int(input())
    ghost_pos = (0, 0)
    goal_pos = (n - 1, n - 1)

    num_holes = int(input())
    holes = list()
    for _ in range(num_holes):
        holes.append(tuple(map(int, input().split(','))))

    problem = GhostOnSkates(ghost_pos, holes, n, goal_pos)
    play = astar_search(problem)
    if play is not None:
        print(play.solution())
    else:
        print("No solution found")

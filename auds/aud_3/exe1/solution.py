
"""
12 8
6 4
8 3
"""

### PATH CONFIGURATION FOR IMPORTING MODULES FROM ROOT DIR
import sys
from os.path import dirname
from pathlib import Path
p = Path(__file__).parents[2]
sys.path.append(dirname(p))
from utils.input_tuple_int import parse_tuple_int
### PATH CONFIGURATION FOR IMPORTING MODULES FROM ROOT DIR


if __name__ == "__main__":
    capacity = parse_tuple_int(input(), " ")
    goal = parse_tuple_int(input(), " ")
    start_state = parse_tuple_int(input(), " ")
    print(capacity)
    print(goal)
    print(start_state)
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"

def update_bomb_data(matrix, row_index, col_index):
    rows = len(matrix)
    cols = len(matrix[0])
    neighbors = [(row_index + i, col_index + j) for i in range(-1, 2) for j in range(-1, 2)]
    
    for r, c in neighbors:
        if 0 <= r < rows and 0 <= c < cols:
            if(matrix[r][c] == "#"):
                continue
            matrix[r][c] += 1


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def fillMatrix(self):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == '-':
                    matrix[i][j] = 0         
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == '#':
                    update_bomb_data(self.matrix, i , j)                       
        
    def __repr__(self):
        string = ""
        for row in self.matrix:
            row_str = "   ".join(map(str, row))
            string += row_str + "\n"
        return string        
    
if __name__ == "__main__":
    num = int(input())
    matrix = []
    to = range(num)
    for i in to:
        matrix.append(input().split("   "))
    minesweeper = Matrix(matrix)
    minesweeper.fillMatrix()
    print(minesweeper)
    
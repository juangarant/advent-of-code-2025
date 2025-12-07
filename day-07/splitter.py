import sys
import copy

def generatearray(file):
    lines = file.splitlines()
    grid = []
    for line in lines:
        elements = list(line)
        grid.append(elements)
    return grid

def split(file):
    grid = generatearray(file)
    m = len(grid)  # number of rows
    n = len(grid[0])   # number of columns
    position = []
    count1 = 0
    count2 = 0
    newposition = []
    for i in range(m):
        
        if not position:
            for j in range(n):
                if grid[i][j] == 'S':
                    position.append(j)
                    break
        else:
            vpos = copy.deepcopy(position)
            for j in range(len(vpos)):
                if grid[i][vpos[j]]=='^':
                    grid[i][vpos[j]-1] = '|'
                    grid[i][vpos[j]+1] = '|'
                    count1 += 1
                    newposition.append(vpos[j]-1)
                    newposition.append(vpos[j]+1)
                    position.remove(vpos[j])
                else:
                    grid[i][vpos[j]] = '|'
            position = list(set(position + newposition))
            newposition = []
    #segunda pasada para comprobar todas las |
    for i in range(m):

        for j in range(n):
            if grid[i][j] == '^':
                for z in range(j-1, n):
                    if grid[i][z] == '|':
                        count2 += 1
                break
    
    return count1, count2




if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python splitter.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    sol1, sol2 = split(content)
    print(f"File '{filename}' has been split into {sol2} parts.")
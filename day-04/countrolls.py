import sys
import copy

def counterrolls1(data):
    grid = [
        [char for char in line]
        for line in data
    ]
    m = len(grid) # number of rows
    n = len(grid[0]) # number of columns
    cr = [-1, -1, -1, 0, 0, 1, 1, 1]
    cc = [-1, 0, 1, -1, 1, -1, 0, 1]
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                aclose = 0
                for k in range(8):
                    ni = i + cr[k]
                    nj = j + cc[k]
                    if ni >= 0 and ni < m and nj >= 0 and nj < n:
                        if grid[ni][nj] == '@':
                            aclose += 1
                if aclose < 4:
                    count += 1
    return count

def counterrolls2(data):
    grid = [
        [char for char in line]
        for line in data
    ]
    gridcopy = [
        [char for char in line]
        for line in data
    ]
    m = len(grid) # number of rows
    n = len(grid[0]) # number of columns
    cr = [-1, -1, -1, 0, 0, 1, 1, 1]
    cc = [-1, 0, 1, -1, 1, -1, 0, 1]
    count = 0
    while True:
        countc = count
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    aclose = 0
                    for k in range(8):
                        ni = i + cr[k]
                        nj = j + cc[k]
                        if ni >= 0 and ni < m and nj >= 0 and nj < n:
                            if grid[ni][nj] == '@':
                                aclose += 1
                    if aclose < 4:
                        count += 1
                        gridcopy[i][j] = '.'
        # if countc == count: break (tambien se puede usar esta linea en vez de la de abajo)
        if grid == gridcopy:
            break
        grid = copy.deepcopy(gridcopy)
    return count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python countrolls.py <file_path>")
        sys.exit(1)

    path = sys.argv[1]
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        sys.exit(1)
    
    count = counterrolls2(data)
    print(f"Total count of rolls: {count}")
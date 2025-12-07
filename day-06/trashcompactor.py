import sys

def generatearray(file):
    lines = file.splitlines()

    finalgrid = []

    for line in lines:
        elements = line.split()
        if elements[0].isdigit():
            numberrow = [int(num) for num in elements]
            finalgrid.append(numberrow)
        else:
            finalgrid.append(elements)
    return finalgrid

def generatearray2(file):
    lines = file.splitlines()

    finalgrid = []
    for line in lines:
        elements = list(line)
        finalgrid.append(elements)
    return finalgrid

def compacttrash2(file):
    grid = generatearray2(file)
    total = 0
    m = len(grid)  # number of rows
    n = len(grid[0])  # number of columns
    total = 0
    for i in range(n):
        count = 0
        operador = grid[m-1][i]
        if operador == '*':
            count = 1
        for j in range(m-1):
            valor = grid[j][i]
            if operador == '+':
                count += int(valor)
            if operador == '*':
                count *= int(valor)
        total += count
    return total
            
def compacttrash(file):
    grid = generatearray2(file)
    total = 0
    m = len(grid)  # number of rows
    n = len(grid[0])  # number of columns
    total = 0
    count = 0
    firstround = True
    for i in range(n):
        number = ''
        if grid[m-1][i] != ' ':
            operador = grid[m-1][i]
        if firstround and operador == '*':
            count = 1
            firstround = False
        for j in range(m-1):
            valor = grid[j][i]
            if valor == ' ':
                continue 
            else:
                number += valor
        
        if number.isdigit():
            number = int(number)
            if operador == '+':
                count += number
            if operador == '*':
                count *= number
        if number == '' or i == n-1:
            total += count
            count = 0
            firstround = True
    return total



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python trashcompactor.py <file_path>")
        sys.exit(1)

    path = sys.argv[1]
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        sys.exit(1)
    ans = compacttrash(data)
    print(f"Total compacted trash: {ans}")
    
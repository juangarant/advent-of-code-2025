import sys

def splitarray(arr):
    elements = arr.splitlines()
    numbers = []
    signs = []
    for line in elements:
        rownumbers = []
        isNumber = False
        rowsigns = []
        isSign = False
        for item in line.split():
            if item.isdigit():
                rownumbers.append(int(item))
                isNumber = True
            else:
                rowsigns.append(item)
                isSign = True
        if isNumber:
            numbers.append(rownumbers)
        if isSign:
            signs.append(rowsigns)  
    return numbers, signs

def compacttrash(file):
    numbers, signs = splitarray(file)
    total = 0
    numberrowlen = len(numbers)
    signrowlen = len(signs)

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
    
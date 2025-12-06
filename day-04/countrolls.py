import sys

def counterrolls(data):
    grid = []
    for i in range(len(data)):
        grid.append(int(digito) for digito in str(data[i]))
    print(grid)

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
    
    count = counterrolls(data)
    print(f"Total count of rolls: {count}")
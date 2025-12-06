import sys

def joinranges(ranges):
    ranges.sort(key=lambda x: x[0])
    fuse = []
    for actual in ranges:
        if not fuse or fuse[-1][1] < actual[0] - 1:
            fuse.append(actual)
        else:
            fuse[-1] = (fuse[-1][0], max(fuse[-1][1], actual[1]))
    return fuse

def existinrange(number, ranges):
    for actual in ranges:
        if actual[0] <= number <= actual[1]:
            return True
    return False

def countinrange(ranges):
    total = 0
    for actual in ranges:
        total += actual[1] - actual[0] + 1
    return total

def countids(data, snd):
    data = data.split("\n\n")
    total = 0
    scope = []
    data1 = data[0]
    data1 = data1.splitlines()
    data2 = data[1]
    data2 = data2.splitlines()
    if snd:
        data = data1
        for i in range(len(data)):
            actualdata = data[i].split("-")
            scope.append(tuple((int(actualdata[0]), int(actualdata[1]))))
        scope = joinranges(scope)
        for i in range(len(scope)):
            total += scope[i][1] - scope[i][0] + 1
        return total
    else:
        for i in range(len(data1)):
            actualdata = data1[i].split("-")
            scope.append(tuple((int(actualdata[0]), int(actualdata[1]))))
        scope = joinranges(scope)
        for i in range(len(data2)):
            if existinrange(int(data2[i]), scope):
                total += 1
        return total



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python countrolls.py <file_path>")
        sys.exit(1)

    path = sys.argv[1]
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        sys.exit(1)
    
    count = countids(data, True)
    print(f"Total count of rolls: {count}")
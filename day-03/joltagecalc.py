import sys

def part1(list):
            pos = 0
            total = 0
            for actual in list:
                first = actual[0]
                n = len(actual)
                for i in range(n-1):
                    if actual[i] > first:
                        first = actual[i]
                        pos = i
                newactual = actual[pos+1:]
                second = newactual[0]
                n = len(newactual)
                for i in range(n):
                    if newactual[i] > second:
                        second = newactual[i]
                total += int(str(first + second))
            return total

def part2(list, long):
            total = 0
            for actual in list:
                searchstart = 0
                n = len(actual)
                result = []
                for i in range(long):
                    holes_needed = long - 1 - i
                    limit = n - holes_needed
                    section = actual[searchstart:limit]
                    if section != []:
                        max_value = max(section)
                        result.append(max_value)
                        index = section.index(max_value)
                        searchstart += index + 1

                total += int(''.join(map(str, result)))
            return total
        
def calculate_max_number(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = file.read().splitlines()
            # file.read() advances the file pointer; pass a fresh StringIO
            return [part1(data), part2(data, 12)]
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return None
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python joltagecalc.py <file_path>")
        sys.exit(1)

    path = sys.argv[1]
    max_number = calculate_max_number(path)
    if max_number is not None:
        print(f"The maximum number in part1 is: {max_number[0]}")
        print(f"The maximum number in part2 is: {max_number[1]}")
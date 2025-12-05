import sys

def calculate_max_number_part1(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            list = file.read().splitlines()
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
        
def calculate_max_number_part2(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            list = file.read().splitlines()
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


    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return None
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python joltagecalc.py <file_path>")
        sys.exit(1)

    path = sys.argv[1]
    max_number1 = calculate_max_number_part1(path)
    max_number2 = calculate_max_number_part2(path)
    if max_number1 and max_number2 is not None:
        print(f"The maximum number in part1 is: {max_number1}")
        print(f"The maximum number in part2 is: {max_number2}")
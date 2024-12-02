from src.utils import read_integer_columns

def is_safe(row):
    for i in range(1, len(row)):
        if row[i] > row[i-1]:
            if row[i] - row[i-1] > 3:
                return False
        elif row[i] < row[i-1]:
            if row[i-1] - row[i] > 3:
                return False
        else:
            return False
    return True

def is_monotonic(row):
    increasing = True
    decreasing = True
    
    for i in range(1, len(row)):
        if row[i] > row[i-1]:
            decreasing = False
        elif row[i] < row[i-1]:
            increasing = False

    return increasing or decreasing

def is_safe_without_record(row):
    for i in range(len(row)):
        new_row = row[:i] + row[i+1:]
        if not is_monotonic(new_row):
            continue

        if is_safe(new_row):
            return True
    
    return False

def solution_1(data_path):
    raw_data = read_integer_columns(data_path, separator=" ")
    return sum(is_safe(row) for row in raw_data if is_monotonic(row))

def solution_2(data_path):
    raw_data = read_integer_columns(data_path, separator=" ")
    return sum(is_safe_without_record(row) for row in raw_data)

if __name__ == "__main__":
    data_path="src/2024/day2/data.txt"
    print(f"part_1 = {solution_1(data_path=data_path)}")
    print(f"part_2 = {solution_2(data_path=data_path)}")

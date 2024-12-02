from src.utils import read_integer_columns, count_values

def solution_1(data_path):
    
    raw_data = read_integer_columns(data_path)
    left, right = zip(*raw_data)

    left = sorted(left)
    right = sorted(right)

    return sum(abs(right[i] - left[i]) for i in range(len(left)))

def solution_2(data_path):
    
    raw_data = read_integer_columns(data_path)
    left, right = zip(*raw_data)

    counts = count_values(right)

    return sum(value * counts.get(value, 0) for value in left)

if __name__ == "__main__":
    data_path="src/2024/day1/data.txt"
    print(f"part_1 = {solution_1(data_path=data_path)}")
    print(f"part_2 = {solution_2(data_path=data_path)}")
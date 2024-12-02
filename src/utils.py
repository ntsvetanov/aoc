
def read_input(data_path):
    with open(data_path, "r") as file:
        data = file.read().splitlines()
    return data


def read_integer_columns(data_path):
    with open(data_path, "r") as file:
        return [tuple(map(int, row.split("   "))) for row in file]


def count_values(data):
    count = {}
    for i in data:
        count[i] = count.get(i, 0) + 1
    return count

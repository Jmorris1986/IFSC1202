import csv

def load_distance_table(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
    return data

def print_distance_table(table):
    for row in table:
        print("\t".join(row))

def find_city_index(table, city, is_row=True):
    try:
        if is_row:
            return table[0].index(city)
        else:
            for i, row in enumerate(table):
                if row[0] == city:
                    return i
    except ValueError:
        return -1

def main():
    filename = "09.Project Distances.csv"
    table = load_distance_table(filename)
    print_distance_table(table)
    
    from_city = input("Enter From City: ")
    to_city = input("Enter To City: ")
    
    row_index = find_city_index(table, from_city, is_row=False)
    col_index = find_city_index(table, to_city, is_row=True)
    
    if row_index == -1:
        print("Invalid From City")
    elif col_index == -1:
        print("Invalid To City")
    else:
        distance = table[row_index][col_index]
        print(f"Distance from {from_city} to {to_city}: {distance} miles")

if __name__ == "__main__":
    main()

def read_names_from_file(filename):
    boys_list = []
    girls_list = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                # Split the name pair and strip any leading/trailing spaces
                boy_name, girl_name = map(str.strip, line.split(','))
                boys_list.append(boy_name)
                girls_list.append(girl_name)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None, None

    return boys_list, girls_list

def format_name(name):
    return name.strip().capitalize()

def search_name(name, boys_list, girls_list):
    for index, (boy_name, girl_name) in enumerate(zip(boys_list, girls_list)):
        if name == boy_name:
            return f"Boy's Name - Rank: {index + 1}"
        elif name == girl_name:
            return f"Girl's Name - Rank: {index + 1}"
    return "Name Not Found"

def main():
    filename = "Exam Two Names.txt"
    boys_list, girls_list = read_names_from_file(filename)

    if boys_list is None or girls_list is None:
        return

    while True:
        user_input = input("Enter a name (or 'Q' to quit): ").strip()
        if user_input.upper() == 'Q':
            break

        formatted_name = format_name(user_input)
        result = search_name(formatted_name, boys_list, girls_list)
        print(result)

if __name__ == "__main__":
    main()
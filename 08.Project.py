def read_constitution(file_path):
    """Reads the constitution file and returns a list of lines."""
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def find_section(lines, search_term):
    """Finds and prints the section containing the search term."""
    found = False
    section_start = -1
    section_end = -1

    for i in range(len(lines)):
        if search_term.lower() in lines[i].lower():
            # We found the search term, now find the section start and end
            if not found:
                # Find the start of the section (loop backward)
                for j in range(i, -1, -1):
                    if lines[j] == "":
                        section_start = j + 1
                        break
                # Find the end of the section (loop forward)
                for k in range(i, len(lines)):
                    if lines[k] == "":
                        section_end = k
                        break
                found = True

            # Print the relevant section
            print(f"Line {i + 1}:")
            for line in lines[section_start:section_end]:
                print(line)
            print("\n")  # Add a new line after each section

            # Skip ahead to the end of the section
            i = section_end
    return found

def search_constitution():
    """Main function to search the constitution for terms."""
    constitution_lines = read_constitution('constitution.txt')

    while True:
        search_term = input("Enter search term (blank to exit): ").strip()
        if not search_term:
            break

        found = find_section(constitution_lines, search_term)
        if not found:
            print(f"Search term '{search_term}' not found.\n")

if __name__ == "__main__":
    search_constitution()

#A school decided to replace the desks in three classrooms. Each desk seats two students.
# Function to calculate the number of desks needed for each classroom
def calculate_desks(students):
    desks_for_two_students = students // 2
    desks_for_one_student = students % 2
    return desks_for_two_students + desks_for_one_student

# Read the number of students in each classroom
students_A = int(input("Enter the number of students in Classroom A: "))
students_B = int(input("Enter the number of students in Classroom B: "))
students_C = int(input("Enter the number of students in Classroom C: "))

# Calculate the number of desks needed for each classroom
desks_A = calculate_desks(students_A)
desks_B = calculate_desks(students_B)
desks_C = calculate_desks(students_C)

# Calculate the total number of desks needed
total_desks = desks_A + desks_B + desks_C

# Print the total number of desks needed
print(f"Total number of desks needed: {total_desks}")

class Student:
    def __init__(self, firstname, lastname, tnumber):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = []  # List of string grades (can be empty)

    def RunningAverage(self):
        valid_grades = [float(g) for g in self.Grades if g.strip() != ""]
        if valid_grades:
            return sum(valid_grades) / len(valid_grades)
        return 0.0

    def TotalAverage(self):
        total_grades = [float(g) if g.strip() != "" else 0.0 for g in self.Grades]
        if total_grades:
            return sum(total_grades) / len(total_grades)
        return 0.0

    def LetterGrade(self):
        avg = self.TotalAverage()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def __str__(self):
        return (f"{self.FirstName} {self.LastName} ({self.TNumber}) - "
                f"Running Avg: {self.RunningAverage():.2f}, "
                f"Total Avg: {self.TotalAverage():.2f}, "
                f"Grade: {self.LetterGrade()}")


class StudentList:
    def __init__(self):
        self.Studentlist = []

    def add_student(self, firstname, lastname, tnumber):
        student = Student(firstname, lastname, tnumber)
        self.Studentlist.append(student)

    def find_student(self, tnumber):
        for index, student in enumerate(self.Studentlist):
            if student.TNumber == tnumber:
                return index
        return -1

    def print_student_list(self):
        for student in self.Studentlist:
            print(student)

    def add_student_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        self.add_student(parts[0].strip(), parts[1].strip(), parts[2].strip())
        except FileNotFoundError:
            print(f"File {filename} not found.")

    def add_scores_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) > 1:
                        tnumber = parts[0].strip()
                        scores = parts[1:]
                        index = self.find_student(tnumber)
                        if index != -1:
                            self.Studentlist[index].Grades.extend([s.strip() for s in scores])
        except FileNotFoundError:
            print(f"File {filename} not found.")


# ==== Main Program ====

def main():
    student_list = StudentList()

    # Add students from file
    student_list.add_student_from_file("11.Project Students.txt")

    # Add scores from file
    student_list.add_scores_from_file("11.Project Scores.txt")

    # Print student details
    student_list.print_student_list()


if __name__ == "__main__":
    main()

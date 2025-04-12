class Student:
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname.strip()
        self.LastName = lastname.strip()
        self.TNumber = tnumber.strip()
        self.Grades = [score.strip() for score in scores]  # Store as list of strings

    def RunningAverage(self):
        valid_scores = [int(score) for score in self.Grades if score != '']
        if valid_scores:
            return sum(valid_scores) / len(valid_scores)
        return 0.0

    def TotalAverage(self):
        total_scores = [int(score) if score != '' else 0 for score in self.Grades]
        return sum(total_scores) / len(total_scores)

    def LetterGrade(self):
        avg = self.TotalAverage()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

def main():
    filename = "10.Project Student Scores.txt"

    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                firstname = parts[0]
                lastname = parts[1]
                tnumber = parts[2]
                scores = parts[3:]
                student = Student(firstname, lastname, tnumber, scores)

                print(f"Student: {student.FirstName} {student.LastName}, {student.TNumber}")
                print(f"  Grades: {student.Grades}")
                print(f"  Running Average (non-blank): {student.RunningAverage():.2f}")
                print(f"  Total Average (missing=0): {student.TotalAverage():.2f}")
                print(f"  Letter Grade: {student.LetterGrade()}")
                print("-" * 50)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

if __name__ == "__main__":
    main()

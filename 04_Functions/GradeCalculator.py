"""A teacher enters a student's marks for each subject: test (out of 30), attendance (out of 30), exam (out of 90), and project (out of 50). 
For every subject, the program totals the marks, converts the total to a percentage, and assigns a grade."""



maxMark= {"test": 30, "attendance": 30, "exam": 90, "project": 50}

def sortGrade(score: float) -> str:
    #For each score range, append a suitable grade
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 55:
        return "C"
    elif score >= 35:
        return "D"
    return "F"

def calcAvg(scores: list[float]) -> float:
    #return the average of a list of scores
    return sum(scores)/ len(scores)

def getPercentage(test: float, attendance:float, exam: float, project: float) -> float:
    #Covert the total(out of 200 points) to percentage
    
    total = test + attendance + exam + project
    return (total / sum(maxMark.values())) * 100

def askMark(label: str) -> float:
    #Ask for a mark and repeat until it is a number between 0 and maxMark.
    limit = maxMark[label]
    while True:
        try:
            score = float(input(f"{label.title()} score (out of {limit}): "))
        except ValueError:
            print("Please enter a number.")
            continue
        if 0 <= score <= limit:
            return score
        print(f"Mark must be between 0 and {limit}.")

def askSubject() -> str:
     while True:
        name = input("\nSubject name: ").strip()
        if name.replace(" ", "").isalpha():
            return name.title()
        print("Subject name must contain letters only (no numbers).")

def main() -> None:
    percentages = []
    while True:
        text = input("How many subjects? ")
        try:
            numberOfSubjects = int(text)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if numberOfSubjects < 1:
            print("Enter at least 1 subject.")
            continue
        break

    for i in range(numberOfSubjects):
        subject = askSubject()
        test = askMark("test")
        attendance = askMark("attendance")
        exam = askMark("exam")
        project = askMark("project")

        percentage = getPercentage(test, attendance, exam, project)
        percentages.append(percentage)
        print(f"{subject}: {percentage:.1f}%  Grade {sortGrade(percentage)}")

    overall = calcAvg(percentages)
    print(f"\nOverall average: {overall:.1f}%  Grade {sortGrade(overall)}")


if __name__ == "__main__":
    main()

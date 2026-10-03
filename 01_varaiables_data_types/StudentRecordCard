"""A clean summary of student records, saved correctly to the 
right data type, their averagee score and tells if the students passes/fails"""

#Initialize pass mark for the remark
PASS_MARK = 55.0

#define database of student records saved in a dictionary

students = {
    "Ama Udochi":{"age": 10, "class": "SS1B", "scores": [43, 79, 91, 31]},
    "Ahmadu Usmar":{"age": 15, "class": "SS1C", "scores": [78, 75, 58, 90]},
    "Janet Uwagboi":{"age": 14, "class": "SS1A", "scores": [55, 80, 98, 80]},
    "Tunde Balogun":{"age": 13, "class": "SS1B", "scores": [70, 75, 78, 71]},
    "Bello Onakoya":{"age": 12, "class": "SS1C", "scores": [88, 89, 60, 56]},
    "Abigail Traore":{"age": 11, "class": "SS1A", "scores": [77, 76, 98, 91]},
    "Samuel Akins":{"age": 10, "class": "SS1B", "scores": [70, 44, 68, 91]},
    "Peter Nwangaga":{"age": 16, "class": "SS1C", "scores": [100, 99, 78, 71]},
    "Selome Tai":{"age": 13, "class": "SS1C", "scores": [78, 67, 98, 81]},
    "Favour Martins":{"age": 14, "class": "SS1A", "scores": [66, 77, 99, 33]},
    "Xavier Callister":{"age": 12, "class": "SS1A", "scores": [88, 45, 78, 88]}
}
name = input("Enter Student's name here: ").strip().title()
record = students.get(name)

if record is None:
    print(f"No record found for '{name}'. ")
else:
    average = sum(record["scores"])/len(record["scores"])

    print("\n--- Data types in this record ---")
    for key, value in record.items():
        print(f"{key:10} {value!r:35} {type(value).__name__}")
    print(f"{'average':10} {average!r:35} {type(average).__name__}")
    print(f"{'name':10} {name!r:35} {type(name).__name__}")
    print(f"{'record':10} {'(whole record)':35} {type(record).__name__}")
    print(f"{'students':10} {'(whole database)':35} {type(students).__name__}")

print("\n======STUDENT CARD =========")
print(f"Name:                       {name}")
print(f"Age:                        {record['age']}")
print(f"Class:                      {record['class']}")
print(f"Scores                      {record['scores']}")
print(f"Average:                    {average:.1f}")

if average >= 85:
    print("Remark: Excellent performance!!!")
elif average >= PASS_MARK:
    print("Remark: PASS!!!")
else:
    print("Remark:  FAIL - needs improvement.")
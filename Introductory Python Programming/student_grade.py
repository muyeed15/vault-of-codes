"""
Write a program that will calculate student grades for a given list of students and their corresponding marks.
See the sample input and output for detail. Your program should output the result exactly same as given in
the sample.
Brief Description:
Your program should ask for how many students to calculate the grade. Then take the names and corresponding marks for that many students and store them in a list. Output how many students are there in the list and print the list.
Then for each student in the list calculate grade according to the following grading scheme:
studentMark >= 90: grade = 'A'
studentMark >= 80 and studentMark < 90: grade = 'B' studentMark >= 70 and studentMark < 80: grade = 'C' studentMark >= 60 and studentMark < 70: grade = 'D' Otherwise: grade = 'F'
Store all the calculated grades in the student list corresponding to each student.
Print the list of students, their marks, and grades in a tabular form.
Finally, user can enter a grade to search in the list. The program will print how many students has achieved the given grade.
Sample Input and Output:
Calculate grade for how many students?: 3 Student Name: suha
Enter Marks (0-100):98
Student Name: samah
Enter Marks (0-100):95
Student Name: mou
Enter Marks (0-100):67
Total Number of students: 3
The Marks list is: [['suha', 98], ['samah', 95], ['mou', 67]] [['suha', 98, 'A'], ['samah', 95, 'A'], ['mou', 67, 'D']]
Student Grade Table is as follows
Student Name | Marks | Grade | suha 98 A samah 95 A
mou 67 D
Enter Which Grade to Search: A
Grade A achieved by 2 many students
"""

number = int(input("Calculate grade for how many students?: "))
student_list = []
grade_list = []

for i in range(number):
    name = input("Student Name: ")
    mark = float(input("Enter Marks (0 - 100): "))

    student_list.append([name, mark])

print(f"Total Number of students: {len(student_list)}")
print(f"The Marks list is: {student_list}\n")
print("Student Grade Table is as follows\n")
print("Student Name | Marks | Grade")

def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80 and mark < 90:
        return "B"
    elif mark >= 70 and mark < 80:
        return "C"
    elif mark >= 60 and mark < 70:
        return "D"
    else:
        return "F"

for j in range(number):        
    grade_list.append(grade(student_list[j][1]))
    
    print(student_list[j][0], student_list[j][1], grade_list[j])

search = input("Enter Which Grade to Search: ")
print(f"\nGrade {search} achieved by {grade_list.count(search)} many students")

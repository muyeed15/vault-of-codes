"""
Write a program to carry out the following:
a. Create a student list containing the information: StudentID, Student name, major, contact no,
address using a 2D list. Enter information of 5 Students.
b. Print the 2D list that you have created.
c. Now, add/append a student list in your 2D student list.
d. Update the student’s name in the first student list.
e. Delete the 3rd student list.
f. Write 3 functions that will perform the operations in questions: c, d and e.
g. Create a menu to call these 3 functions to perform the operations.
"""

# a
studentList = [[1, 'Syed Abdullah Al Muyeed', 'CSE', '+8801712345678', 'Mirpur'],
               [2, 'Nafisa Anzum Dipra', 'CSE', '+8801812345678', 'Eskaton'],
               [3, 'Ishrak Alam', 'CSE', '+8801912345678', 'Gaus Nagar'], 
               [4, 'Afraim Romeo', 'CSE', '+8801612345678', 'Malibag'],
               [5, 'Diya Rahman', 'CSE', '+8801512345678', 'Bashundhara R/A']]

# b
print(studentList)

# c
studentList.append([6, "Jamiul Ahmed", "CSE", "+8801312345678", "Mirpur"])

# d
studentList[0][1] = "Muyeed"

# e
studentList.remove(studentList[2]) # d

# f
def addStudent(studentID, studentName, major, contactNo, address):
    studentList.append([studentID, studentName, major, contactNo, address])


def updateName(index, studentName):
    studentList[0][index] = studentName


def deleteStudent(index):
    studentList.remove(studentList[index])


# g
addStudent(3, 'Ishrak Alam', 'CSE', '+8801912345678', 'Gaus Nagar')
updateName(1, "Dipra")
deleteStudent(4)

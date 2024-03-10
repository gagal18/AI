import math
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"

class Subject:
    def __init__(self, name, points):
        self.name = name
        sumPoints = sum(points)
        self.points = sumPoints
        self.grade = math.ceil(sumPoints / 10) if math.ceil(sumPoints / 10) >= 5 else 5
        
    def __repr__(self):
        return f"----{self.name}: {self.grade}"
        
class Student:
    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.subjects = []
    
    def addSubject(self, subject):
        self.subjects.append(subject)
        
    def __repr__(self):
        repr_string = f"Student: {self.name}\n"
        for subj in self.subjects:
            repr_string += str(subj) + "\n"
        return repr_string

if __name__ == "__main__":
    students = {}
    while True :
        line = input()
        if line == "end":
            break
        lines = line.split(",")
        name = " ".join([lines[0], lines[1]])
        index = lines[2]
        student = Student(name, lines[2])
        points = list(map(int, lines[4:]))
        subject = Subject(lines[3], points)
        if(index not in students.keys()):
            students[index] = student
        students[index].addSubject(subject)
        
    for key in students:
        print(students[key])
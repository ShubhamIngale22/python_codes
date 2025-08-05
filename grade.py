class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

student = Student("Shubham", [85, 92, 78])
print(f"Student: {student.name}")
print(f"Average Marks: {student.average():.2f}")

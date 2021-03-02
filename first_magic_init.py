class Student:
    def __init__(self, name, faculty):
        self.name = name
        self.faculty = faculty
    def info(self):
        print(f"# STUDENT: {self.name:20s}, {self.faculty:20s} #")

###############################################
s1 = Student("Jora", "LAW")
s2 = Student("Tanea", "IT")
s3 = Student("Vasea", "HEALTH")

s1.info()
s2.info()
s3.info()

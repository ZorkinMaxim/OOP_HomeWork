class Person:
    def __init__(self, first_name, second_name, qualification=1):
        self.first_name = first_name
        self.second_name = second_name
        self.qualification = qualification

    def __str__(self):
        return f"-= {self.first_name} {self.second_name}, {self.qualification} =-"

    def __del__(self):
        print(f"Good bye mr. {self.first_name} {self.second_name}!")


###################################################################

s1 = Person("Ivan", "Dulin", 10)
s2 = Person("Petr", "Orlov", 5)
s3 = Person("Oleg", "Moroz", 7)

print(s1)
print(s2)
print(s3)

del s2

input()

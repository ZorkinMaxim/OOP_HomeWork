class Person:
    def __init__(self, fullName, dob):
        self.fullName = fullName
        self.dob = dob

    def __str__(self):
        return f"PERSON: {self.fullName:20s} {self.dob:10}"


class Patient(Person):
    def __init__(self, fullName, dob, doi):
        Person.__init__(self, fullName, dob)
        self.doi = doi

    def __str__(self):
        return f"PACIENT: {self.fullName:20s} {self.dob:10} [ill since: {self.doi:10}]"

    def transformToPatient(person, doi):
        patient = Patient(person.fullName, person.dob, doi)
        return patient


class Cured(Patient):
    def __init__(self, fullName, dob, doi, doc):
        Patient.__init__(self, fullName, dob, doi)
        self.doc = doc

    def __str__(self):
        return f"CURED: {self.fullName:20s} {self.dob:10} [ill since: {self.doi:10}], [cured since: {self.doc:10}]"

    def transformToCured(patient, doc):
        cured = Cured(patient.fullName, patient.dob, patient.doi, doc)
        return cured


########################################################################################

firstPerson = Person("Martin Rodrigues", "1990-01-02")
firstPatient = Patient.transformToPatient(firstPerson, "2020-01-02")
firstCured = Cured.transformToCured(firstPatient, "2020-01-17")

print(firstPerson)
print(firstPatient)
print(firstCured)

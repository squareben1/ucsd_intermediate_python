class Student:
    def __init__(self, id, firstName, lastName, courses=None):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.courses = dict() if courses == None else courses

    def gpa(self):
        """Calculates the cumulative grade point average for the student."""
        total = 0
        for key, value in self.courses.items():
            total += float(value)

        return total / len(self.courses.values())

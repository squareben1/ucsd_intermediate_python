class Student:
    def __init__(self, id, firstName, lastName, courses = None):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.courses = dict() if courses == None else courses

class Student(object):
    def __init__(self, id, firstName, lastName, courses=None):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.courses = dict() if courses == None else courses

    def gpa(self):
        """Calculates the cumulative grade point average for the student."""
        total = 0
        if self.courses == {}:
            return total
        else:
            for key, value in self.courses.items():
                total += float(value)

            return total / len(self.courses.values())

    def add_course(self, course, score):
        """adds a new entry into the self.courses member variable where “course” is the item’s key and “score” is its value"""
        try:
            score = float(score)
            assert isinstance(score, float)
            if 0 < score > 4:
                print("UH UH")
            else:
                # append
                self.courses[f"{course}"] = float(score)
                print("self.courses", self.courses)
                return self.courses
        except:
            return self.courses

    def add_courses(self, courses):
        """appends the given dictionary (called “courses”) to the member variable self.courses"""
        # TODO Use assertions to ensure “courses” is a dictionary (type dict)
        self.courses.update(courses)
        return self.courses

    def __str__(self):
        """Print tabular output as specified in rubric."""
        # header:
        # string = f"Year\tInterest\tBalance\n===================================="
        string = ""
        course_list = self.get_course_list()

        string += (f"\n{self.id:>4}\t {self.lastName:5}\t {self.firstName:6}\t{self.gpa()} {course_list:6}")
        print(string)
        return string

    def get_course_list(self):
        course_keys = ""
        try:
            for key in self.courses:
                course_keys += f"{key},"
        except:
            pass

        return course_keys.rstrip(",")


# if __name__ == "__main__":

#     johnnie = Student(123456, "Johnnie", "Smith")
#     print(johnnie.get_course_list())

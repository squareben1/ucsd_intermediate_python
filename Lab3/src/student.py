from functools import reduce


class Student(object):
    def __init__(self, id, firstName, lastName, courses=None):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.courses = dict() if courses == None else courses

    def gpa(self):
        """Calculates the cumulative grade point average for the student."""

        if self.courses == {}:
            return 0
        else:
            # bonus - use reduce to get sum before dividing
            total = reduce(lambda a, b: a + b, self.courses.values())

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
        # string = ""
        course_list = self.get_course_list()
        # TODO Johnnie Smith is messed up - no idea why.
        # string += (f"{self.id:>4}\t {self.lastName:7}\t{self.firstName:8}\t{self.gpa()} {course_list:<6}")
        # print(string)
        return f"{self.id:>4}\t {self.lastName:7}\t{self.firstName:8}\t{self.gpa():.3f} {course_list:<6}"

    def get_course_list(self):
        """Return string of keys of self.course, i.e. course codes only"""
        course_keys = ""
        try:
            for key in self.courses:
                course_keys += f"{key},"
        except:
            pass
        # strip trailing ,
        return course_keys.rstrip(",")

    def __repr__(self):
        """Return simple string of class attrs."""
        # TODO Finish
        return f"{self.id},{self.firstName},{self.lastName},{self.courses}"

    def header():
        """This method returns a string that can used as a header for the results of the __str__ method."""
        return f"{'ID':>1}\t {'Last Name':7}\t{'First Name':8}\t{'GPA'} {'Courses':<6}\n=========================================================================================="

# if __name__ == "__main__":

#     johnnie = Student(123456, "Johnnie", "Smith")
#     print(johnnie.get_course_list())

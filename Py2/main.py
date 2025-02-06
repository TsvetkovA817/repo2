# t2.1

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
    pass

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    pass

def print_st(name):
    print(f'{name}!')

if __name__ == '__main__':
    print_st('Start t1')
    
    best_student = Student('Name_st11', 'Name_st12', 'v')
    best_student.courses_in_progress += ['Python']

    cool_mentor = Mentor('Name_men11', 'Name_men12')
    cool_mentor.courses_attached += ['Python']

    cool_mentor.rate_hw(best_student, 'Python', 10)
    cool_mentor.rate_hw(best_student, 'Python', 10)
    cool_mentor.rate_hw(best_student, 'Python', 10)

    print(best_student.grades)
    print(best_student.name)

    lecturer1=Lecturer('Name_lec11','Name_lec12');
    reviewer1=Reviewer('Name_rev11','Name_rev12');

    print(lecturer1.name)
    print(reviewer1.name)

    print_st('End t1')

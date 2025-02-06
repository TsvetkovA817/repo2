class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def _rate_hw(self, student, course, grade):
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
        self.courses_in_progress = []
        self.grades = {}


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        self._rate_hw(student, course, grade)


def print_st(name):
    print(f'{name}!')

if __name__ == '__main__':
    
    print_st('Start t2')

    best_student = Student('Ruoy', 'Eman', 'your_gender')
    best_student.courses_in_progress += ['Python']

    cool_mentor = Mentor('Some', 'Buddy')
    cool_mentor.courses_attached += ['Python']

    #cool_mentor._rate_hw(best_student, 'Python', 10)
    #cool_mentor._rate_hw(best_student, 'Python', 10)
    #cool_mentor._rate_hw(best_student, 'Python', 10)

    print(best_student.grades)
    print(best_student.name)

    lecturer1=Lecturer('Иван','Петрович');
    reviewer1=Reviewer('Петр','Иванович');
    student2 = Student('Федор', 'Федорович', 'м')

    print(lecturer1.name)
    print(reviewer1.name)

    # добавляем курс преподавателю и студенту
    reviewer1.courses_attached.append('Java')
    student2.courses_in_progress.append('Java')

    # выставляет оценку
    reviewer1.rate_hw(student2, 'Java', 10)
    # оценка выставлена
    print(student2.grades)  # {'Java': [10]}

    # добавляем курс лектору
    lecturer1.courses_in_progress.append('Java')
    # выставляет оценку
    student2.rate_lec(lecturer1, 'Java', 8)
    # оценка выставлена
    print(lecturer1.grades)  # {'Java': [8]}

    print_st('End t2')



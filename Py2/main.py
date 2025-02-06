#t2.4

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

    # Cредняя оценка
    def get_average_grade(self):
        average_grade = 0
        total_sum = 0  # Общая сумма оценок
        total_count = 0  # Общее количество оценок
        # Проходим по всем предметам и их оценкам
        for subject, grade_list in self.grades.items():
            total_sum += sum(grade_list)  # Суммируем оценки по предмету
            total_count += len(grade_list)  # Считаем количество оценок
        # Вычисляем среднюю оценку
        if total_count > 0:
            average_grade = total_sum / total_count
        return average_grade

    def __str__(self):
        # Форматируем строку
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.get_average_grade():.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    # Методы сравнения
    def __eq__(self, other):
        return self.get_average_grade() == other.get_average_grade()

    def __ne__(self, other):
        return self.get_average_grade() != other.get_average_grade()

    def __gt__(self, other):
        return self.get_average_grade() > other.get_average_grade()

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        return self.get_average_grade() <= other.get_average_grade()

    def __ge__(self, other):
        return self.get_average_grade() >= other.get_average_grade()



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

    def __str__(self):
        return self.name


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_average_grade()}'

    # Cредняя оценка
    def get_average_grade(self):
        average_grade = 0
        total_sum = 0  # Общая сумма оценок
        total_count = 0  # Общее количество оценок
        # Проходим по всем предметам и их оценкам
        for subject, grade_list in self.grades.items():
            total_sum += sum(grade_list)  # Суммируем оценки по предмету
            total_count += len(grade_list)  # Считаем количество оценок
        # Вычисляем среднюю оценку
        if total_count > 0:
            average_grade = total_sum / total_count
        return average_grade

    # Методы сравнения
    def __eq__(self, other):
        return self.get_average_grade() == other.get_average_grade()

    def __ne__(self, other):
        return self.get_average_grade() != other.get_average_grade()

    def __gt__(self, other):
        return self.get_average_grade() > other.get_average_grade()

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        return self.get_average_grade() <= other.get_average_grade()

    def __ge__(self, other):
        return self.get_average_grade() >= other.get_average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        self._rate_hw(student, course, grade)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

def print_st(name):
    print(f'{name}!')


# Cредняя оценка по всем студентам
def students_average_grade(students_list, course_name):
    average_grade = 0
    total_sum = 0  # Общая сумма оценок
    total_count = 0  # Общее количество оценок
    # Проходим по всем предметам и их оценкам
    for el in students_list:
        if course_name in el.grades:
            total_sum += sum(el.grades[course_name])  # Суммируем оценки по предмету
            total_count += len(el.grades[course_name])  # Считаем количество оценок
    # Вычисляем среднюю оценку
    if total_count > 0:
        average_grade = total_sum / total_count
    return average_grade

# Cредняя оценка по всем лекторам
def lecturers_average_grade(lecturers_list, course_name):
    average_grade = 0
    total_sum = 0  # Общая сумма оценок
    total_count = 0  # Общее количество оценок
    # Проходим по всем предметам и их оценкам
    for el in lecturers_list:
        if course_name in el.grades:
            total_sum += sum(el.grades[course_name])  # Суммируем оценки по предмету
            total_count += len(el.grades[course_name])  # Считаем количество оценок
    # Вычисляем среднюю оценку
    if total_count > 0:
        average_grade = total_sum / total_count
    return average_grade


if __name__ == '__main__':
    print_st('Start t4')

    student1 = Student('Name_st11', 'Name_st12', 'v')
    student1.courses_in_progress += ['Python']
    student2 = Student('Name_st21', 'Name_st22', 'v')
    student2.courses_in_progress += ['Python']

    cool_mentor = Mentor('Name_men11', 'Name_men12')
    cool_mentor.courses_attached += ['Python']
    mentor2 = Mentor('Name_men21', 'Name_men22')
    mentor2.courses_attached += ['Java']


    lecturer1 = Lecturer('Name_le11', 'Name_le12');
    lecturer2=Lecturer('Name_le21','Name_le22');

    reviewer1 = Reviewer('Name_re11', 'Name_re12');
    reviewer2=Reviewer('Name_re21','Name_re22');

    print(lecturer1.name)
    print(reviewer1.name)

    # добавляем курс преподавателю и студенту
    reviewer1.courses_attached.append('Java')
    reviewer2.courses_attached.append('Python')
    student1.courses_in_progress.append('Java')
    student2.courses_in_progress.append('Java')
    student2.finished_courses += ['Введение в программирование']

    # выставляет оценку
    reviewer1.rate_hw(student1, 'Python', 10)
    reviewer1.rate_hw(student2, 'Java', 10)
    reviewer1.rate_hw(student1, 'Python', 7)
    reviewer1.rate_hw(student2, 'Java', 8)
    reviewer1.rate_hw(student1, 'Java', 8)
    reviewer1.rate_hw(student1, 'Java', 9)
    reviewer2.rate_hw(student1, 'Python', 4)
    reviewer2.rate_hw(student1, 'Python', 6)

    # оценка выставлена
    print('1> ', student2.grades)  # {'Java': [10]}

    print(student1.grades)
    print(student1.name)

    # добавляем курс лектору
    lecturer1.courses_in_progress.append('Java')
    lecturer1.courses_in_progress.append('Python')
    lecturer2.courses_in_progress.append('Python')

    # выставляет оценку
    student1.rate_lec(lecturer1, 'Python', 10)
    student2.rate_lec(lecturer1, 'Java', 8)
    student2.rate_lec(lecturer1, 'Python', 6)
    student1.rate_lec(lecturer2, 'Python', 4)
    # оценка выставлена
    print('2> ', lecturer1.grades)  #  {'Python': [10, 6], 'Java': [8]}
    # оценка выставлена
    print('3> ', lecturer1.courses_in_progress) # ['Java', 'Python']
    print('4> ', lecturer1.grades)  # {'Java': [8], 'Python': [10]}

    #__str__
    print('----')
    print(student2)
    print('----')
    print(reviewer1)
    print('----')
    print(lecturer1)

    # Cравнение
    print('----')
    print(student2.get_average_grade())
    print(student1.get_average_grade())
    print(student2==student1)
    reviewer1.rate_hw(student2, 'Java', 7)
    print('5> ', student2.grades)  # {'Java': [10, 8, 7]}
    print(f"{student2.get_average_grade():.1f}")
    print(f"{student1.get_average_grade():.1f}")
    print(student2==student1)
    print(student1>student2)
    print(lecturer1 >= lecturer2)

    print('6> ', student1.grades)  # {'Java': [8, 9], 'Python': [4, 6]}
    print('7> ', student2.grades)  # {'Java': [10, 8, 7]}
    students = [student1, student2]
    course = "Java"
    print(f"{students_average_grade(students,course):.1f}")  #8.4

    print('8> ', lecturer1.grades)  # {'Python': [10, 6], 'Java': [8]}
    print('9> ', lecturer2.grades)  # {'Python': [4]}
    lecturers = [lecturer1, lecturer2]
    course = "Python"
    print(f"{lecturers_average_grade(lecturers, course):.1f}")  #6.7

    print_st('End t4')

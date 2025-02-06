#t2.3

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

if __name__ == '__main__':
    print_st('Start t3')

    best_student = Student('Ruoy', 'Eman', 'v')
    best_student.courses_in_progress += ['Python']

    cool_mentor = Mentor('Some', 'Buddy')
    cool_mentor.courses_attached += ['Python']

    print(best_student.grades)
    print(best_student.name)

    lecturer1=Lecturer('Name_lec11','Name_lec12');
    reviewer1=Reviewer('Name_rev11','Name_rev12');
    student2 = Student('Name_st21', 'Name_st22', 'm')

    print(lecturer1.name)
    print(reviewer1.name)

    # добавляем курс преподавателю и студенту
    reviewer1.courses_attached.append('Java')
    student2.courses_in_progress.append('Java')
    student2.finished_courses += ['Введение в программирование']

    # выставляет оценку
    reviewer1.rate_hw(student2, 'Java', 10)
    # оценка выставлена
    print('1> ', student2.grades)  # {'Java': [10]}

    # добавляем курс лектору
    lecturer1.courses_in_progress.append('Java')
    # выставляет оценку
    student2.rate_lec(lecturer1, 'Java', 8)
    # оценка выставлена
    print('2> ', lecturer1.grades)  # {'Java': [8]}
    #
    lecturer1.courses_in_progress += ['Python']
    best_student.rate_lec(lecturer1, 'Python', 10)
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
    print(best_student.get_average_grade())
    print(student2==best_student)
    reviewer1.rate_hw(student2, 'Java', 7)
    print('5> ', student2.grades)  # {'Java': [10, 7]}
    print(student2.get_average_grade())
    print(best_student.get_average_grade())
    print(student2==best_student)
    print(best_student>student2)

    print_st('End t3')

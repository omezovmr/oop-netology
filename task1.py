class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        avg_score = self.get_avg_grade()

        # return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_score}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

        stroki = [
            f'Имя: {self.name}',
            f'Фамилия: {self.surname}',
            f'Средняя оценка за домашние задания: {avg_score}',
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}',
            f'Завершенные курсы: {", ".join(self.finished_courses)}'
        ]
        return '\n'.join(stroki)

    def get_avg_grade(self):
        all_grades = []
        for a in self.grades.values():
            all_grades += a
        return sum(all_grades) / len(all_grades)

    def __gt__(self, other):
        return self.get_avg_grade() > other.get_avg_grade()

    def __lt__(self, other):
        return self.get_avg_grade() < other.get_avg_grade()

    def __eq__(self, other):
        return self.get_avg_grade() == other.get_avg_grade()

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
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

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_avg_grade(self):
        all_grades = []
        for a in self.grades.values():
            all_grades += a
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        avg_score = self.get_avg_grade()
        return f'{super().__str__()}\nСредняя оценка за лекции: {avg_score}'

    def __gt__(self, other):
        return self.get_avg_grade() > other.get_avg_grade()

    def __lt__(self, other):
        return self.get_avg_grade() < other.get_avg_grade()

    def __eq__(self, other):
        return self.get_avg_grade() == other.get_avg_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

##ПРОВЕРКА ПЕРВОЙ ЧАСТИ

# lecturer = Lecturer('Иван', 'Иванов')
# reviewer = Reviewer('Пётр', 'Петров')
# print(isinstance(lecturer, Mentor)) # True
# print(isinstance(reviewer, Mentor)) # True
# print(lecturer.courses_attached)    # []
# print(reviewer.courses_attached)    # []

##ПРОВЕРКА ВТОРОЙ ЧАСТИ

# lecturer = Lecturer('Иван', 'Иванов')
# reviewer = Reviewer('Пётр', 'Петров')
# student = Student('Алёхина', 'Ольга', 'Ж')
#
# student.courses_in_progress += ['Python', 'Java']
# lecturer.courses_attached += ['Python', 'C++']
# reviewer.courses_attached += ['Python', 'C++']
#
# print(student.rate_lecture(lecturer, 'Python', 7))  # None
# print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
# print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
# print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка
#
# print(lecturer.grades)  # {'Python': [7]}

##ПРОВЕРКА ТРЕТЬЕЙ ЧАСТИ

# print(reviewer)

# lecturer.grades = {'Python': [2, 3, 4, 5, 5, 4, 3, 2, 1]}
# print(lecturer)
#
# student.grades = {'Python': [2, 3, 4, 5, 5, 4, 3, 2, 1]}
# student.courses_in_progress = ['Java', 'C++']
# student.finished_courses = ['AI']
# print(student)

##ИТОГОВАЯ ПРОВЕРКА (4 ЗАДАНИЕ)

student1 = Student('Александр', 'Македонский', 'М')
student2 = Student('Анна', 'Каренина', 'Ж')
student1.courses_in_progress += ['Python']
student2.courses_in_progress += ['Python']

lecturer1 = Lecturer('Петр', 'Степанян')
lecturer2 = Lecturer('Александр', 'Пушкин')
lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Python']

reviewer1 = Reviewer('Ольга', 'Цимбалюк')
reviewer2 = Reviewer('Игорь', 'Николаев')
reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['Python']

reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 10)

student1.rate_lecture(lecturer1, 'Python', 7)
student2.rate_lecture(lecturer2, 'Python', 9)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

print(student1 > student2)
print(lecturer1 < lecturer2)

def average_hw_grade(students, course):
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades += student.grades[course]
    return sum(all_grades) / len(all_grades)

def average_lecture_grade(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades += lecturer.grades[course]
    return sum(all_grades) / len(all_grades)

print(average_hw_grade([student1, student2], 'Python'))
print(average_lecture_grade([lecturer1, lecturer2], 'Python'))
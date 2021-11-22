class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):  # выставление оценок за курс лекторам
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_score(self):  # средняя оценка
        counter = 0
        sum_ = 0
        for course in self.grades:
            for grade in self.grades[course]:
                sum_ += grade
                counter += 1
        res = sum_ / counter
        return res

    def __str__(self):
        res = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.average_score()}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы: {", ".join(self.finished_courses)}'''
        return res

    def __lt__(self, student):
        if not isinstance(student, Student):
            print('Not a Student!')
            return
        return self.average_score() < student.average_score()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):  # лекторы
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_score(self):  # средняя оценка
        counter = 0
        sum_ = 0
        for course in self.grades:
            for grade in self.grades[course]:
                sum_ += grade
                counter += 1
        res = sum_ / counter
        return res

    def __str__(self):
        res = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.average_score()}'''
        return res

    def __lt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            print('Not a Student!')
            return
        return self.average_score() < lecturer.average_score()


class Reviewer(Mentor):  # эксперты, проверяющие домашние задания
    def rate_hw(self, student, course, grade):  # выставление оценок за курс студентам
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'''Имя: {self.name}
Фамилия: {self.surname}'''
        return res


best_student_1 = Student('Harry', 'Potter', 'man')
best_student_2 = Student('Hermione', 'Granger', 'woman')
best_students = [best_student_1, best_student_2]
cool_lecturer_1 = Lecturer('Albus', 'Dumbledore')
cool_lecturer_2 = Lecturer('Severus', 'Snape')
cool_lecturers = [cool_lecturer_1, cool_lecturer_2]
super_reviewer_1 = Reviewer('Fred', 'Weasley')
super_reviewer_2 = Reviewer('George', 'Weasley')

best_student_1.finished_courses += ['SQL']
best_student_1.courses_in_progress += ['Python']
best_student_1.courses_in_progress += ['Java']
best_student_2.finished_courses += ['SQL']
best_student_2.courses_in_progress += ['Python']
best_student_2.courses_in_progress += ['Java']
cool_lecturer_1.courses_attached += ['Python']
cool_lecturer_2.courses_attached += ['Java']
super_reviewer_1.courses_attached += ['Python']
super_reviewer_2.courses_attached += ['Java']

super_reviewer_1.rate_hw(best_student_1, 'Python', 10)
super_reviewer_1.rate_hw(best_student_2, 'Python', 9)
super_reviewer_2.rate_hw(best_student_1, 'Java', 2)
super_reviewer_2.rate_hw(best_student_2, 'Java', 4)

best_student_1.rate_hw(cool_lecturer_1, 'Python', 6)
best_student_2.rate_hw(cool_lecturer_1, 'Python', 5)
best_student_1.rate_hw(cool_lecturer_2, 'Java', 8)
best_student_2.rate_hw(cool_lecturer_2, 'Java', 10)

print('Students:')
print(best_student_1)
print(best_student_2)
print()
print('Lecturers:')
print(cool_lecturer_1)
print(cool_lecturer_2)
print()
print('Reviewers:')
print(super_reviewer_1)
print(super_reviewer_2)
print()
print(best_student_1 > best_student_2)
print()


def score_student(best_student, course):
    counter = 0
    sum_ = 0
    for student in best_student:
        for courses in student.grades:
            if courses == course:
                for grade in student.grades[courses]:
                    sum_ += grade
                    counter += 1
    res = sum_ / counter
    return res

def score_lecturer(cool_lecturer, course):
    counter = 0
    sum_ = 0
    for lecturer in cool_lecturer:
        for courses in lecturer.grades:
            if courses == course:
                for grade in lecturer.grades[courses]:
                    sum_ += grade
                    counter += 1
    res = sum_ / counter
    return res


print(f"Средняя оценка среди всех студентов по курсу Python - {score_student(best_students, 'Python')}")
print(f"Средняя оценка среди всех студентов по курсу Java - {score_student(best_students, 'Java')}")
print(f"Средняя оценка среди всех лекторов по курсу Python - {score_lecturer(cool_lecturers, 'Python')}")
print(f"Средняя оценка среди всех лекторов по курсу Java - {score_lecturer(cool_lecturers, 'Java')}")
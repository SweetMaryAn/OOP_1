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
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_hw(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        x = 0
        x1 = 0
        for i, e in self.grades.items():
            for j in e:
                x += j
                x1 += 1
        if x1 == 0:
            x1 = 1
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {x/x1}\nКурсы в процессе изучения: {course(self)}\nЗавершённые курсы: {end_course(self)}"
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def __str__(self):
        x = 0
        x1 = 0
        for i, e in self.grades.items():
            for j in e:
                x += j
                x1 += 1
        if x1 == 0:
            x1 = 1
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {x/x1}"
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"
def course(selfi):
    x = ''
    for i in selfi.courses_in_progress:
        x += i+', '
    return x[0:-2]
def end_course(selfi):
    x = ''
    for i in selfi.finished_courses:
        x += i+', '
    return x[0:-2]
def student_grade(list_student, course):
    x = 0
    x1 = 0
    for student in list_student:
        if course in student.grades:
            x += sum(student.grades[course])
            x1 += len(student.grades[course])
    print(x/x1)
def lectourer_grade(list_lector, course):
    x = 0
    x1 = 0
    for lector in list_lector:
        if course in lector.grades:
            x += sum(lector.grades[course])
            x1 += len(lector.grades[course])
    print(x/x1)
best_student = Student('Ruoy', 'Eman', 'man')
best_student.courses_in_progress += ['Python']

cool_student = Student('Sue', 'Joulin', 'woman')
cool_student.courses_in_progress += ['Python', 'Java']
cool_student.finished_courses += ['Git']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
 
best_reviewer = Reviewer('Max', 'Sikon')
best_reviewer.courses_attached += ['Python', 'Git', 'Java']

cool_lector = Lecturer('Sofa', 'Rison')
cool_lector.courses_attached += ['Git', 'Java']

best_lector = Lecturer('Bard', 'Frimol')
best_lector.courses_attached += ['Python', 'Java', 'Git']

best_student.rate_hw(best_lector,'Python',9)
best_reviewer.rate_hw(cool_student,'Python',10)
best_reviewer.rate_hw(cool_student,'Python',8)
best_reviewer.rate_hw(cool_student,'Python',7)
best_reviewer.rate_hw(best_student,'Python',9)

student_grade([cool_student, best_student], 'Python')

print(cool_student)
print(best_reviewer)
print(cool_lector)
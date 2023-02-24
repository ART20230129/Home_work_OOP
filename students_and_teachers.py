class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []  #какие курсы студент уже прошел
        self.courses_in_progress = []   #информацию о списке курсов, которые сейчас изучаются
        self.grades = {}  #информацию студентов об оценках

    def rate_lectures(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def average_raiting_st(self):
        new_list = []
        for value in self.grades.values():
            new_list.extend(value)
        summ_raiting = sum(new_list)
        number_of_ratings = len(new_list)
        return round(summ_raiting / number_of_ratings, 1)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_raiting_st()}\nКурсы в процессе: {", ".join(self.courses_in_progress)}\nЗавершённые курсы: {"".join(self.finished_courses)}'
        return res

    #     добавим возможность сравнения студентов
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не является экземпляром класса Student!')
            return
        return self.average_raiting_st() < other.average_raiting_st()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.courses_in_progress = []
        self.grades = {}

    def average_raiting(self):
        new_list = []
        for value in self.grades.values():
            new_list.extend(value)
        summ_raiting = sum(new_list)
        number_of_ratings = len(new_list)
        return round(summ_raiting / number_of_ratings, 1)


    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя отенка за лекции: {self.average_raiting()}'
        return res

    #     добавим возможность сравнения лекторов
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не является экземпляром класса Lecturer!')
            return
        return self.average_raiting() < other.average_raiting()




class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

# метод, который будет проверять, что оценка выставляется именно
#экземпляру класса Student, при этом преподаватель должен быть прикреплен
#к соответствующему курсу, а студент должен его проходить

    def raiting_st(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

student_one = Student('Иван', 'Иванов', 'мужчина')
student_one.finished_courses +=['Введение в программирование']
student_one.courses_in_progress +=['Python']
student_one.courses_in_progress +=['Git']


student_two = Student('Мария', 'Петрова', 'женщина')
student_two.finished_courses +=['Введение в программирование']
student_two.courses_in_progress +=['Python']
student_two.courses_in_progress +=['Git']


lecturer_one = Lecturer('Александр', 'Александров')
lecturer_one.courses_attached +=['Python']
lecturer_one.courses_in_progress +=['Python']
student_one.rate_lectures(lecturer_one, 'Python', 8)
student_one.rate_lectures(lecturer_one, 'Python', 9)
student_one.rate_lectures(lecturer_one, 'Python', 10)
student_one.rate_lectures(lecturer_one, 'Python', 7)

lecturer_two = Lecturer('Алексей', 'Алексеев')
lecturer_two.courses_attached +=['Python']
lecturer_two.courses_in_progress +=['Python']
student_two.rate_lectures(lecturer_two, 'Python', 10)
student_two.rate_lectures(lecturer_two, 'Python', 9)
student_two.rate_lectures(lecturer_two, 'Python', 10)
student_two.rate_lectures(lecturer_two, 'Python', 9)


reviewer_one = Reviewer('Петр', 'Петров')
reviewer_one.courses_attached +=['Python']
reviewer_one.courses_attached +=['Git']
reviewer_one.raiting_st(student_one, 'Python', 8)
reviewer_one.raiting_st(student_one, 'Python', 9)
reviewer_one.raiting_st(student_one, 'Python', 7)
reviewer_one.raiting_st(student_one, 'Python', 10)

reviewer_two = Reviewer('Сергей', 'Сергеев')
reviewer_two.courses_attached +=['Python']
reviewer_two.courses_attached +=['Git']
reviewer_two.raiting_st(student_two, 'Python', 9)
reviewer_two.raiting_st(student_two, 'Python', 7)
reviewer_two.raiting_st(student_two, 'Python', 8)
reviewer_two.raiting_st(student_two, 'Python', 8)



print('Проверяющие')
print(reviewer_one)
print()
print(reviewer_two)
print("-----------------------------------------------------------------------")
print('Лекторы')
print(lecturer_one)
print()
print(lecturer_two)
print()

# Выводим данные лучшего лектора
if lecturer_one.__lt__(lecturer_two):
    print(f'{lecturer_two.name} {lecturer_two.surname} - лучший лектор!')
else:
    print(f'{lecturer_one.name} {lecturer_one.surname} - лучший лектор!')
print("-----------------------------------------------------------------------")

print('Студенты')
print(student_one)
print()
print(student_two)
print()


# Выводим данные лучшего студента
if student_one.__lt__(student_two):
    print(f'{student_two.name} {student_two.surname} - лучший студент!')
else:
    print(f'{student_one.name} {student_one.surname} - лучший студент!')
print("-----------------------------------------------------------------------")

#подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса
students_list = [student_one, student_two]
def average_evaluations_students(students, course):
    new_list = []
    for student in students_list:
        if isinstance(student, Student) and course in student.grades:
            new_list.extend(student.grades[course])
        else:
            print("Ошибка!")
            return
    return f'Средняя оценка за домашние задания по курсу {course}: {round(sum(new_list)/len(new_list), 2)}'


print(average_evaluations_students(students_list, 'Python'))
print('-----------------------------------------------------------------------')

#подсчет средней оценки за лекции всех лекторов в рамках курса
lecturers_list = [lecturer_one, lecturer_two]
def average_evaluations_lecturers(lecturers, course):
    new_list = []
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.grades:
            new_list.extend(lecturer.grades[course])
        else:
            print("Ошибка!")
            return
    return f'Средняя оценка за лекции всех лекторов в рамках курса {course}: {round(sum(new_list)/len(new_list), 2)}'


print(average_evaluations_lecturers(lecturers_list, 'Python'))
print('-----------------------------------------------------------------------')


import datetime

class Student:
  min_avg = 4.5
  university = 'New York Academy'

  def __init__(self, name, last, age, student_avg):
    self.name = name
    self.last = last
    self.age = age
    self.student_avg = student_avg

  def __repr__(self):
    return self.name.capitalize() + " " + self.last.capitalize()

  def email(self):
    return '{}.{}.university.com'.format(self.name, self.last)

  def grant_scholarship(self):
    if self.student_avg > self.min_avg:
      print('Przyznano stypendium')
    else:
      print('Odmowa przyznania stypendium')




@classmethod
def set_min_avg(cls, average):
    cls.min_avg = average

@staticmethod
def academic_day(day):
  if day.weekday() == 5 or day.weekday() == 6:
    return False
  else:
    return True


obj_anna = Student('anna', 'kowalska', 23, 4.7)
obj_arek = Student('arkadiusz', 'nowak', 21, 3.9)
print(Student.min_avg)
print(obj_anna.min_avg)
print(obj_arek.min_avg)

obj_anna.set_min_avg(4.8)
print('Min srednia dla obiektu anna', obj_anna.min_avg)
print('Min srednia dla obiektu arek', obj_arek.min_avg)

today = datetime.date.today()
print(today)

#-----------------------------------------------------------------------------

import datetime

class Student:
    min_avg = 4.5
    university = 'New York Academy'

    def __init__(self, name, last, age, student_avg):
        self.name = name
        self.last = last
        self.age = age
        self.student_avg = student_avg

    def __repr__(self):
        return self.name.capitalize() + " " + self.last.capitalize()

    def email(self):
        return '{}.{}.university.com'.format(self.name, self.last)

    def grant_scholarship(self):
        if self.student_avg > self.min_avg:
            print('Przyznano stypendium')
        else:
            print('Odmowa przyznania stypendium')

    @classmethod
    def set_min_avg(cls, average):
        cls.min_avg = average

    @staticmethod
    def academic_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return 'Nie'
        else:
            return 'Tak'


today = datetime.date.today()

print('Czy dzisiaj są zajęcia? ', Student.academic_day(today))

# #------------------------------------------------------------------------
# import holidays
#
# class Student:
#   min_avg = 4.5
#   university = 'New York Academy'
#
#   def __init__(self, name, last, age, student_avg):
#     self.name = name
#     self.last = last
#     self.age = age
#     self.student_avg = student_avg
#
#   def __repr__(self):
#     return self.name.capitalize() + " " + self.last.capitalize()
#
#   def (self):
#       return
#
#   @property
#   def email(self):
#     return '{}.{}.university.com'.format(self.name, self.last)
#
#   def grant_scholarship(self):
#     if self.student_avg > self.min_avg:
#       print('Przyznano stypendium')
#     else:
#       print('Odmowa przyznania stypendium')
# @staticmethod
# def academic_football_team_cheer():
#     return "Go go NYA"
# print(Student.academic_football_cheer())
#
#
# obj_anna = Student('anna', 'kowalska', 23, 4.7)
# obj_arek = Student('arkadiusz', 'nowak', 21, 3.9)
#
# print(obj_anna.min_avg)
# print(Student.min_avg)
#
#
# today = datetime.date.today()
# print(today, 'zajęcia się odbywają:', Student.academic_day(today))
#
# saturday = datetime.datetime.strptime('2019-06-22', '%Y-%m-%d')
# print(saturday, 'zajęcia się odbywają:', Student.academic_day(saturday))
#
# sunday = datetime.date.today() - datetime.timedelta(days=1)
# print(sunday, 'zajęcia się odbywają:', Student.academic_day(sunday))


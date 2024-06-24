from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, yob:int):
        self._name = name
        self._yob = yob
    @abstractmethod
    def describe(self):
        pass
    def get_yob(self):
        return self._yob
    
class Student(Person):
    def __init__(self, name:str, yob:int, grade:str):
        super().__init__(name=name, yob=yob)
        self.__grade = grade

    def describe(self):
        print(f"Student: Name {self._name}, Yob: {self._yob}, Grade: {self.__grade}")

class Teacher(Person):
    def __init__(self, name: str, yob: int, subject:str):
        super().__init__(name, yob)
        self.__subject = subject
     
    def describe(self):
        print(f"Doctor: Name {self._name}, Yob: {self._yob}, Grade: {self.__subject}")

class Doctor(Person):
    def __init__(self, name:str, yob:int, specialist: str):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(f"Doctor: Name {self._name}, Yob: {self._yob}, Specialist: {self.__specialist}")


class Ward:
    def __init__(self, name: str) :
        self.__name = name
        self.__list_people = list()
    def add_person(self, p:Person):
        self.__list_people.append(p)

    def describe(self):
        print(f"War Name: {self.__name}")
        for p in self.__list_people:
            p.describe()
    def count_doctor(self):
        count = 0
        for p in self.__list_people:
            if isinstance(p,Doctor):
                count +=1
        return count
    
    def sort_yob(self):
        return self.__list_people.sort(lambda x:x.getyob(), reverse=True)
    

    def compute_average(self):
        total = 0
        count = 0
        for p in self.__list_people:
            if isinstance(p,Doctor):
                count +=1
                total += p.get_yob()
        return total/count
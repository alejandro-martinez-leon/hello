import datetime

class Person:

    def __init__(self, name:str, birthday:list[int]) -> None:
        """The constructor

        Parameters
        ----------
        name : str
            The name of the person
        birthday : list[int]
        His birthday in (year, month, day)
        """
        self.name = name
        self.birthday = datetime.date(*birthday)

    @property
    def age(self):
        return datetime.date.today().year - self.birthday.year

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name = {self.name}, age = {self.age})"

if __name__ == "__main__":
    print(Person('Pepe', (2020, 9, 9)))
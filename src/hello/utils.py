from hello.register import Person
def average_age(persons: list[Person]):
    """It prints the average age of the persons

    Parameters
    ----------
    persons : list[Person]
        list of persons
    
    Example
    -------
    .. ipython:: python

        from hello.utils import average_age
        from hello.register import Person
        result = average_age(
            [
                Person('Pepe', (2020, 12, 3)),
                Person('Ana', (2022, 2, 4)),
                Person('John', (2000, 2, 20)),
            ]
        )
        print(result)
        print(Person('Pepe', (2020, 12, 3)))
    """
    return sum([person.age for person in persons]) / len(persons)
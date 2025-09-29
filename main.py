from dataclasses import dataclass, field
from sortedcontainers import SortedSet, SortedKeyList

@dataclass(order=True, frozen=True)
class Person:
    id: int
    age: int = field(compare=False)

class Club:
    def __init__(self):
        self.__sorted_set: SortedSet = SortedSet()
        self.__sorted_key_list: SortedKeyList = SortedKeyList(
                key=lambda p: (p.age, p.id)
        )

    def add_person(self, person: Person) -> None:
        """Add person to the club. Raise ValueError if it is already in the club."""
        if person in self.__sorted_set:
            raise ValueError(f"Person with id {person.id} already exists")
        self.__sorted_set.add(person)
        self.__sorted_key_list.add(person)

    def get_all_sorted_by_id(self) -> list[Person]:
        """Return a list of all club members sorted by id."""
        return list(self.__sorted_set)

    def get_all_sorted_by_age_id(self) -> list[Person]:
        """Return a list of all club members sorted by age and id."""
        return list(self.__sorted_key_list)

    def get_persons_by_age(self, min_age: int, max_age: int) -> list[Person]:
        """
        Return a list of the club members, whose age is within the inclusive range: [min_age, max_age].
        Sort the result by age and id.
        """
        left: int = self.__sorted_key_list.bisect_left(Person(-1, min_age))
        right: int = self.__sorted_key_list.bisect_left(Person(-1, max_age + 1))
        return list(self.__sorted_key_list[left:right])

if __name__ == '__main__':
    person1: Person = Person(100, 29)
    person2: Person = Person(500, 25)
    person3: Person = Person(300, 30)
    person3_1 = Person(300, 55)

    print(f"person1 < person2 == {person1 < person2}")
    print(f"person3 == person3_1 == {person3 == person3_1}")

    club: Club = Club()
    club.add_person(person1)
    club.add_person(person2)
    club.add_person(person3_1)

    print(f"All members sorted by id: {club.get_all_sorted_by_id()}")
    print(f"All members sorted by age, id: {club.get_all_sorted_by_age_id()}")
    print(f"Persons between 25 and 29: {club.get_persons_by_age(25, 29)}")
    print(f"Persons between 77 and 79: {club.get_persons_by_age(77, 79)}")

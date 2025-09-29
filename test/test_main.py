import unittest as ut
from main import *

class TestClub(ut.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.persons = [
            Person(500, 35),
            Person(100, 45),
            Person(300, 39),
            Person(200, 46),
        ]
        cls.not_a_member = Person(1000, 43)

    def setUp(self):
        super().setUp()
        self.club = Club()
        for p in self.persons:
            self.club.add_person(p)

    def test_add_person_throws(self):
        self.assertRaises(ValueError, self.club.add_person, self.persons[0])

    def test_add_person_ok(self):
        self.club.add_person(self.not_a_member)
        all_sorted_by_id: list[Person] = sorted(self.persons + [self.not_a_member], key=lambda p: p.id)
        self.assertEqual(self.club.get_all_sorted_by_id(), all_sorted_by_id)

    def test_get_all_sorted_by_id(self):
        all_sorted_by_id: list[Person] = sorted(self.persons, key=lambda p: p.id)
        self.assertEqual(self.club.get_all_sorted_by_id(), all_sorted_by_id)

    def test_get_all_sorted_by_age_id(self):
        all_sorted_by_age_id: list[Person] = sorted(self.persons, key=lambda p: (p.age, p.id))
        self.assertEqual(self.club.get_all_sorted_by_age_id(), all_sorted_by_age_id)

    def test_get_persons_by_age_exists(self):
        from36to45: list[Person] = sorted([self.persons[1], self.persons[2]], key=lambda p: (p.age, p.id))
        self.assertEqual(self.club.get_persons_by_age(36, 45), from36to45)

    def test_get_persons_by_age_not_exists(self):
        self.assertEqual(self.club.get_persons_by_age(20, 30), [])

if __name__ == '__main__':
    ut.main()
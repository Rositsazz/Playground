import unittest

from elevator import elevator_steps


class TestElevator(unittest.TestCase):
    def test_empty_elevator(self):
        self.assertEqual(0, elevator_steps([], [], 5, 2, 200))
        self.assertEqual(0, elevator_steps([40, 50], [], 5, 2, 200))
        self.assertEqual(0, elevator_steps([], [3, 4], 5, 2, 200))

    def test_if_person_floor_is_gt_elevator_max_floor(self):
        with self.assertRaises(Exception):
            elevator_steps([50, 70], [3, 8], 5, 2, 200)

    def test_elevator_steps_when_different_floors(self):
        self.assertEqual(5, elevator_steps([80, 60, 40], [2, 3, 5], 5, 2, 200))

    def test_elevator_steps_when_the_same_floors(self):
        self.assertEqual(6, elevator_steps([40, 40, 100, 80, 60], [2, 3, 3, 2, 3], 3, 5, 200))

    def test_elevator_all_passengers_to_one_floor_max_size(self):
        self.assertEqual(6, elevator_steps([100, 101, 104], [4, 4, 4], 5, 3, 105))

    def test_elevator_overweight(self):
        with self.assertRaises(Exception):
            elevator_steps([100, 101, 500], [4, 4, 4], 5, 3, 105)


if __name__ == '__main__':
    unittest.main()

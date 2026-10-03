"""tests/test_thai_year.py

เทสต์สำหรับโมดูล thai_year.py (to_gregorian / to_buddhist)
รันด้วย: python -m unittest -v
"""

import unittest

from thai_year import to_buddhist, to_gregorian


class TestToGregorian(unittest.TestCase):
    def test_buddhist_year_converts_to_gregorian(self):
        # ปี พ.ศ. 2567 -> ค.ศ. 2024
        self.assertEqual(to_gregorian(2567), 2024)

    def test_gregorian_year_stays_the_same(self):
        # ปี ค.ศ. 2024 (ต่ำกว่า 2400) -> คงค่าเดิม
        self.assertEqual(to_gregorian(2024), 2024)

    def test_boundary_2399_treated_as_gregorian(self):
        # 2399 < 2400 ถือเป็น ค.ศ. -> คงค่าเดิม
        self.assertEqual(to_gregorian(2399), 2399)

    def test_boundary_2400_treated_as_buddhist(self):
        # 2400 >= 2400 ถือเป็น พ.ศ. -> ลบ 543
        self.assertEqual(to_gregorian(2400), 1857)

    def test_non_int_raises_value_error(self):
        for bad_value in ["2567", 2567.0, None, [2567], {}, True, False]:
            with self.subTest(bad_value=bad_value):
                with self.assertRaises(ValueError):
                    to_gregorian(bad_value)


class TestToBuddhist(unittest.TestCase):
    def test_gregorian_year_converts_to_buddhist(self):
        # ปี ค.ศ. 2024 -> พ.ศ. 2567
        self.assertEqual(to_buddhist(2024), 2567)

    def test_buddhist_year_stays_the_same(self):
        # ปี พ.ศ. 2567 (>= 2400) -> คงค่าเดิม
        self.assertEqual(to_buddhist(2567), 2567)

    def test_boundary_2399_treated_as_gregorian(self):
        # 2399 < 2400 ถือเป็น ค.ศ. -> บวก 543
        self.assertEqual(to_buddhist(2399), 2942)

    def test_boundary_2400_treated_as_buddhist(self):
        # 2400 >= 2400 ถือเป็น พ.ศ. -> คงค่าเดิม
        self.assertEqual(to_buddhist(2400), 2400)

    def test_non_int_raises_value_error(self):
        for bad_value in ["2024", 2024.0, None, [2024], {}, True, False]:
            with self.subTest(bad_value=bad_value):
                with self.assertRaises(ValueError):
                    to_buddhist(bad_value)


class TestRoundTrip(unittest.TestCase):
    def test_round_trip_gregorian_to_buddhist_to_gregorian(self):
        original = 2024
        self.assertEqual(to_gregorian(to_buddhist(original)), original)

    def test_round_trip_buddhist_to_gregorian_to_buddhist(self):
        original = 2567
        self.assertEqual(to_buddhist(to_gregorian(original)), original)


if __name__ == "__main__":
    unittest.main()

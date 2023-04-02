import unittest
from models.cod_profile import CodProfile

class TestCodProfile(unittest.TestCase):

    def setUp(self):
        self.codprofile_1=CodProfile("BlackRaven", 1000, 2000, 345, "PS5", "hemlock")

    # def test_codprofile_has_name(self):
    #     self.assertEqual("BlackRaven", self.codprofile_1)

    def test_kd_ratio(self):
        kd_ratio = 1000 / 2000
        self.assertAlmostEqual(0.5, kd_ratio)
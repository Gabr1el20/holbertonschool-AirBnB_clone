import unittest

from models.amenity import Amenity


class AmenityTest(unittest.TestCase):
    """ Unit tests for the Amenity class """

    def test_init(self):
        """ Test the __init__ method """
        amenity = Amenity(name="Wifi")
        self.assertEqual(amenity.name, "Wifi")

    def test_str(self):
        """ Test the __str__ method """
        amenity = Amenity(name="Wifi")
        self.assertEqual(str(amenity), "Amenity(name='Wifi')")

    def test_save(self):
        """ Test the save method """
        amenity = Amenity(name="Wifi")
        amenity.save()
        self.assertTrue(amenity.id > 0)


if __name__ == "__main__":
    unittest.main()

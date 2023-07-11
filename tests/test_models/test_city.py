import unittest

from models.city import City


class CityTest(unittest.TestCase):
    """ Unit tests for the City class """

    def test_init(self):
        """ Test the __init__ method """
        city = City(state_id="CA", name="Los Angeles")
        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "Los Angeles")

    def test_str(self):
        """ Test the __str__ method """
        city = City(state_id="CA", name="Los Angeles")
        self.assertEqual(
            str(city),
            f"[City] \
            ({city.id}) ({city.created_at}) ({city.state_id}: {city.name})",
        )

    def test_save(self):
        """ Test the save method """
        city = City(state_id="CA", name="Los Angeles")
        city.save()
        self.assertTrue(city.id > 0)

    def test_to_dict(self):
        """ Test the to_dict method """
        city = City(state_id="CA", name="Los Angeles")
        city_dict = city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(city_dict["state_id"], "CA")
        self.assertEqual(city_dict["name"], "Los Angeles")


if __name__ == "__main__":
    unittest.main()

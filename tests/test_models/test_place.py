import unittest

from models.place import Place


class PlaceTest(unittest.TestCase):
    """ Unit tests for the Place class """

    def test_init(self):
        """ Test the __init__ method """
        place = Place(
            city_id="CA",
            user_id="1",
            name="My Place",
            description="This is my place",
            number_rooms=2,
            number_bathrooms=1,
            max_guest=4,
            price_by_night=100,
            latitude=34.052222,
            longitude=-118.243333,
            amenity_ids=["1", "2"],
        )
        self.assertEqual(place.city_id, "CA")
        self.assertEqual(place.user_id, "1")
        self.assertEqual(place.name, "My Place")
        self.assertEqual(place.description, "This is my place")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 34.052222)
        self.assertEqual(place.longitude, -118.243333)
        self.assertEqual(place.amenity_ids, ["1", "2"])

    def test_str(self):
        """ Test the __str__ method """
        place = Place(
            city_id="CA",
            user_id="1",
            name="My Place",
            description="This is my place",
            number_rooms=2,
            number_bathrooms=1,
            max_guest=4,
            price_by_night=100,
            latitude=34.052222,
            longitude=-118.243333,
            amenity_ids=["1", "2"],
        )
        self.assertEqual(
            str(place),
            f"[Place] \
            ({place.id}) ({place.created_at}) ({place.city_id}: {place.name})",
        )

    def test_save(self):
        """ Test the save method """
        place = Place(
            city_id="CA",
            user_id="1",
            name="My Place",
            description="This is my place",
            number_rooms=2,
            number_bathrooms=1,
            max_guest=4,
            price_by_night=100,
            latitude=34.052222,
            longitude=-118.243333,
            amenity_ids=["1", "2"],
        )
        place.save()
        self.assertTrue(place.id > 0)

    def test_to_dict(self):
        """ Test the to_dict method """
        place = Place(
            city_id="CA",
            user_id="1",
            name="My Place",
            description="This is my place",
            number_rooms=2,
            number_bathrooms=1,
            max_guest=4,
            price_by_night=100,
            latitude=34.052222,
            longitude=-118.243333,
            amenity_ids=["1", "2"],
        )
        place_dict = place.to_dict()
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(place_dict["city_id"], "CA")
        self.assertEqual(place_dict["user_id"], "1")
        self.assertEqual(place_dict["name"], "My Place")
        self.assertEqual(place_dict["description"], "This is my place")
        self.assertEqual(place_dict["number_rooms"], 2)
        self.assertEqual(place_dict["number_bathrooms"], 1)
        self.assertEqual(place_dict["max_guest"], 4)

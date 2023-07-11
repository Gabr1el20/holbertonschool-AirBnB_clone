import unittest

from models.review import Review


class ReviewTest(unittest.TestCase):
    """ Unit tests for the Review class """

    def test_init(self):
        """ Test the __init__ method """
        review = Review(place_id="1", user_id="2", text="This is a review")
        self.assertEqual(review.place_id, "1")
        self.assertEqual(review.user_id, "2")
        self.assertEqual(review.text, "This is a review")

    def test_str(self):
        """ Test the __str__ method """
        review = Review(place_id="1", user_id="2", text="This is a review")
        self.assertEqual(
            str(review),
            f"[Review] ({review.id}) \
            ({review.created_at}) ({review.place_id}: {review.text})",
        )

    def test_save(self):
        """ Test the save method """
        review = Review(place_id="1", user_id="2", text="This is a review")
        review.save()
        self.assertTrue(review.id > 0)

    def test_to_dict(self):
        """ Test the to_dict method """
        review = Review(place_id="1", user_id="2", text="This is a review")
        review_dict = review.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertEqual(review_dict["place_id"], "1")
        self.assertEqual(review_dict["user_id"], "2")
        self.assertEqual(review_dict["text"], "This is a review")


if __name__ == "__main__":
    unittest.main()

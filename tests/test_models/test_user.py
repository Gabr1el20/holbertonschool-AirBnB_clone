import unittest

from models.user import User


class UserTest(unittest.TestCase):
    """ Unit tests for the User class """

    def test_init(self):
        """ Test the __init__ method """
        user = User(email="test@example.com", password="password",
                    first_name="John", last_name="Doe")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_str(self):
        """ Test the __str__ method """
        user = User(email="test@example.com", password="password",
                    first_name="John", last_name="Doe")
        self.assertEqual(
            str(user),
            f"[User] ({user.id}) ({user.created_at}) ({user.email})",
        )

    def test_save(self):
        """ Test the save method """
        user = User(email="test@example.com", password="password",
                    first_name="John", last_name="Doe")
        user.save()
        self.assertTrue(user.id > 0)

    def test_to_dict(self):
        """ Test the to_dict method """
        user = User(email="test@example.com", password="password",
                    first_name="John", last_name="Doe")
        user_dict = user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["email"], "test@example.com")
        self.assertEqual(user_dict["password"], "password")
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Doe")


if __name__ == "__main__":
    unittest.main()

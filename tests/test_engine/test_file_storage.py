import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


class FileStorageTest(unittest.TestCase):
    """ Unit tests for the FileStorage class """

    def setUp(self):
        """ Setup the test """
        self.file_storage = FileStorage()

    def tearDown(self):
        """ Teardown the test """
        os.remove("file.json")

    def test_all(self):
        """ Test the all method """
        self.assertEqual(self.file_storage.all(), {})

    def test_new(self):
        """ Test the new method """
        user = User(email="test@example.com", password="password",
                    first_name="John", last_name="Doe")
        self.file_storage.new(user)
        self.assertEqual(self.file_storage.all(), {"User.1": user})

    def test_save(self):
        """ Test the save method """
        user = User(email="test@example.com", password="password",
                    first_name="John", last_name="Doe")
        self.file_storage.new(user)
        self.file_storage.save()
        with open("file.json") as f:
            data = json.load(f)
        self.assertEqual(data, {"User.1": user.to_dict()})

    def test_reload(self):
        """ Test the reload method """
        user = User(email="test@example.com", password="password",
                    first_name="John", last_name="Doe")
        data = {"User.1": user.to_dict()}
        with open("file.json", "w") as f:
            json.dump(data, f)
        self.file_storage.reload()
        self.assertEqual(self.file_storage.all(), {"User.1": user})


if __name__ == "__main__":
    unittest.main()

import unittest

from models.base_model import BaseModel
import datetime
from uuid import uuid4


class BaseModelTest(unittest.TestCase):
    """ Unit tests for the BaseModel class """

    def test_init(self):
        """ Test the __init__ method """
        base_model = BaseModel()
        self.assertEqual(base_model.id, str(uuid4()))
        self.assertEqual(base_model.created_at, datetime.now())
        self.assertEqual(base_model.updated_at, datetime.now())

    def test_str(self):
        """ Test the __str__ method """
        base_model = BaseModel()
        self.assertEqual(
            str(base_model),
            f"[BaseModel] \
            ({base_model.id}) ({base_model.created_at}) {base_model.__dict__}",
        )

    def test_save(self):
        """ Test the save method """
        base_model = BaseModel()
        base_model.save()
        self.assertTrue(base_model.id > 0)

    def test_to_dict(self):
        """ Test the to_dict method """
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertEqual(base_model_dict["__class__"], "BaseModel")
        self.assertEqual(
            base_model_dict["created_at"], base_model.created_at.isoformat()
        )
        self.assertEqual(
            base_model_dict["updated_at"], base_model.updated_at.isoformat()
        )


if __name__ == "__main__":
    unittest.main()

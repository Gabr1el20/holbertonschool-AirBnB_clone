import unittest

from models.state import State


class StateTest(unittest.TestCase):
    """ Unit tests for the State class """

    def test_init(self):
        """ Test the __init__ method """
        state = State(name="California")
        self.assertEqual(state.name, "California")

    def test_str(self):
        """ Test the __str__ method """
        state = State(name="California")
        self.assertEqual(
            str(state),
            f"[State] ({state.id}) ({state.created_at}) ({state.name})",
        )

    def test_save(self):
        """ Test the save method """
        state = State(name="California")
        state.save()
        self.assertTrue(state.id > 0)

    def test_to_dict(self):
        """ Test the to_dict method """
        state = State(name="California")
        state_dict = state.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(state_dict["name"], "California")


if __name__ == "__main__":
    unittest.main()

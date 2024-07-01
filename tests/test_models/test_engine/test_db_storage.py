import unittest
import MySQLdb
from models import storage
import os

class TestDBStorage(unittest.TestCase):
    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "Skipping DBStorage tests for FileStorage")
    def test_create_state(self):
        # Connect to the test database
        db = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cursor = db.cursor()

        # Get initial count of states
        cursor.execute("SELECT COUNT(*) FROM states;")
        initial_count = cursor.fetchone()[0]

        # Perform the action: create a new state
        # Assuming you have a method to create state
        storage.create(State, name="California")

        # Get the new count of states
        cursor.execute("SELECT COUNT(*) FROM states;")
        new_count = cursor.fetchone()[0]

        # Assert the difference is +1
        self.assertEqual(new_count, initial_count + 1)

        cursor.close()
        db.close()

if __name__ == "__main__":
    unittest.main()


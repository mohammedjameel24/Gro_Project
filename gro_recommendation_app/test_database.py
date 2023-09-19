#python
# Import necessary libraries
import unittest
import sqlite3
from sqlite3 import Error
import database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.conn = database.create_connection()

    def tearDown(self):
        self.conn.close()

    def test_create_connection(self):
        self.assertIsNotNone(self.conn, "Connection should not be None")

    def test_create_table(self):
        database.create_table(self.conn)
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='recommendations'")
        self.assertIsNotNone(cursor.fetchone(), "Table should exist")

    def test_insert_recommendation(self):
        database.create_table(self.conn)
        recommendation = (1, 1, 5)
        database.insert_recommendation(self.conn, recommendation)
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM recommendations WHERE user_id=? AND product_id=? AND rating=?", recommendation)
        self.assertIsNotNone(cursor.fetchone(), "Inserted recommendation should exist")

    def test_select_all_recommendations(self):
        database.create_table(self.conn)
        recommendations = [(1, 1, 5), (2, 2, 4), (3, 3, 3)]
        for recommendation in recommendations:
            database.insert_recommendation(self.conn, recommendation)
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM recommendations")
        rows = cursor.fetchall()
        self.assertEqual(len(rows), len(recommendations), "All inserted recommendations should be selected")

if __name__ == '__main__':
    unittest.main()


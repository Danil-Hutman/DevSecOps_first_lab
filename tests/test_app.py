import unittest

from src.app import get_db_connection, app

class TestDatabase(unittest.TestCase):
    def test_fetch_cactus_data(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Cactus")
        rows = cursor.fetchall()

        self.assertGreater(len(rows), 0, "Таблиця Cactus порожня або недоступна")

        first = rows[0]
        self.assertIn("id", first)
        self.assertIn("name", first)
        self.assertIn("description", first)
        self.assertIn("price", first)

        cursor.close()
        conn.close()

if __name__ == "__main__":
    unittest.main()
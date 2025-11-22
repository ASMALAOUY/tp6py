import unittest
from film import Film


class TestFilm(unittest.TestCase):

    def test_creation(self):
        f = Film("Inception", "Nolan", 2010, 8.8)
        self.assertEqual(f.titre, "Inception")

    def test_note_invalide(self):
        with self.assertRaises(ValueError):
            Film("Test", "X", 2000, 15)

    def test_est_classique(self):
        f = Film("Matrix", "Wachowski", 1999, 9)
        self.assertTrue(f.est_classique())

    def test_immutabilite(self):
        f = Film("Inception", "Nolan", 2010, 8.8)
        with self.assertRaises(Exception):
            f.note = 5

    def test_to_json(self):
        f = Film("Test", "X", 2000, 7.5)
        self.assertIn('"note": 7.5', f.to_json())

    def test_from_json(self):
        json_data = '{"titre": "Test", "realisateur": "X", "annee": 2000, "note": 7.5}'
        f = Film.from_json(json_data)
        self.assertEqual(f.note, 7.5)

    def test_tri(self):
        films = [
            Film("A", "X", 2000, 9),
            Film("B", "X", 2000, 5),
            Film("C", "X", 2000, 7),
        ]
        tri = sorted(films)
        self.assertEqual([f.note for f in tri], [5, 7, 9])


if __name__ == "__main__":
    unittest.main()

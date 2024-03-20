import unittest
import pandas as pd

class TestDevOps(unittest.TestCase):

    def test_excel_file(self):
        df = pd.read_excel("sample.xlsx")  # Test odczytu pliku Excel
        self.assertEqual(len(df), 4)  # Sprawdzenie liczby wierszy w pliku Excel

    def test_html_file(self):
        with open("index.html", "r") as file:
            html_content = file.read()
            self.assertTrue("<table>" in html_content)  # Sprawdzenie czy plik HTML zawiera tabelę
            self.assertTrue("<tr>" in html_content)    # Sprawdzenie czy plik HTML zawiera wiersze w tabeli

if __name__ == '__main__':
    unittest.main()

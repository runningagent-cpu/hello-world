import io
import unittest
from contextlib import redirect_stdout

from main import main


class MainTest(unittest.TestCase):
    def test_main_prints_hello_world(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            main()
        self.assertEqual(output.getvalue(), "Hello, World!\n")


if __name__ == "__main__":
    unittest.main()

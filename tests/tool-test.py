#
# Unit test cli
#

# imports
import os.path
import unittest
from cli.tool import check_extension
from cli.tool import file_read


class TestCli(unittest.TestCase):

    def test_extension(self):
        newName = check_extension("pyper")
        self.assertEqual(newName, "pyper.py", "File name is invalid")
        newName = check_extension("pyper.py")
        self.assertEqual(newName, "pyper.py", "File name is invalid")

    def test_read(self):
        file_path = 'test.py'
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write("test line")
        file_read(file_path)
        os.remove(file_path)

    def test_cli(self):
        pass  # Only cli wrapper here


if __name__ == '__main__':
    unittest.main()

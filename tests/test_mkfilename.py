import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__),os.pardir))

import unittest
import datetime
from click.testing import CliRunner

from mkfilename import mkfilename

class MyTestCase(unittest.TestCase):
    def test_converting_a_heading(self):
        s = 'Python is a high-level, interpreted, general-purpose programming language.'
        t = datetime.datetime.now().strftime("%y%m%d")
        runner = CliRunner()
        result = runner.invoke(mkfilename, ['--string', s, '--stdout'])
        print(result)
        self.assertEqual(result.stdout,
                         f'{t}-python-is-a-high-level-interpreted-general-purpose-programming-language.md\n')
    def test_converting_a_filename(self):
        s = 'Python Logo.png'
        t = datetime.datetime.now().strftime("%y%m%d")
        runner = CliRunner()
        result = runner.invoke(mkfilename, ['--string', s, '--stdout'])
        print(result)
        self.assertEqual(result.stdout,
                         f'{t}-python-logo.png\n')


if __name__ == '__main__':
    unittest.main()

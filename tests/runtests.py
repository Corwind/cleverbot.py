import unittest

import cleverbot3


class Cleverbot(unittest.TestCase):
    def test_replay(self):
        cbc = cleverbot3.Cleverbot()
        response = cbc.ask("Hi. How are you?")
        print(response)
        self.assertNotEqual(response, str())


def main():
    unittest.main()

if __name__ == '__main__':
    main()

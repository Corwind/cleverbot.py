import unittest

import cleverbot3


class Cleverbot(unittest.TestCase):
    def test_replay(self):
        cbc = cleverbot3.Cleverbot()
        response = cbc.ask("Coucou, ça va ?")
        print(response)
        response = cbc.ask("Tu veux pas me faire un de caractère non-ASCII"
                "PLZ ?")
        print(response)
        response = cbc.ask("Hey je te parle là.")
        print(response)
        response = cbc.ask("HEY HO PARLE MOI")
        print(response)
        response = cbc.ask("Bon j'en ai marre.")
        print(response)
        self.assertNotEqual(response, str())


def main():
    unittest.main()

if __name__ == '__main__':
    main()

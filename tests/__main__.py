from context import pendulum

import unittest

class BasicTestSuite(unittest.TestCase):
    def testPendulumLoaded(self):
        self.assertEqual(pendulum.testPendulumLoaded(), 'Pendulum Loaded')


if __name__ == "__main__":
    # execute only if run as the entry point into the program
    unittest.main()

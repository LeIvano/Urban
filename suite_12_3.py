import unittest
import tests_12_3


if __name__ == '__main__':
    t_suite = unittest.TestSuite()
    t_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
    t_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(t_suite)

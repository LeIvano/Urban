import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        some_runner = runner.Runner("Igor")
        for _ in range(10):
            some_runner.walk()

        self.assertEqual(some_runner.distance, 50)

    def test_run(self):
        some_runner = runner.Runner("Mark")
        for _ in range(10):
            some_runner.run()

        self.assertEqual(some_runner.distance, 100)

    def test_challenge(self):
        some_runner_first = runner.Runner("Mark")
        for _ in range(10):
            some_runner_first.run()

        some_runner_second = runner.Runner("Igor")
        for _ in range(10):
            some_runner_second.walk()

        self.assertNotEqual(some_runner_first.distance, some_runner_second.distance)


if __name__ == '__main__':
    unittest.main()

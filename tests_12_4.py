import logging
import unittest
import rt_with_exceptions as r_and_t


class RunnerTest(unittest.TestCase):
    __is_frozen = False

    @unittest.skipIf(__is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            some_runner = r_and_t.Runner("Igor", speed=-1)
            for _ in range(10):
                some_runner.walk()

            self.assertEqual(some_runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')

        except ValueError as error:
            logging.warning('Неверная скорость для Runner')

    @unittest.skipIf(__is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            some_runner = r_and_t.Runner(5)
            for _ in range(10):
                some_runner.run()

            self.assertEqual(some_runner.distance, 100)
            logging.info('"test_run" выполнен успешно')

        except TypeError as error:
            logging.warning('Неверный тип данных для объекта Runner')

    @unittest.skipIf(__is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        some_runner_first = r_and_t.Runner("Mark")
        for _ in range(10):
            some_runner_first.run()

        some_runner_second = r_and_t.Runner("Igor")
        for _ in range(10):
            some_runner_second.walk()

        self.assertNotEqual(some_runner_first.distance, some_runner_second.distance)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        filemode='w',
                        filename='runner_tests.log',
                        encoding='utf-8',
                        format="%(asctime)s | %(levelname)s | %(message)s")
    unittest.main()

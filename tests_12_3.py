import r_and_t
import unittest


class RunnerTest(unittest.TestCase):
    __is_frozen = False

    @unittest.skipIf(__is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        some_runner = r_and_t.Runner("Igor")
        for _ in range(10):
            some_runner.walk()

        self.assertEqual(some_runner.distance, 50)

    @unittest.skipIf(__is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        some_runner = r_and_t.Runner("Mark")
        for _ in range(10):
            some_runner.run()

        self.assertEqual(some_runner.distance, 100)

    @unittest.skipIf(__is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        some_runner_first = r_and_t.Runner("Mark")
        for _ in range(10):
            some_runner_first.run()

        some_runner_second = r_and_t.Runner("Igor")
        for _ in range(10):
            some_runner_second.walk()

        self.assertNotEqual(some_runner_first.distance, some_runner_second.distance)


class TournamentTest(unittest.TestCase):
    __is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = list()

    def setUp(self):
        self.first_runner = r_and_t.Runner('Усэйн', 10)
        self.second_runner = r_and_t.Runner('Андрей', 9)
        self.third_runner = r_and_t.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)

    @unittest.skipIf(__is_frozen, "Тесты в этом кейсе заморожены")
    def test1_tournament(self):
        first_tourn = r_and_t.Tournament(90, self.first_runner, self.third_runner)
        self.all_results.append(first_tourn.start())
        name = self.all_results[len(self.all_results) - 1][len(self.all_results[len(self.all_results) - 1])]
        self.assertTrue(name == 'Ник')

    @unittest.skipIf(__is_frozen, "Тесты в этом кейсе заморожены")
    def test2_tournament(self):
        second_tourn = r_and_t.Tournament(90, self.second_runner, self.third_runner)
        self.all_results.append(second_tourn.start())
        name = self.all_results[len(self.all_results) - 1][len(self.all_results[len(self.all_results) - 1])]
        self.assertTrue(name == 'Ник')

    @unittest.skipIf(__is_frozen, "Тесты в этом кейсе заморожены")
    def test3_tournament(self):
        third_tourn = r_and_t.Tournament(90, self.first_runner, self.second_runner, self.third_runner)
        self.all_results.append(third_tourn.start())
        name = self.all_results[len(self.all_results) - 1][len(self.all_results[len(self.all_results) - 1])]
        self.assertTrue(name == 'Ник')

import r_and_t
import unittest


class TournamentTest(unittest.TestCase):

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

    def test1_tournament(self):
        first_tourn = r_and_t.Tournament(90, self.first_runner, self.third_runner)
        self.all_results.append(first_tourn.start())
        name = self.all_results[len(self.all_results) - 1][len(self.all_results[len(self.all_results) - 1])]
        self.assertTrue(name == 'Ник')

    def test2_tournament(self):
        second_tourn = r_and_t.Tournament(90, self.second_runner, self.third_runner)
        self.all_results.append(second_tourn.start())
        name = self.all_results[len(self.all_results) - 1][len(self.all_results[len(self.all_results) - 1])]
        self.assertTrue(name == 'Ник')

    def test3_tournament(self):
        third_tourn = r_and_t.Tournament(90, self.first_runner, self.second_runner, self.third_runner)
        self.all_results.append(third_tourn.start())
        name = self.all_results[len(self.all_results) - 1][len(self.all_results[len(self.all_results) - 1])]
        self.assertTrue(name == 'Ник')


if __name__ == '__main__':
    unittest.main()

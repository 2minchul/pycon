import time
from unittest import TestCase

from .solution import Solution
from .problems import problem_set


class MyTest(TestCase):
    def adjust_result(self, result):
        return result

    @classmethod
    def setUpClass(cls):
        cls.solver = Solution()
        cls.start = time.time()

    @classmethod
    def tearDownClass(cls):
        elapsed = time.time() - cls.start

    @classmethod
    def patch(cls):
        def test_factory(test):
            def test_function(self):
                input_, expected = test
                actual = self.solver.solve(input_)
                self.assertEqual(
                    self.adjust_result(actual),
                    self.adjust_result(expected)
                )

            return test_function

        for i, test in enumerate(problem_set):
            setattr(cls, 'test_{}'.format(i), test_factory(test))


MyTest.patch()

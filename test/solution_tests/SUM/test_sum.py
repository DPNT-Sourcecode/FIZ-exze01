
from lib.solutions.SUM import sum_solution
import pytest
class TestSum():
    def test_sum(self):
        # test sum function return expected putput
        assert sum_solution.compute(1, 2) == 3
    
    def test_sum_negative_numbers(self):
        # test sun function raise error when the number is negative
        with pytest.raises(ValueError):
            sum_solution.compute(-1,7)

    def test_sum_number_higher_than_100(self):
        with pytest.raises(ValueError):
            sum_solution.compute(200,5)
        




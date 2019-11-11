
from lib.solutions.SUM import sum_solution
import pytest
class TestSum():
    def test_sum(self):
        # test sum function return expected putput
        assert sum_solution.compute(1, 2) == 3
    
    def test_sum_raise_error_when_negative_numbers(self):
        # test sun function raise error when the number is not integer positive
        with pytest.raises(ValueError):
            sum_solution.compute(-1,7)
            
    def test_sum_raise_erro_when_adds_floats(self):
        # test sun function raise error when the numbers are floats
        with pytest.raises(ValueError):
            sum_solution.compute(1.5,5.9)

    def test_sum_number_higher_than_100(self):
        # test function raises error when number higher than 100
        with pytest.raises(ValueError):
            sum_solution.compute(200,5)
        

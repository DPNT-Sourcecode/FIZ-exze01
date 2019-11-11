
from lib.solutions.FIZ import fizz_buzz_solution
import pytest
class TestSum():
    def test_fiz(self):
        # test sum function return expected putput
        assert fizz_buzz_solution.fizz_buzz(3) == "fizz"
        assert fizz_buzz_solution.fizz_buzz(5) == "buzz"
        assert fizz_buzz_solution.fizz_buzz(30) == "fizz buzz"
    
    
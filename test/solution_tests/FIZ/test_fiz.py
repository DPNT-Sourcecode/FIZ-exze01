
from lib.solutions.FIZ import fizz_buzz_solution
import pytest
class TestSum():
    def test_fiz(self):
        # test sum function return expected putput
        assert fizz_buzz_solution.fizz_buzz(3) == "fizz"
        assert fizz_buzz_solution.fizz_buzz(5) == "buzz"
        assert fizz_buzz_solution.fizz_buzz(30) == "fizz buzz"
        assert fizz_buzz_solution.fizz_buzz(2) == 2
        assert fizz_buzz_solution.fizz_buzz(15) == "fizz buzz"
        assert fizz_buzz_solution.fizz_buzz(37) == 'fizz'
        assert fizz_buzz_solution.fizz_buzz(50) == 'buzz'
        assert fizz_buzz_solution.fizz_buzz(45) == "fizz buzz"
        assert fizz_buzz_solution.fizz_buzz(546) == "fizz buzz"



    
    

from lib.solutions.FIZ import fizz_buzz_solution
import pytest
class TestSum():
    def test_fiz(self):
        # test sum function return expected putput
        assert fizz_buzz_solution.fizz_buzz(3) == "fizz fake deluxe"
        assert fizz_buzz_solution.fizz_buzz(5) == "buzz fake deluxe"
        assert fizz_buzz_solution.fizz_buzz(30) == "fizz buzz deluxe"
        assert fizz_buzz_solution.fizz_buzz(2) == 2
        assert fizz_buzz_solution.fizz_buzz(15) == "fizz buzz fake deluxe"
        assert fizz_buzz_solution.fizz_buzz(37) == 'fizz'
        assert fizz_buzz_solution.fizz_buzz(50) == 'buzz deluxe'
        assert fizz_buzz_solution.fizz_buzz(555) == "fizz buzz fake deluxe"
        assert fizz_buzz_solution.fizz_buzz(546) == "fizz buzz"
        assert fizz_buzz_solution.fizz_buzz(22) == 22
        assert fizz_buzz_solution.fizz_buzz(111) == "fizz"
        assert fizz_buzz_solution.fizz_buzz(99) == "fizz"
        assert fizz_buzz_solution.fizz_buzz(33) == "fizz fake deluxe"
        assert fizz_buzz_solution.fizz_buzz(222) == "fizz"
        assert fizz_buzz_solution.fizz_buzz(777) == "fizz"
    
    

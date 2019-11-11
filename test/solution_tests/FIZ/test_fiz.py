
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
        assert fizz_buzz_solution.fizz_buzz(555) == "fizz buzz fake deluxe"
        assert fizz_buzz_solution.fizz_buzz(546) == "fizz buzz"
        assert fizz_buzz_solution.fizz_buzz(22) == "deluxe"
        assert fizz_buzz_solution.fizz_buzz(11) == "fake deluxe"
        assert fizz_buzz_solution.fizz_buzz(77) == "fake deluxe"
        assert fizz_buzz_solution.fizz_buzz(111) == "fizz fake deluxe"
        assert fizz_buzz_solution.fizz_buzz(99) == "fizz fake deluxe"
        assert fizz_buzz_solution.fizz_buzz(33) == "fizz fake deluxe"
        assert fizz_buzz_solution.fizz_buzz(222) == "fizz deluxe"
        assert fizz_buzz_solution.fizz_buzz(777) == "fizz fake deluxe"
    
    
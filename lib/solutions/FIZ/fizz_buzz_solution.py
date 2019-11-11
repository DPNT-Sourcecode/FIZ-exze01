# noinspection PyUnusedLocal
def fizz_buzz(number):
    if not (1 <= number <= 9999):
        raise ValueError("NUmber not between 1 and 9999")
    if _check_multiple_of(number,15):
        return  "fizz buzz"    
    elif _check_multiple_of(number,3):
        return "fizz"
    elif _check_multiple_of(number,5):
        return "buzz"
    
    else:
        return number
   

def _check_multiple_of(n, k):
    if n % k == 0:
        return True



